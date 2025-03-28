import os
from datetime import datetime
from functools import wraps


def log(filename=""):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                time_start = datetime.now()
                formatted_time = time_start.strftime("%Y-%m-%d %H:%M:%S")
                result = func(*args, **kwargs)
                end_time = datetime.now()
                formatted_time_end = end_time.strftime("%Y-%m-%d %H:%M:%S")

                # print(f"{func.__name__}: Результат {result}")
                if filename:
                    with open(os.path.abspath(f"{filename}"), "a", encoding="utf-8") as f:
                        f.write(
                            f"\n[{formatted_time}] {func.__name__} started with inputs: {args}, {kwargs}\n"
                            f"[{formatted_time_end}] {func.__name__} finished successfully with result: {result}"
                        )
                else:
                    print(
                        f"\n[{formatted_time}] {func.__name__} started with inputs: {args}, {kwargs}\n"
                        f"[{formatted_time_end}] {func.__name__} finished successfully with result: {result}"
                    )
                return result

            except TypeError as e:
                time_start_error = datetime.now()
                formatted_time_error_start = time_start_error.strftime("%Y-%m-%d %H:%M:%S")
                time_end_error = datetime.now()
                formatted_time_error_end = time_end_error.strftime("%Y-%m-%d %H:%M:%S")
                if filename:
                    print(f"{func.__name__} as {e}")
                    with open(os.path.abspath(f"{filename}"), "a", encoding="utf-8") as f:
                        f.write(
                            f"\n [{formatted_time_error_start}] {func.__name__} started with inputs: "
                            f"{args}, {kwargs}"
                            f"\n [{formatted_time_error_end}] {func.__name__}"
                            f"error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                        )
                else:
                    print(
                        f" \n [{formatted_time_error_start}] {func.__name__} started with inputs:"
                        f"{args}, {kwargs}\n [{formatted_time_error_end}] {func.__name__}"
                        f"error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                    )
                raise TypeError(f"Введены не правильные данные в функции {func.__name__}")

        return wrapper

    return decorator


@log()
def my_function(x, y):
    """Сложение чисел"""
    return x + y


my_function(1, 2)
# print(my_function(1, 2))
