def decorator_func(func):
    def wrapper():
        print("Decorator Applied")
        return func()
    return wrapper

def apply_decorator(func):
    return decorator_func(func)

def say_hello():
    print("Hello!")

decorated_func = apply_decorator(say_hello)
decorated_func()