import time

def plus(a, b):
    return f'PLUS Total: {a + b}'


def minus(a, b):
    return f'MINUS Total: {a - b}'


def multi(a, b):
    return f'MULTI Total: {a * b}'


def divide(a, b):
    return f'DIVIDE total: {round(a / b, 2)}'


def exp(a, b):
    return f'EXP Total: {a ** b}'


def r_of_dev(a, b):
    return f'Total: {a % b}'


def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("====Time taken====:", end_time - start_time, "seconds")
        return result
    return wrapper