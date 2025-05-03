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
        
        name, start_time, duration = task_queue.popleft()
        print(f"Starting new task: {name}, Start time: {start_time}, Duration: {duration}")
        
        while paused_tasks and current_time < start_time:
            # Check if there are paused tasks and if the current time is less than the start time of the new task
            last_task, remaining_time = paused_tasks.pop()
            print(f"Trying to finish paused task: {last_task}, Remaining time: {remaining_time}, Current time: {current_time}")
            
            if current_time + remaining_time <= start_time:
                # If the paused task can be completed before the new task starts
                current_time += remaining_time
                completed_tasks.append(last_task)
                print(f"Finished paused task: {last_task}, Current time: {current_time}")
            else:
                remaining_time -= (start_time - current_time)
                paused_tasks.append((last_task, remaining_time))
                print(f"Paused task again: {last_task}, New remaining time: {remaining_time}")
                current_time = start_time
                break
        
        if current_time < start_time:
            current_time = start_time
        if 
            
        

            
            

        
        
        
        
        
        
        
        
#Test cases
plans = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
print(solution(plans))
        

        
        