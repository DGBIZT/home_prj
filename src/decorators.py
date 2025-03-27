from functools import wraps
import os

def log(filename=""):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args , **kwargs)
                print(f"{func.__name__}: Результат {result}")
                if filename:
                    with open(os.path.abspath(f"{filename}"), 'a', encoding="utf-8") as f:
                        f.write(f"{func.__name__} ок \n")
                else:
                    print(f"{func.__name__} ок")
                return result
            except TypeError as e:
                if filename:
                    print(f"{func.__name__} as {e}")
                    with open(os.path.abspath(f"{filename}"), 'a', encoding="utf-8") as f:
                        f.write(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}  \n")
                else:
                    print(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise   TypeError(f"Введены не правильные данные в функции {func.__name__}")
        return wrapper
    return decorator


@log()
def my_function(x, y):
    """Сложение чисел"""
    return x + y

my_function(1.5, 2)
# print(my_function(1, 2))

