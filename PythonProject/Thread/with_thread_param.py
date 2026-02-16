import threading
from threading import *

def hello(name):
    for i in range(1,11):
        print("Hello:",name)

def hi(name):
    for i in range(1,11):
        print("Hi:",name)

t1 = threading.Thread(target=hello,args=("Kavya",))
t2 = threading.Thread(target=hi,args=("Niya",))

t1.start()
t2.start()
