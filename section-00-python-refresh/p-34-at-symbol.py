import functools

# simple decorators allow the modification of functions or methods
user = {"username": "john", "access_level": "admin"}

# make_secure is a decorator that takes a function as an argument
def make_secure(func):
    # secure_function is a wrapper for func, also keeps doc for func if any
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}"
        
    return secure_function

# the @ symbol is a decorator syntax that applies make_secure to get_admin_password
@make_secure
def get_admin_password():
    return "1234"

print(get_admin_password())
print(get_admin_password.__name__) # secure_function -> if @functools.wraps(func) is not used
