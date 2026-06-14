"""
fetch_solutions.py
==================
Fetches your first 100 accepted LeetCode submissions and organizes them
into Easy / Medium / Hard folders.

HOW TO USE:
-----------
1. Create a .env file in the same folder with:
      LEETCODE_SESSION=your_session_cookie
      CSRF_TOKEN=your_csrftoken

2. Make sure .gitignore contains: .env

3. Run:
      pip install requests python-dotenv
      python fetch_solutions.py
"""

import requests
import os
import time
from dotenv import load_dotenv

# ── Load cookies from .env ──
load_dotenv()
LEETCODE_SESSION  = os.getenv("LEETCODE_SESSION", "")
CSRF_TOKEN        = os.getenv("CSRF_TOKEN", "")
LEETCODE_USERNAME = "S6sDRAvCKS"
MAX_PROBLEMS      = 100
OUTPUT_DIR        = "."

GRAPHQL_URL = "https://leetcode.com/graphql"

LANG_EXT = {
    "python3": "py", "python": "py",
    "cpp": "cpp", "c": "c",
    "java": "java", "javascript": "js", "typescript": "ts",
}

def get_headers():
    return {
        "Content-Type": "application/json",
        "Cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}; csrftoken={CSRF_TOKEN}",
        "x-csrftoken": CSRF_TOKEN,
        "Referer": "https://leetcode.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    }

def fetch_submissions(offset=0, limit=20):
    """Fetch a page of submissions (all statuses, we filter accepted manually)."""
    query = """
    query submissionList($offset: Int!, $limit: Int!, $lastKey: String, $questionSlug: String) {
      submissionList(offset: $offset, limit: $limit, lastKey: $lastKey, questionSlug: $questionSlug) {
        lastKey
        hasNext
        submissions {
          id
          statusDisplay
          lang
          timestamp
          title
          titleSlug
        }
      }
    }
    """
    variables = {
        "offset": offset,
        "limit": limit,
        "lastKey": None,
        "questionSlug": None
    }
    try:
        response = requests.post(
            GRAPHQL_URL,
            json={"query": query, "variables": variables},
            headers=get_headers(),
            timeout=15
        )
        if response.status_code != 200:
            print(f"❌ Error {response.status_code}: {response.text[:300]}")
            return None
        return response.json()
    except Exception as e:
        print(f"❌ Request failed: {e}")
        return None

def fetch_submission_code(submission_id):
    query = """
    query submissionDetails($submissionId: Int!) {
      submissionDetails(submissionId: $submissionId) {
        code
        lang { name }
      }
    }
    """
    try:
        response = requests.post(
            GRAPHQL_URL,
            json={"query": query, "variables": {"submissionId": int(submission_id)}},
            headers=get_headers(),
            timeout=15
        )
        if response.status_code != 200:
            return None
        return response.json().get("data", {}).get("submissionDetails", {})
    except:
        return None

def fetch_problem_details(title_slug):
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionFrontendId
        difficulty
        title
        titleSlug
      }
    }
    """
    try:
        response = requests.post(
            GRAPHQL_URL,
            json={"query": query, "variables": {"titleSlug": title_slug}},
            headers=get_headers(),
            timeout=15
        )
        if response.status_code != 200:
            return None
        return response.json().get("data", {}).get("question", {})
    except:
        return None

def slugify(title):
    # Remove characters Windows does not allow in folder names
    for ch in ["\\", "/", ":", "*", "?", '"', "<", ">", "|"]:
        title = title.replace(ch, "")
    return (title.lower()
            .replace(" ", "-")
            .replace("(", "")
            .replace(")", "")
            .replace("'", "")
            .strip("-"))

def create_solution_file(problem_num, title, title_slug, difficulty, code, lang, idx):
    ext = LANG_EXT.get(lang, "txt")
    folder_name = f"{str(problem_num).zfill(3)}-{slugify(title)}"
    folder_path = os.path.join(OUTPUT_DIR, difficulty, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    solution_path = os.path.join(folder_path, f"solution.{ext}")
    if not os.path.exists(solution_path):
        header = (
            f"# Problem {problem_num}: {title}\n"
            f"# Difficulty: {difficulty}\n"
            f"# Link: https://leetcode.com/problems/{title_slug}/\n"
            f"# Language: {lang}\n"
            f"# {'─'*40}\n\n"
        )
        with open(solution_path, "w", encoding="utf-8") as f:
            f.write(header + code)
        print(f"  ✅ [{idx:03d}] {title} ({difficulty})")
    else:
        print(f"  ⏭️  [{idx:03d}] {title} — skipped (exists)")

    notes_path = os.path.join(folder_path, "notes.md")
    if not os.path.exists(notes_path):
        with open(notes_path, "w", encoding="utf-8") as f:
            f.write(
                f"# {title}\n\n"
                f"**Difficulty:** {difficulty}  \n"
                f"**Link:** https://leetcode.com/problems/{title_slug}/  \n"
                f"**Language:** {lang}  \n\n"
                f"## 🧠 Approach\n\n<!-- your approach here -->\n\n"
                f"## ⏱️ Complexity\n\n- **Time:** O(?)\n- **Space:** O(?)\n"
            )

def main():
    print("🚀 LeetCode Solution Fetcher")
    print(f"👤 Username : {LEETCODE_USERNAME}")
    print(f"🎯 Target   : First {MAX_PROBLEMS} accepted submissions\n")

    if not LEETCODE_SESSION or not CSRF_TOKEN:
        print("❌ .env file not found or empty!")
        print("Create .env with:\n  LEETCODE_SESSION=...\n  CSRF_TOKEN=...")
        return

    print("📥 Fetching submissions from LeetCode...")
    seen_slugs = set()
    collected  = []
    offset     = 0

    while len(collected) < MAX_PROBLEMS:
        data = fetch_submissions(offset=offset, limit=20)
        if not data:
            break

        sub_list = data.get("data", {}).get("submissionList", {})
        submissions = sub_list.get("submissions", [])
        has_next    = sub_list.get("hasNext", False)

        for sub in submissions:
            # Only keep Accepted submissions
            if sub.get("statusDisplay") != "Accepted":
                continue
            slug = sub["titleSlug"]
            if slug not in seen_slugs:
                seen_slugs.add(slug)
                collected.append(sub)
                if len(collected) >= MAX_PROBLEMS:
                    break

        print(f"  📄 {len(collected)} accepted unique problems so far...")

        if not has_next or not submissions:
            break
        offset += 20
        time.sleep(1)

    if not collected:
        print("\n❌ No accepted submissions found.")
        print("→ Make sure you're logged in and cookies are fresh.")
        return

    # Sort oldest → newest
    collected.sort(key=lambda x: int(x["timestamp"]))
    first_100 = collected[:MAX_PROBLEMS]

    print(f"\n✅ Found {len(collected)} accepted problems. Processing first {len(first_100)}...\n")

    for i, sub in enumerate(first_100, 1):
        title      = sub["title"]
        title_slug = sub["titleSlug"]
        sub_id     = sub["id"]
        lang       = sub["lang"]

        problem = fetch_problem_details(title_slug)
        if not problem:
            print(f"  ⚠️  Skipping {title} — couldn't get problem details")
            continue

        difficulty  = problem.get("difficulty", "Easy")
        problem_num = problem.get("questionFrontendId", str(i))

        details = fetch_submission_code(sub_id)
        if not details:
            print(f"  ⚠️  Skipping {title} — couldn't get code")
            continue

        code = details.get("code", "# Code unavailable")
        create_solution_file(problem_num, title, title_slug, difficulty, code, lang, i)
        time.sleep(0.5)

    print(f"\n🎉 Done! Solutions saved to Easy / Medium / Hard folders.")
    print("\n📌 Now run:")
    print('  git add Easy/ Medium/ Hard/')
    print('  git commit -m "feat: add first 100 LeetCode solutions 🚀"')
    print('  git push')

if __name__ == "__main__":
    main()