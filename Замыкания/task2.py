def add():
    number = 1
    def inner(number):
        number += 1
        return number
    return inner

d = add()
print(d(1))
print(d(2))
print(d(10))

