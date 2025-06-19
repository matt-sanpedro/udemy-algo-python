import functools

# simple decorators allow the modification of functions or methods
user = {"username": "john", "access_level": "admin"}

# make_secure is a decorator that takes a function as an argument
def make_secure(func):
    # secure_function is a wrapper for func
    print(f"Decorating function [make_secure]: {func.__name__}")
    # print(f"Decorating function: {func.__code__.co_name}")
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        print(f"Decorating function [secure_function]: {func.__name__}")
        # print(f"Decorating function: {func}")
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}"
        
    return secure_function

@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"

# get password is replaced by secure_function
# print(get_password.__name__)
print(get_password("admin"))
print(get_password("billing"))
