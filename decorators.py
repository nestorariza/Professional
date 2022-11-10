from datetime import datetime


def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura


@mayusculas
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'
    print(mensaje('Cesar'))


def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Pasaron {time_elapsed.total_seconds()} segundos')
    return wrapper


@execution_time
def random_func():
    print(mensaje('leonel'))
    for _ in range(1, 10000000):
        pass


random_func()


def with_custom_message(message):
    def with_message(function):
        print(f"{message}: ")

        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
        return wrapper
    return with_message


@with_custom_message("Hello")
def multiply(a, b):
    c = a * b
    print(f"The result of {a} × {b} is {c}")


multiply(10, 2)
