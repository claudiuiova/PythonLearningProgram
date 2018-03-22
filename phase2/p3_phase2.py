"""
P3. Write a function decorator that tracks how long the execution of 
the wrapped function took. The decorator will log slow function calls including details 
about the execution time and function name. The decorator should take an optional threshold argument.
"""
import time

def arguments_dec(threshold = None):
    def time_track(func):
        def func_wrapper(*args, **kwargs):
            time_start = time.time()
            func(*args, **kwargs)
            elapsed_time = time.time() - time_start
            
            if not callable(threshold):
                if threshold > elapsed_time:
                    return elapsed_time
                else:
                    print("Function execution took too long")
                    return func()
            else:
                return elapsed_time
            
        return func_wrapper
    
    if callable(threshold):
        return time_track(threshold)
    else:
        return time_track

@arguments_dec(threshold= 0.3)
def my_func():
    for _ in range(9999999):
        pass
    return ("Somtext")

@arguments_dec
def my_func1():
    for _ in range(9999999):
        pass
    return ("Somtext1")

@arguments_dec
def my_func2(x):
    for _ in range(x):
        pass
    return ("Somtext2")

print(my_func())
print(my_func1())
print(my_func2(9999999))