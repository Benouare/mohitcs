import threading 
import time
list1 = []

lock = threading.Lock()

class MyThread(threading.Thread):
	def __init__(self,i):
		threading.Thread.__init__(self)
		self.h = i
		
	def run(self):
		
		time.sleep(3)
		lock.acquire()
		
		list1.append(self.h)
		print ("Value added ", self.h)
		lock.release()
		
		
	
thread1 = MyThread(10)
thread1.start()



thread2 = MyThread(20)
thread2.start()

thread1.join()
thread2.join()

print ("All work done",list1)