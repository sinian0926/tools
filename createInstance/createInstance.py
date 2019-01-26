

if __name__ == '__main__':
	m = __import__('test',globals(),locals(),['My','Mye'])
	m1 = getattr(m,'My')
	m2 = getattr(m,'Mye')
	obj = m1('aaa')
	obj1 = m2(111)
	obj.test()
	obj1.test()