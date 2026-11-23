from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        # Build graph: prereq -> course
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1
            
        # Start with courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        completed = 0
        
        while queue:
            curr = queue.popleft()
            completed += 1
            
            for next_course in adj[curr]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
                    
        return completed == numCourses
            
           