import random
def choose(color, a, b):
    return {color: random.randint(a, b)}
c=str(input("Enter color = "))
print((choose(c, 0, 100)))