import functools
import logging

def log(filename=None):
    def decorator(func):
        if filename:
            logging.basicConfig(filename=filename, level=logging.INFO)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    logging.info(f"Function {func.__name__} executed with args: {args}, kwargs: {kwargs} and returned: {result}")
                else:
                    print(f"Function {func.__name__} executed with args: {args}, kwargs: {kwargs} and returned: {result}")
                return result
            except Exception as e:
                if filename:
                    logging.error(f"Function {func.__name__} failed with args: {args}, kwargs: {kwargs}. Error: {e}")
                else:
                    print(f"Function {func.__name__} failed with args: {args}, kwargs: {kwargs}. Error: {e}")

        return wrapper
    return decorator
