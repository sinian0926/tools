import os


# 如果目录名字为中文 需要转码处理
# uPath = unicode(cPath,'utf-8')
class OpFile:
    _result = list()

    def __init(self):
        self._result = list()

    def list_file2(self, path):
        # @parma path 推荐使用 u'd:\\'

        assert os.path.isdir(path)
        result = []
        for root, dirs, files in os.walk(path, topdown=True):
            for f in files:
                result.append(os.path.join(root, f))
        return result

    def list_file(self, path):
        # result = []
        if os.path.isfile(path):
            # print(path)
            self._result.append(path)
        elif os.path.isdir(path) is True:
            for p in os.listdir(path):
                self.list_file(path + '\\' + p)

    def is_empty_folder(self, path):
        if os.path.isdir(path):
            if not os.listdir(path):
                # 是空文件夹
                os.rmdir(path)
                isdel = os.path.exists(path)
                if isdel:
                    print('文件：%s，删除状态：%s 。' % (path, isdel))

            else:
                for p in os.listdir(path):
                    self.is_empty_folder(path + '\\' + p)


if __name__ == '__main__':
    path = u'D:\\'

    # 如果目录名字为中文 需要转码处理
    # path = unicode(path,'utf-8')

    f = OpFile()
    # s1 = datetime.datetime.now()
    # f.list_file(path)
    # s2 = datetime.datetime.now()
    # print('listfile耗时：{0},filenum is {1}'.format((s2 - s1),len(f._result)))
    # p2 = f.list_file2(path)
    # print('listfile2耗时：{0},filenum is {1}'.format((datetime.datetime.now()-s2),len(p2)))
    f.is_empty_folder(path)
