class MyCustomError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)


try:
    raise MyCustomError("Custom error message")
except MyCustomError as custom_error:
    print("prsnth customer error--Zero division error",custom_error)
