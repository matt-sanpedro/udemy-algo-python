import functools

# BONUS: refactor the code to take in the user as an argument to the decorator

# simple decorators allow the modification of functions or methods
user = {"username": "john", "access_level": "guest"}

# make_secure is now a factory function that takes an argument and returns a decorator
def make_secure(access_level):
    # decorator takes a function as an argument
    def decorator(func):
        # secure_function is a wrapper for func
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}"
            
        return secure_function
    return decorator

@make_secure("admin")
def get_admin_password():
    return "admin: 1234"

@make_secure("user")
def get_dashboard_password():
    return "user: user_password"

print(get_admin_password())
print(get_dashboard_password())

user = {"username": "anna", "access_level": "admin"}

print(get_admin_password())
print(get_dashboard_password())
