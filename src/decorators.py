from datetime import datetime
from functools import wraps
from typing import Any


def log(filename: str | None = None) -> Any:
    """ функция-декоратор автоматически выводит в консоль начало и конец выполнения функции,
    результат выполнения и возникшие ошибки """
    def decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                start_time = (datetime.now()).strftime("%H:%M:%S")
                result = func(*args, **kwargs)
                log_result = (f"{func.__name__} result: {result}, start time: {start_time}, "
                              f"arguments: {args}, {kwargs}")
                if filename:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(log_result)
                    print(f"{func.__name__} ok")
                else:
                    print(f"{log_result}")
                return result
            except Exception as e:
                log_result = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(log_result)
                    print(log_result)
                else:
                    print(log_result)
        return wrapper
    return decorator
