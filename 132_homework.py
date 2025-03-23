from collections import deque

def solution(plans):
    
    def time_to_min(time):
        h, m = map(int, time.split(':'))
        return h*60 + m
    
    plans.sort(key=lambda x: time_to_min(x[1]))
    # sort by start time in ascending order
    
    task_queue = deque([(name, time_to_min(start), int(playtime)) for name, start, playtime in plans])
    paused_tasks = []  #stack to store paused tasks
    completed_tasks = []  #list to store completed tasks
    current_time = 0
    
    print(f"task_queue : {task_queue}")
    
    while task_queue:
    #go through the task_queue until all tasks are done 
        name, start, duration = task_queue.popleft()
        
        while start > current_time and paused_tasks:
            
            
        #if there is time to do paused tasks before the next new task starts

            
            

        
        
        
        
        
        
        
        
#Test cases
plans = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
print(solution(plans))
        

        
        