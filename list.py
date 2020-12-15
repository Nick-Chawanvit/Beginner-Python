>>> garage = ['toyota'.'honda','izusu']
SyntaxError: invalid syntax
>>> garage = ['toyota','honda','izusu']
>>> garage.append('suzuki')
>>> print(garage)
['toyota', 'honda', 'izusu', 'suzuki']
>>> print(2)
2
>>> print(garage[2])
izusu
>>> garage.remove('honda')
>>> print(garage)
['toyota', 'izusu', 'suzuki']
>>> garage.insert(1,benz)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    garage.insert(1,benz)
NameError: name 'benz' is not defined
>>> garage.insert(1,'benz')
>>> 
>>> print(garage)
['toyota', 'benz', 'izusu', 'suzuki']
>>> del garage[2]
>>> print(garage)
['toyota', 'benz', 'suzuki']
>>> mycar = garage.pop(-1)
>>> print(mycar)
suzuki
>>> print(garage)
['toyota', 'benz']
>>> garage.append('honda')
>>> print(garage)
['toyota', 'benz', 'honda']
>>> garage[1] = 'tesla'
>>> print(garage)
['toyota', 'tesla', 'honda']
>>> print(len(garage))
3
users = ['z','a','t','v','n','c']
>>> users.sort()
>>> print(users)
['a', 'c', 'n', 't', 'v', 'z']
>>> users.sort(reverse=True)
>>> users
['z', 'v', 't', 'n', 'c', 'a']
>>> print(sorted(users))
['a', 'c', 'n', 't', 'v', 'z']
>>> print(users)
['z', 'v', 't', 'n', 'c', 'a']
>>> users = ['z','a','t','v','n','c']
>>> users.reverse()
>>> print(users)
['c', 'n', 'v', 't', 'a', 'z']
>>> for u in users:
	print(u)

	
c
n
v
t
a
z
>>> for u in sorted(users):
	print(u)

	
a
c
n
t
v
z
>>> for u in users.reverse():
	print(u)

	
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    for u in users.reverse():
TypeError: 'NoneType' object is not iterable
>>> users.reverse()
>>> for u in users:
	print(u)

	
c
n
v
t
a
z
>>> for u in users:
	print('สวัสดี',u)
	print('สวัสดี'+u)

	
สวัสดี c
สวัสดีc
สวัสดี n
สวัสดีn
สวัสดี v
สวัสดีv
สวัสดี t
สวัสดีt
สวัสดี a
สวัสดีa
สวัสดี z
สวัสดีz
>>> 
