import numpy as np

#1a
a = np.zeros(10)
a[4] = 1
print(a)

#1b
b = np.arange(10,50)
print(b)

#1c
b = np.flip(b)
print(b)

#1d
d =  np.arange(0, 9).reshape(3,3)
print(d)

#1e
e = np.array([1,2,0,0,4,0])
print(np.nonzero(e)[0])

#1f
f = np.random.random(30)
print('Mean is: '+str(np.mean(f)))

#1g
g = np.ones((3,3),dtype=int)
g[1,1] = 0
print(g)

#1h
h = np.zeros((8,8),dtype=int)
h[1::2,::2] = 1
h[::2,1::2] = 1
print(h)

#1i
i = np.array([[1, 0], [0, 1]])
i = np.tile(i, (4,4))
print(i)

#1j
Z = np.arange(11)
Z[(Z > 3) & (Z < 8)] *= -1
print(Z)

#1k
Z = np.random.random(10)
Z = np.sort(Z)
print(Z)

#1l
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.array_equal(A, B)
print(equal)

#1m
Z = np.arange(10, dtype=np.int32)
print(Z.dtype)
Z = Z.astype('float32') 
print(Z.dtype)

#1n
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
print(C)
D = np.diag(C)
print(D)


#3a
class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

#3b
class Student(Person):
    def __init__(self, firstname, lastname, subject):
        Person.__init__(self, firstname, lastname)
        self.subject = subject
    def printNameSubject(self):
        print(self.firstname, self.lastname, self.subject)

#3c
me = Student('Benedikt', 'Daurer', 'physics') 
me.printNameSubject() 

#3d       
class Teacher(Person):
    def __init__(self, first, last, course):
        Person.__init__(self, first, last)
        self.course = course
    def printNameCourse(self):
        print(self.firstname, self.lastname, self.course)

me = Teacher('Filipe', 'Maia', 'Python programming') 
me.printNameCourse() 
