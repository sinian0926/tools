import os

from base_tools.GetProjectPath import get_root_path


def auto_update_svn(txt_path):
    with open(txt_path, 'r', encoding='utf8')as f:
        for line in f.readlines():
            # print(line)
            pro_line = line.strip()

            # 过滤以井号(#)开头的
            if '#'.__eq__(pro_line[0]):
                continue

            # print(pro line)
            print('更新-', pro_line)
            os.chdir(pro_line)
            system = os.system('svn update')
            if system != 0:
                os.system("svn clean up")
                os_system = os.system('svn update')
                if os_system != 0:
                    raise Exception('SVN update faild! SVN更新失败！')


if __name__ == '__main__':
    # paths=[r"D:\5VN-Documents\结算业务组”，r"D:\SVN-Documents\公共内容”，r"D:\5VN-Code\SCS\LXZZ"r"D:\SVWr"D:\SVW-Code\STS\LXZZ"]
    PROJECT_NAME = r'tools'
    root_path = get_root_path(project_name=PROJECT_NAME)
    # 要更新的目录存放在下面这个文档中
    source_path = r'\exts\autoUpSVN.txt'
    path = root_path + source_path
    auto_update_svn(path)
