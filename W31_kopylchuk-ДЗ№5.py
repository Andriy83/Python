from random import randint
x1=(input('List1 lenght = '))
y1=(input('List1 value = '))
x1=int(x1)
y1=int(y1)
def func1(a1,b1):
  a1b1 = []
  for i in range(a1):
    a1b1.append(randint(0,b1))
  return a1b1
list1=func1(x1,y1)
x2=(input('List2 lenght = '))
y2=(input('List2 value = '))
x2=int(x2)
y2=int(y2)
def func2(a2,b2):
  a2b2 = []
  for i in range(a2):
    a2b2.append(randint(0,b2))
  return a2b2
list2=func2(x2,y2)
result=list(set(list1) & set(list2))
if result == []:
 print('No match', result)
elif result == result:
 print('Match', result)