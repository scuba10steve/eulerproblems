import time


def set_start_time():
    global start_time
    start_time = time.time()
    print("Start Time: ", start_time)


def get_elapsed():
    end_time = time.time()
    print("End Time: ", end_time)
    elapsed = end_time - start_time
    print("Elapsed: ", elapsed)
    return elapsed

