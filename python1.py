import numpy as np
import numpy.random

print(np.array([5,75,90]))
my_list = ["denizli","zeliha","tolunay",15,True,98.65]
print((f"listenin ilk tipi = {type(my_list)}"))

my_arr = np.array(my_list)
print(f"listenin son tipi = {type(my_arr)}")
print(my_list)
print("*"*50)
print(my_arr)
my_arr2= np.array([56,785,99,86,],dtype=int)
print(my_arr2)
print(type(my_arr2))

print(numpy.random.rand(5,3))
print(type(my_arr2))
print("*"*50)

print(numpy.random.uniform(-5,10,(5,3)))
print("*"*50)
# 4 satır 4 sutun 10 ve 100 arasında ki degerlerin yazınız.
print(numpy.random.randint(10,100,(4,4)))
print("*"*50)
my_arr4= numpy.random.randint(1,100,(5,3))

print(numpy.random.randint(1,20,(2,2)))
print(my_arr4)
print(my_arr2)
#print(my_arr2 * my_arr4)

my_arr5 = numpy.random.randint(1,20,(2,2))
my_arr6 = numpy.random.randint(1,20,(2,2))

my_arr5 = my_arr5*3
my_arr6=my_arr6*3
print("-"*50)
print(my_arr5)
print(my_arr6)
print(my_arr5 - my_arr6)

