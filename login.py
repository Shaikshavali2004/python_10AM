def login_req(func):
    def inner(name,status):
        if status==False:
            print("Please Login")

        else:
            return func(name,status)
        
    return inner