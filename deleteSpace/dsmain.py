import delete_SQLspace as ds
import re


# 主函数入口
if __name__ == '__main__':
    filepath = r'C:\Users\sy\Desktop\保单登记改造\RDI提数sql-1010fp.xlsx'
    
    # 开始读取表格
    ds.read_excel(filepath,'GX',x1=0,y1=2,x=10,y=169)
    # ds.excel_config()
