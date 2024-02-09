class UnauthorizedError(Exception):
    pass

def authorize(username, password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            
            predefined_username = "admin"
            predefined_password = "password123"

          
            if username == predefined_username and password == predefined_password:
               
                return func(*args, **kwargs)
            else:
                
                raise UnauthorizedError("Unauthorized access: Invalid username or password")

        return wrapper

    return decorator


@authorize(username="admin", password="password123")
def sensitive_operation():
    return "Sensitive information"

try:
   
    print(sensitive_operation())  
except UnauthorizedError as e:
    print(e)

try:
   
    @authorize(username="user", password="wrongpassword")
    def another_sensitive_operation():
        return "Another sensitive information"

    another_sensitive_operation() 
except UnauthorizedError as e:
    print(e)
