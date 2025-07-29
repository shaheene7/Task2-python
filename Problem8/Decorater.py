def handle_request():
    print("Processing request")


def with_auth(handler):
    def wrapper():
        print("Validating auth")
        handler()
    return wrapper

def with_limit_rate(handler):
    def wrapper():
        print("Checking rate limits")
        handler()
    return wrapper

def with_logging(handler):
    def wrapper():
        print("Logging request")
        handler()
    return wrapper

decorated = with_auth(with_limit_rate(with_logging(handle_request)))
decorated()


"""it enables adding or modifying behaviors of a function dynamically without changing its original code
    By wrapping the handler with multiple decorators"""