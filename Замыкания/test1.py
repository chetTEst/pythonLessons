def next(number):
    def inner():
        n = number
        n += 1
        return n
    return inner

d = next(10)
print(d())
print(d())
print(d())

