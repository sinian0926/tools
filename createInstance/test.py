# import datetime
# import re

# def timestamp_to_utc(t):
# 	'''
# 	时间戳转UTC时间,例：1533207600583
# 	'''
# 	tt = str(t)
# 	if len(tt) > 10 :
# 		t = t / 1000
# 	ta = datetime.datetime.utcfromtimestamp(t)
# 	oos = ta.strftime("%Y-%m-%d %H:%M:%S")
# 	return oos
# import numpy as np
# if __name__ == '__main__':
# 	print(timestamp_to_utc(1540728010270))
# 	help(np)

# class My():
# 	def __init__(self,name):
# 		self.name = name



# 	def test(self):
# 		print('我是%s测试类'%self.name)

# class Mye():
# 	def __init__(self,age):
# 		self.age = age

# 	def test(self):
# 		print('我今年%s岁了'%self.age)

# import numpy as np 


# a = np.ceil(np.random.rand(10,8)*10)
# b = np.ceil(np.random.rand(10,8)*10)
# #print(np.concatenate((a,b),axis=0))
# print(a)
# print(a[np.newaxis,:].shape)


# import threading
# import asyncio
# import datetime
# import time
# # from aiohttp import ClientSession

# async def work():

# 	# for x in range(10):
# 	asyncio.sleep(1)

# 	for x in range(10):
# 		print('加班使我快乐！%s-----%s' % (x,datetime.datetime.now()))

# def run():
# 	for i in range(5):
# 		loop.run_until_complete(work())

# loop = asyncio.get_event_loop()
# if __name__ == '__main__':
# 	run()


# if __name__ == '__main__':

# 	t1 = threading.Thread(target = work )	
# 	t1.start()
# 	t1.join()
# 	print('Are you ready?')