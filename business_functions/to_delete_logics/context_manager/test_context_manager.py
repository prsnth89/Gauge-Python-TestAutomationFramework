class TestContextManager:
    def __enter__(self):
        print("Enter the context manager")
        return self
    
    def __exit__(self,excep_type,excep_value,traceback):
        print("Exit the context manager")

    
#using context manager
with TestContextManager() as cm:
    print("Inside context")


    