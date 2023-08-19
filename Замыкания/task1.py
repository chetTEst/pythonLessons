def add(number):
    def inner():
        nonlocal number
        number += 1
        return number
    return inner

d = add(10)
print(d())
print(d())
print(d())

