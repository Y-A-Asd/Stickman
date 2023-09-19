import logging
import functools
import time
import psutil

def measure_memory_usage():
    process = psutil.Process()
    memory_usage = process.memory_info().rss  # in B
    return memory_usage
def custom_decorator(func):
    logging.basicConfig(filename='app.log', level=logging.DEBUG, filemode='a',
                        format='%(asctime)s-%(process)d-%(levelname)s-%(message)s')
    logging.debug(f"called function {func.__name__}")
    start_time = time.time()
    start_memory = measure_memory_usage()
    @functools.lru_cache(maxsize=None)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    end_time = time.time()
    execution_time = end_time - start_time
    end_memory = measure_memory_usage()
    memory_usage_diff = end_memory - start_memory
    print(f"Function '{func.__name__}' with argutook {execution_time:.2f} seconds to execute")
    print(f"Memory usage difference: {memory_usage_diff:.2f} B")
    logging.debug(f"Memory usage difference: {memory_usage_diff:.2f} B")
    logging.debug(f"Function '{func.__name__}' took {execution_time:.2f} seconds to execute")
    return wrapper

@custom_decorator
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
fibonacci(330)
@custom_decorator
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
factorial(300)


start_time = time.time()
start_memory = measure_memory_usage()
def fibonacci1(n):
    if n <= 1:
        return n
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)
fibonacci1(90)
end_time = time.time()
execution_time = end_time - start_time
process = psutil.Process()
end_memory = measure_memory_usage()
memory_usage_diff = end_memory - start_memory
print(f"Function took {execution_time:.2f} seconds to execute")
print(f"Memory usage difference: {memory_usage_diff:.2f} B")



start_time = time.time()
start_memory = measure_memory_usage()
def factorial1(n):
    if n == 0:
        return 1
    else:
        return n * factorial1(n-1)
factorial1(995)
end_time = time.time()
execution_time = end_time - start_time
process = psutil.Process()
end_memory = measure_memory_usage()
memory_usage_diff = end_memory - start_memory
print(f"Function took {execution_time:.2f} seconds to execute")
print(f"Memory usage difference: {memory_usage_diff:.2f} B")

