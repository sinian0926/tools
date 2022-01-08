import hashlib
import os


class OpFile:
    def __init__(self):
        self._result = list()

    def list_file(self, path):
        n = dict()
        f = dict()
        n['file_list'] = list()
        if os.path.isfile(path) is True:
            f_MD5 = self.get_file_md5(path)
            n['md5'] = f_MD5
            f['name'] = path
            fsize = str(os.path.getsize(path) / 1024 / 1024) + 'MB' if os.path.getsize(path) / 1024 / 1024 > 0 else str(
                os.path.getsize(path) / 1024) + 'KB'
            f['size'] = str(fsize)
            n['file_list'].append(f)
            # print(path)
            # print(n)
            if len(self._result) == 0:
                self._result.append(n)
            else:
                for m in self._result:
                    # print(len(self._result))
                    if f_MD5.__eq__(m['md5']) is True and path not in m['file_list']:
                        m['file_list'].append(path)
                self._result.append(n)

        elif os.path.isdir(path) is True:
            for p in os.listdir(path):
                try:
                    self.list_file(path + '\\' + p)
                except Exception as e:
                    print({'error': repr(e),
                           'path': path + '\\' + p})
                    continue

    def list_file2(self, path):
        '''
        @parma path 推荐使用 u'd:\\'
        '''
        assert os.path.isdir(path)
        result = []
        for root, dirs, files in os.walk(path, topdown=True):
            for f in files:
                result.append(os.path.join(root, f))
        return result

    def get_file_md5(self, filename):
        if os.path.isfile(filename):
            myhash = hashlib.md5()
            f = open(filename, 'rb')
            while True:
                b = f.read(8096)
                if not b:
                    break
                myhash.update(b)
        hashcode = myhash.hexdigest()
        f.close()
        md5 = str(hashcode).lower()
        return md5

    @property
    def result(self):
        return self._result


if __name__ == '__main__':
    filepath = r'D:\整理'
    of = OpFile()
    of.list_file(filepath)
    # print(of._result)
    repeat_flist = list()
    for l in of.result:
        if len(l['file_list']) > 1:
            repeat_flist.append(l)
    print(repeat_flist)
    # print(of.list_file2(filepath))
