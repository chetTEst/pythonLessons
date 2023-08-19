def outer(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Функция {func.__name__} запускалась {count} раз")
        return func(*args, **kwargs)
    return inner


def smm(a, b):
    return a+b


smm = outer(smm)

print(smm(4,6))
print(smm(14,16))
print(smm(24,36))