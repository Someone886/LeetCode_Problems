# Last updated: 6/22/2025, 2:50:40 PM
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for sequence, t in enumerate(tasks):
            t.append(sequence)
        
        tasks.sort(key = lambda x: x[0])

        time = 1
        q = []
        heapq.heapify(q)
        index = 0
        seq = []

        while index < len(tasks):
            task = tasks[index]
            while task and time >= task[0]:
                # task stores required time to process a task and original index of the task
                heapq.heappush(q, (task[1], task[2])) 
                index += 1
                if index < len(tasks):
                    task = tasks[index]
                else:
                    task = None

            
            if len(q) != 0:
                next_task = heapq.heappop(q)
                seq.append(next_task[1])
                time += next_task[0]
            else:
                time = task[0]
        
        while q:
            next_task = heapq.heappop(q)
            seq.append(next_task[1])
        
        return seq