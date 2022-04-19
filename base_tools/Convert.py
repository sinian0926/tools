from base_tools.GetProjectPath import get_root_path


def to_camel(content):
    content = content.lower()
    result = ''
    flag = False
    length = len(content)

    for i in range(length):
        if '_'.__eq__(content[i]):
            flag = True
            continue

        if flag:
            if ord('z') >= ord(content[i]) >= ord('a'):
                result += chr(ord(content[i]) - 32)
            else:
                result += content[i]
        else:
            result += content[i]
        flag = False
    return result


def to_underline(content):
    result = ''
    for i, x in enumerate(content):
        if i > 0 and ord('Z') >= ord(x) >= ord('A'):
            result += '_' + chr(ord(x) + 32)
        else:
            result += x
    return result


if __name__ == '__main__':
    # paths=[r"D:\5VN-Documents\结算业务组”，r"D:\SVN-Documents\公共内容”，r"D:\5VN-Code\SCS\LXZZ"r"D:\SVWr"D:\SVW-Code\STS\LXZZ"]
    PROJECT_NAME = r'tools'
    root_path = get_root_path(project_name=PROJECT_NAME)
    # 要更新的目录存放在下面这个文档中
    source_path = r'\exts\convert.txt'
    path = root_path + source_path

    with open(path, 'r', encoding='utf8')as f:
        for line in f.readlines():
            line_strip = line.strip()

            # camel = to_camel(line_strip)
            # print(camel)

            underline = to_underline(line_strip)
            print(underline)