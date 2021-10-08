#We created a sub-class of the thread class.
#Then we override the __init__ function of the thread class.
#Then we override the run method to define the behavior of the thread.
#The start() method starts a Python thread.

# import the threading module
import threading

class thread(threading.Thread):
	def __init__(self, thread_name, thread_ID):
		threading.Thread.__init__(self)
		self.thread_name = thread_name
		self.thread_ID = thread_ID

		# helper function to execute the threads
	def run(self):
		print(str(self.thread_name) +" "+ str(self.thread_ID))

thread1 = thread("hi", 1)
thread2 = thread("hello", 2)

thread1.start()
thread2.start()

print("Exit")
