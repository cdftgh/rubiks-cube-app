import time

is_running = False
def start():
    global is_running
    global start_time
    if not is_running:
        is_running = True
        start_time = time.time()
        update_time()
 
# Stop the stopwatch
def stop():
    global is_running
    is_running = False
 
# Update the elapsed time
def update_time():
    global elapsed_time
    if is_running:
        elapsed_time = time.time() - start_time
