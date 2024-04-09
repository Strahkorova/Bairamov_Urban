def is_prime(func):
    def wrapper(*args):
        if func(*args) == "true":
            print("Это простое число!")
        elif func(*args) == "false":
            print("Это сложное число!")
    return wrapper


@is_prime
def sum_three(a, b, c):
    k = a + b + c
    print(k)
    if k % 2 == 0:
        return "false"
    else:
        for i in range(3, k):
            if k % i == 0:
                return "false"
            break
        return "true"


result = sum_three(8, 3, 6)
print(result)
