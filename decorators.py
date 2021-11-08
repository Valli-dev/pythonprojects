def announce(f):
    def wrapper():
        print("Function about to begin...")
        f()
        print("function execution done")
    return wrapper

@announce
def hello():
    print("Hello world")


hello()