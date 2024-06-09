import time
import psutil
import os
import inspect
from radon.complexity import cc_visit

def analyze_complexity(func):
    """
    Analyze the Cyclomatic Complexity of the given function.
    """
    source_code = inspect.getsource(func)
    complexities = cc_visit(source_code)
    return complexities[0].complexity if complexities else 0

def time_memory_cpu_complexity_decorator(func):
    def wrapper(*args, **kwargs):
        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss
        initial_cpu_times = process.cpu_times()
        start_time = time.time()
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        final_memory = process.memory_info().rss
        final_cpu_times = process.cpu_times()
        time_taken = end_time - start_time
        memory_used = final_memory - initial_memory
        cpu_time_used = sum(final_cpu_times) - sum(initial_cpu_times)
        cpu_usage_percentage = (cpu_time_used / time_taken) * 100 / psutil.cpu_count()
        complexity = analyze_complexity(func)

        print(f"\033[1;34;40m Time taken  : \033[1;35;40m {time_taken:.4f} seconds")
        print(f"\033[1;34;40m Memory used : \033[1;35;40m {memory_used / (1024 * 1024):.4f} MB")
        print(f"\033[1;34;40m CPU usage   : \033[1;35;40m {cpu_usage_percentage:.2f} %")
        print(f"\033[1;34;40m Complexity  : \033[1;35;40m {complexity}\n")

        return result
    return wrapper
