import xlrd
import re
# import asyncio
##  特别加的
# import sys
# sys.setrecursionlimit(1000000) ### 这是一百万




# def excel_config():
#     with open(r'cfg.txt') as f:
#         for line in f.readlines():
#             path = 


def read_excel(filepath,sheetname,x1,y1,x,y):
    '''
    filepath: 要打开表格文件的路径名
    sheetname：工作簿的名字
    x1：起始X坐标
    y1：起始Y坐标
    x：X轴偏移量
    y：Y轴偏移量
    '''

    # 打开excel文件
    file = xlrd.open_workbook(filepath)

    # 根据sheetname 打开工作簿
    data = file.sheet_by_name(sheetname)

    # 索引从0开始，所以要减 1
    y1 = y1 - 1

    # 开始读取表格数据
    for i in range(y1,y1+y):
        # print(i)
        # 获取 calcode 值
        calcode = str(data.cell(i,0)).replace("text:'","").replace("'","").replace("empty:'","")

        # 获取 SQL描述 值
        desc = str(data.cell(i,1)).replace("text:'","").replace("'","").replace("empty:'","")

        # 获取 SQL语句，并做简单处理，以' '进行分割
        vals = str(data.cell(i,2)).replace('\\n','').replace('text:"',"").replace('"',"").replace("'","''").replace("empty:''''","").split()
        
        # 开始拼接SQL语句
        s1,s2 = str_group(vals)
        
        # ### 如果SQL长度小于4000。
        s1 = delete_space(s1)
        s2 = delete_space(s2)

        # print('------------------------'+calcode+'---------------------------')
        # print(s1)
        # print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
        # print(s2)
        # print('---------------------------------------------------')
        
        # 选择最终的SQL插入语句的拼接SQL
        if ''.__eq__(s2) or s2 == None:
            str_sql = "insert into lmcalmode (CALCODE, RISKCODE, TYPE, CALSQL, REMARK, CALSQL1)values ('"+\
            str(calcode)+"','', '0', '"+str(s1)+"', '"+str(desc)+"', '');"
        else:
            str_sql = "insert into lmcalmode (CALCODE, RISKCODE, TYPE, CALSQL, REMARK, CALSQL1)values ('"+\
            str(calcode)+"','', '0', '"+str(s1)+"', '"+str(desc)+"', ' "+str(s2)+"');"

        
        # print('----------------------{}--'.format(len(s1))+calcode+'++{}---------------------------'.format(len(s2)))
        print(str_sql)
        # print('---------------------------------------------------')
        


def str_group(vals):
    '''
    拼接已经分割后的SQL语句
    '''
    s1 = ''
    s2 = ''
    for val in vals:        
        # print(val)
        if len(s1) <4000:
            s1 += val + ' '
        else:
            s2 += val + ' '
    return s1.strip(),s2.strip()




def delete_space(s_str):
    '''
    s_str:欲删除空格的字符串
    '''
    ss = ''
    # 判断一下长度是否大于4000，是则删除空格，否则返回原值
    if len(s_str) > 4000:
        ss = s_str.replace(' (','(').replace('( ','(').replace(' )',')').replace(') ',')').replace(', ',',').replace(' =','=').replace('= ','=').replace(' ||','||').replace('|| ','||').replace(' >','>').replace('> ','>').replace(' <','<').replace('< ','<').replace(' >=','>=').replace('>= ','>=').replace('<= ','<=').replace(' <=','<=').replace('  ',' ')
    else:
        return s_str

    # 判断删除空格后长度是否小于4000，是则返回字符串，否则递归执行该函数
    if len(ss) < 4000:
        return ss
    else:
        delete_space(ss)


# 主函数入口
if __name__ == '__main__':
    filepath = r'D:\ql\20180704整理\保单登记\1修改记录\PAYSTATUSCODE.xlsx'
    
    # 开始读取表格
    read_excel(filepath,'paystatuscodeTX',x1=0,y1=1,x=10,y=2)