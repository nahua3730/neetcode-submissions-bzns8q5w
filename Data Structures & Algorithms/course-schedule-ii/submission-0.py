from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph= {i: [] for i in range(numCourses)}
        indegree=[0]*numCourses
        for course, pre in prerequisites:
            indegree[course]+=1
            graph[pre].append(course)
        queue=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        order=[]
        while queue:
            course=queue.popleft()
            order.append(course)
            for neighbor in graph[course]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
        if len(order)==numCourses:
            return order
        return []