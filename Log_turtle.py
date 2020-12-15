Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle.Turtle()
>>> tao.shape('dog')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    tao.shape('dog')
  File "C:\Python\Python39\lib\turtle.py", line 2777, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named dog
>>> tao.shape('turtle')
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.lef(90)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    tao.lef(90)
AttributeError: 'Turtle' object has no attribute 'lef'
>>> tao.left(90)
>>> tao.clear()
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.clear()
>>> for i in range (4):
	tao.forward(100)
	tao.left(90)

	
>>> range(4)
range(0, 4)
>>> list(range(4))
[0, 1, 2, 3]
>>> for i in range(5)
SyntaxError: invalid syntax
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> for i in [10,50,90]:
	print(i)

	
10
50
90
>>> tao.clear()
>>> for i in range (4):
	tao.forward(100)
	tao.left(90)
	print('No.',i)

	
No. 0
No. 1
No. 2
No. 3
>>> for i in range(9):
	tao.forward(100)
	tao.left(45)
	print('No.',i)

	
No. 0
No. 1
No. 2
No. 3
No. 4
No. 5
No. 6
No. 7
No. 8
>>> tao.clear()
>>> for i in range(9):
	tao.forward(100)
	tao.left(45)
	print('No.',i)

	
No. 0
No. 1
No. 2
No. 3
No. 4
No. 5
No. 6
No. 7
No. 8
>>> tao.reset()
>>> for i in range(8):
	tao.forward(100)
	tao.left(45)
	print('No.',i)

	
No. 0
No. 1
No. 2
No. 3
No. 4
No. 5
No. 6
No. 7
>>> for i in range(6):
	tao.forward(100)
	tao.left(45)
	print('No.',i)

	
No. 0
No. 1
No. 2
No. 3
No. 4
No. 5
>>> tao.reset()
>>> for i in range(8):
	tao.forward(100)
	tao.left(45)
	print('No.',i)

	
No. 0
No. 1
No. 2
No. 3
No. 4
No. 5
No. 6
No. 7
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print('8เหลี่ยมรูปที่',i)

	
8เหลี่ยมรูปที่ 0
8เหลี่ยมรูปที่ 1
8เหลี่ยมรูปที่ 2
8เหลี่ยมรูปที่ 3
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print('8เหลี่ยมรูปที่',i)
	tao.left(90)

	
8เหลี่ยมรูปที่ 0
8เหลี่ยมรูปที่ 1
8เหลี่ยมรูปที่ 2
8เหลี่ยมรูปที่ 3
>>> tao.reset()
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print('8เหลี่ยมรูปที่',i)
	tao.left(180)

	
8เหลี่ยมรูปที่ 0
8เหลี่ยมรูปที่ 1
8เหลี่ยมรูปที่ 2
8เหลี่ยมรูปที่ 3
>>> tao.reset()
>>> for i in range(4):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print('8เหลี่ยมรูปที่',i)
	tao.left(135)

	
8เหลี่ยมรูปที่ 0
8เหลี่ยมรูปที่ 1
8เหลี่ยมรูปที่ 2
8เหลี่ยมรูปที่ 3
>>> tao.reset()
>>> for i in range(10):
	for j in range(8):
		tao.forward(100)
		tao.left(45)
	print('8เหลี่ยมรูปที่',i)
	tao.left(36)

	
8เหลี่ยมรูปที่ 0
8เหลี่ยมรูปที่ 1
8เหลี่ยมรูปที่ 2
8เหลี่ยมรูปที่ 3
8เหลี่ยมรูปที่ 4
8เหลี่ยมรูปที่ 5
8เหลี่ยมรูปที่ 6
8เหลี่ยมรูปที่ 7
8เหลี่ยมรูปที่ 8
8เหลี่ยมรูปที่ 9
>>> tao.reset()
>>> def regtangle():
	for i in range(4):
		tao.forward(100)
		tao.left(90)

		
\
>>> 
>>> 
>>> def regtangle():
	for i in range(4):
		tao.forward(100)
		tao.left(90)

		
>>> rectangle()
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    rectangle()
NameError: name 'rectangle' is not defined
>>> reregtangle()
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    reregtangle()
NameError: name 'reregtangle' is not defined
>>> regtangle()
>>> for i in range(10):
	rectangle()
	tao.left(36)

	
Traceback (most recent call last):
  File "<pyshell#91>", line 2, in <module>
    rectangle()
NameError: name 'rectangle' is not defined
>>> for i in range(10):
	regtangle()
	tao.left(36)

	
>>> tao.size(50)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    tao.size(50)
AttributeError: 'Turtle' object has no attribute 'size'
>>> 