from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"Calling {func.__name__} with args - {args} and kwargs = {kwargs}")
        result = func(*args,**kwargs)
        print(f"Finisheed {func.__name__}")
        return result
    return wrapper

@log_activity
def brew_chai(type):
    print(f"Brewing {type} chai")


brew_chai("masala chai")