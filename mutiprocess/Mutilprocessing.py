import time
from multiprocessing.dummy import Pool as ThreadPool

import requests as req


def test(a):
    data = req.get(a)

    if data.status_code == 200:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    p = ThreadPool(4)
    # print([x for x in range(100)])

    l = list()
    p.map(test, ['https://www.baidu.com', 'https://www.qq.com', 'https://www.sina.com', 'https://www.163.com',
                 'https://www.126.com', 'https://www.hao123.com'])
    p.close()
    s = time.time()
    p.join()
    print('耗时：%s' % (time.time() - s))
