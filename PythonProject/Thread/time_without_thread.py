import threading
import time

def task1():
    for i in range(3):
        print("Task one is running")
        time.sleep(1)

def task2():
    for i in range(3):
        print("Task two is running")
        time.sleep(1)

task1()
task2()
