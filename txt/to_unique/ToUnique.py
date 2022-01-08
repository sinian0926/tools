#  文本去重
from collections import Counter

from base_tools.GetProjectPath import get_root_path


class deal_text():
    def to_unique(self, filepath, seq=None):
        """
        filepath: 要去重的文本文件路径
        seq: 分隔符;若为空，则默认为换行符（‘\n’）
        """
        with open(filepath, 'r') as f:
            old_list = list()
            res_dict = dict()
            if seq is None or seq == '':
                old_list = f.readlines()
                # print(len(old_list))
                # deal_list = [x.strip('\n') for x in old_list]
                # new_list = list(set(deal_list))
                # relist = self.find_repeat(deal_list)
                # return deal_list,relist
            else:
                text = ''
                for line in f.readlines():
                    text += line
                if text is not None or text != '':
                    old_list = text.split(seq)
                    # print(old_list)                    
                else:
                    return '文件为空，请重新选择文件！'

            # print('old_list{0},{1}'.format(old_list,len(old_list)))
            if old_list is not None and len(old_list) > 0:
                deal_list = [x.strip('\n') for x in old_list]
                new_list = list(set(deal_list))
                # print(len(new_list))
                relist = self.find_repeat(deal_list)
                res_dict['no_repeatText'] = new_list
                res_dict['repeatText'] = relist
                return res_dict
            else:
                res_dict['res'] = '文件内容为空，请重新选择文件！'
                return res_dict

    def find_repeat(self, relist):
        redict = Counter(relist)
        # print(redict)
        result_list = list()
        for k, v in redict.items():
            if v >= 2:
                result_list.append(k)
        return result_list


if __name__ == '__main__':
    PROJECT_NAME = r'base_tools'
    root_path = get_root_path(project_name=PROJECT_NAME)
    # 要更新的目录存放在下面这个文档中
    source_path = r'\exts\toUnique.txt'
    path = root_path + source_path

    fo = deal_text()
    # res_text = fo.to_unique(filepath,seq='\n');
    res_text = fo.to_unique(path);
    print(res_text)
