def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, 'Solo puedes repetir cadenas'
        return string * n
    return repeater


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5('Hola'))
    division_by_3 = make_division_by(3)
    print(division_by_3(18))  # 6.0
    division_by_5 = make_division_by(5)
    print(division_by_5(100))  # 20.0


def make_division_by(n):
    return lambda x: x/n

# def make_multiplier(x):
# def multiplier(n):
# return x * n
# return multiplier
# times10 = make_multiplier (10)
# times4 = make_multiplier (4)
# print(times10(3))
# print(times4(5))
# print(times10(times4(2)))


if __name__ == '__main__':
    run()
