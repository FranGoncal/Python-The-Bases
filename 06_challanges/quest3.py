'''
Implement a simple Singleton in Python.

Imagine you have a printer in your office. 
No matter how many people try to use it, theres only one printer for everyone. 
If someone tries to create a new printer, they should get the same one that already exists.
'''
from Queue import Queue, Node
import time
import sys
import threading


class Printer:

    queue = Queue()
    n_connection = 0

    def __init__(self):
        Printer.n_connection += 1

    def add_printer_queue(self, value):
        Printer.queue.enqueue(value)

    def print(self):
        while(not Printer.queue.isEmpty()):
            Printer._printing()

    def _animation():
        for i in range(5):
            
            print(f"Loading... {i*20}%")
            sys.stdout.write("\033[F\033[K")
            time.sleep(1)

    def _printing():
        Printer._animation()
        item =  Printer.queue.peek().value
        Printer.queue.dequeue()
        print(str(item))


printer1 = Printer()
printer2 = Printer()
printer3 = Printer()


printer1.add_printer_queue("Olá1")

printer3.add_printer_queue("Olá2")

printer2.add_printer_queue("Olá3")


thread1 = threading.Thread(target=printer2.print)
thread1.start()

printer4 = Printer()
printer3.add_printer_queue("upa!")