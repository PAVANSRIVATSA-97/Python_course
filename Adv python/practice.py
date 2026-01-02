def logger(say_hello):
    def wrapper():
        print("The function is being called before the decorator")
        say_hello()
    return wrapper
@logger
def say_hello():
    print("Hello, World!")
say_hello()


    