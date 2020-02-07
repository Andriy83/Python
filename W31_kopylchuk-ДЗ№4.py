from random import randint
x=(input('List lenght = '))
y=(input('List value = '))
x=int(x)
y=int(y)
def func(a,b):
  ab = []
  for i in range(a):
    ab.append(randint(0,b))
  return ab
list=func(x,y)
print(list)
