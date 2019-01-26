import os
import hashlib
import datetime 

class op_file:
    def __init__(self):
        self._result = list()
        

    def list_file(self,path):
        n = dict()
        n['file_list'] = list()     
        if os.path.isfile(path) == True:
            f_MD5 = self.get_file_md5(path)
            n['md5'] = f_MD5
            n['file_list'].append(path)
            # print(n)
            if len(self._result) == 0:
                self._result.append(n)
            else:
                for m in self._result:
                    # print(len(self._result))
                    if f_MD5.__eq__(m['md5']) == True and path not in m['file_list']:
                        m['file_list'].append(path)
                self._result.append(n)



        elif os.path.isdir(path) == True:
            for p in os.listdir(path):
                self.list_file(path + '\\' + p)

            
    def list_file2(self,path):
        '''
        @parma path 推荐使用 u'd:\\'
        '''
        assert os.path.isdir(path)
        result = []
        for root,dirs,files in os.walk(path,topdown=True):
            for f in files:
                result.append(os.path.join(root,f))
        return result







    def get_file_md5(self,filename):
        if os.path.isfile(filename):
            myhash = hashlib.md5()
            f = open(filename,'rb')
            while True:
                b = f.read(8096)
                if not b:
                    break
                myhash.update(b)
        hashcode = myhash.hexdigest()    
        f.close()
        md5 = str(hashcode).lower()
        return md5




if __name__ == '__main__':
    filepath = r'C:\Users\sy\Desktop\test'
    of = op_file()
    of.list_file(filepath)   
    #print(of._result)
    for l in of._result:
        if len(l['file_list']) > 1:
            print(l)
    # print(of.list_file2(filepath))