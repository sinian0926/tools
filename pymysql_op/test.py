import pymysql

db = pymysql.connect('localhost','root','root110','test')

cursor = db.cursor()

sql = '''
	insert into test_u values(2,'123',22);
	'''
try:
	
	cursor.execute(sql)

	db.commit()
except:
	db.rollback()

cursor.execute('select * from test_u')

##### 如果先执行了fetchone()方法，再执行fetchall()方法，会导致丢失数据，
#并不是真的丢失，而是读取时会少数据。
data = cursor.fetchone()

print(data)

data1 = cursor.fetchall() 

print(data1)

rowcount = cursor.rowcount

print(rowcount)

db.close()

# import numpy as np

# c = [[1,2],[3,4]]
# d=np.array(c)
# print(d.flatten())

# import matplotlib.pyplot as plt
# import numpy as np
# # %matplotlib inline

# x = np.linspace(0,10,100)

# '''
# 主题样式
# '''
# # plt.style.use("classic")



# # plt.plot(x,np.sin(x),'--')
# # plt.plot(x,np.cos(x),'o')



# y = np.random.rand(100)
# colors = np.random.rand(100)
# sizes = 1000 * np.random.rand(100)
# plt.scatter(x,y,c= colors,s=sizes,alpha=0.4)
# plt.colorbar()
# plt.show()


# import xlrd
 
# if __name__ == '__main__':
# 	file_path = r'C:\Users\Administrator\Desktop\123.xlsx'

# 	sheet = xlrd.open_workbook(file_path)
# 	data = sheet.sheet_by_name('111')
# 	s_str = str(data.cell(0,0)).replace('1','a')
# 	print(s_str)
# 	s_str = s_str.replace(r'\n','')
# 	print(s_str)
	
	