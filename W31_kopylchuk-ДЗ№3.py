import random
a=random.randint(0, 10)
print('A =', a)
import random
b=random.randint(0, 10)
print('Б =', b)
import random
c=random.randint(0, 10)
print('В =', c)
if a>b:
  print('Свет')
elif a<b:
  print('Тьма')
elif a==b:
  print('Теперь эта!', c)
  if a+b>c:
    print('Хорошо')
  elif a+b<c :
    print('Плохо')
  elif a+b == c:
    print('Страдания')