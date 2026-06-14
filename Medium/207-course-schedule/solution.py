# Problem 207: Course Schedule
# Difficulty: Medium
# Link: https://leetcode.com/problems/course-schedule/
# Language: python3
# ────────────────────────────────────────

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs=defaultdict(list)
        for c,p in prerequisites:
            prereqs[c].append(p)

        def cycle(course,visit):
            if course in visit:
                return True
            visit.add(course)
            for p in prereqs[course]:
                if cycle(p,visit):
                    return True
            prereqs[course]=[]
            visit.remove(course)
            return False
        
        visit=set()
        for course in range(numCourses):
            if cycle(course,visit):
                return False
        return True
        