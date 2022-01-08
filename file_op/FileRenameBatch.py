import os

from base_tools.FileTools import OpFile


class FileRename(object):
    def rename_batch(self, path, file_name=None, file_type=None, sorted_key=None):
        if file_name is None:
            file_name = '新建文件'

        if file_type is None:
            file_type = '.txt'

        if os.path.isdir(path) is False:
            raise Exception('请输入正确的文件夹路径！')

        files = OpFile().list_file2(path)
        # files = [file for file in files if str(file).endswith('.mp4')]
        print(len(files), files)

        # 排序
        if sorted_key is not None:
            files.sort(key=sorted_key)
        else:
            files.sort()

        print(files)
        for i, n in enumerate(files):
            # print(path)
            si = '0' + str(i + 1) if i < 9 else str(i + 1)
            file_rename = path + '\\' + file_name + si + file_type
            if os.path.isfile(file_rename) is True:
                continue
            os.rename(n, file_rename)
            # os.unlink(n)

    def rename_file(self, path, file_name=None, file_type=None):
        if file_name is None:
            file_name = []

        if file_type is None:
            file_type = '.txt'

        if os.path.isdir(path) is False:
            raise Exception('请输入正确的文件夹路径！')

        files = OpFile().list_file2(path)
        if files is None:
            raise Exception('文件列表不能为空！！！')

        if len(files) != len(names):
            # print(len(files), len(names))
            # print(files)
            raise Exception('文件名个数与重命名文件个数不一致，无法全部重命名！')

        # 排序
        files.sort()

        print(files)
        for i, n in enumerate(files):
            # print(path)
            file_rename = path + '\\' + file_name[i] + file_type
            if os.path.isfile(file_rename) is True:
                continue
            os.rename(n, file_rename)
            print(n)
            print(file_name[i])
            print('------------------------------------------------------')


if __name__ == '__main__':
    path = r'F:\视频\电视剧\查良镛\侠客行'
    rename = FileRename()

    names = ['成龙历险记-第1集《黑手帮》', '成龙历险记-第2集《文物的神奇力量》', '成龙历险记-第3集《出色的牛战士》', '成龙历险记-第4集《隐身的小蛇》', '成龙历险记-第5集《小玉不见了》',
             '成龙历险记-第6集《龟背上的秘密》', '成龙历险记-第7集《龙叔的怒火》', '成龙历险记-第8集《小玉的玩具》', '成龙历险记-第9集《治病的密码》', '成龙历险记-第10集《老爹的生日》',
             '成龙历险记-第11集《小玉历险》', '成龙历险记-第12集《两位龙叔》', '成龙历险记-第13集《消灭恶龙》', '成龙历险记-第14集《强悍的对手》', '成龙历险记-第15集《龙小组》',
             '成龙历险记-第16集《复制小玉》', '成龙历险记-第17集《真假囚犯》', '成龙历险记-第18集《惊人表演》', '成龙历险记-第19集《女王》', '成龙历险记-第20集《失重的月亮》',
             '成龙历险记-第21集《上帝的盔甲》', '成龙历险记-第22集《送尾巴回家》', '成龙历险记-第23集《新亚特兰蒂斯》', '成龙历险记-第24集《第八扇门》', '成龙历险记-第25集《终极对话(上)》',
             '成龙历险记-第26集《终极对话(下)》', '成龙历险记-第27集《战斗之母》', '成龙历险记-第28集《冷冻中的危险》', '成龙历险记-第29集《恒河宝藏》', '成龙历险记-第30集《迷失的城市》',
             '成龙历险记-第31集《莲花寺》', '成龙历险记-第32集《魔兽的诅咒》', '成龙历险记-第33集《决战西部》', '成龙历险记-第34集《折纸神偷》', '成龙历险记-第35集《特工塔格》',
             '成龙历险记-第36集《善恶龙叔》', '成龙历险记-第37集《童子军的荣誉》', '成龙历险记-第38集《国王和小玉》', '成龙历险记-第39集《变猫记》', '成龙历险记-第40集《游览航行》',
             '成龙历险记-第41集《圣斗士》', '成龙历险记-第42集《手套的故事》', '成龙历险记-第43集《危机四伏》', '成龙历险记-第44集《军团女孩》', '成龙历险记-第45集《万事通》',
             '成龙历险记-第46集《缩小的包裹》', '成龙历险记-第47集《美猴王的木偶》', '成龙历险记-第48集《吸血鬼的血》', '成龙历险记-第49集《复活的士兵》', '成龙历险记-第50集《善恶之争》',
             '成龙历险记-第51集《捕蛇记》', '成龙历险记-第52集《时空隧道》', '成龙历险记-第53集《重新加入龙小组》', '成龙历险记-第54集《魔力的爆发》', '成龙历险记-第55集《顽皮的猴子》',
             '成龙历险记-第56集《争鼠记》', '成龙历险记-第57集《两个龙叔》', '成龙历险记-第58集《会飞的猪》', '成龙历险记-第59集《隐身妈妈》', '成龙历险记-第60集《羊符咒的魔力》',
             '成龙历险记-第61集《兔子跑了》', '成龙历险记-第62集《快乐J团队的圣诞节》', '成龙历险记-第63集《渺小的瓦龙和高大的小玉》', '成龙历险记-第64集《牛首事件》',
             '成龙历险记-第65集《龙的再现》', '成龙历险记-第66集《动物饼干》', '成龙历险记-第67集《歌剧院之夜》', '成龙历险记-第68集《特鲁是谁》', '成龙历险记-第69集《克隆成龙团队》',
             '成龙历险记-第70集《鬼影军团的面具》', '成龙历险记-第71集《拉苏变成了武士》', '成龙历险记-第72集《出色的T军团》', '成龙历险记-第73集《布莱克警长的法力》',
             '成龙历险记-第74集《黑影追踪》', '成龙历险记-第75集《万圣节的礼物》', '成龙历险记-第76集《食影人》', '成龙历险记-第77集《功夫面具》', '成龙历险记-第78集《学做好人》',
             '成龙历险记-第79集《两个小玉》', '成龙历险记-第80集《小鬼大盗》', '成龙历险记-第81集《记忆宝石之争》', '成龙历险记-第82集《忍者之光》', '成龙历险记-第83集《纸扇之谜》',
             '成龙历险记-第84集《小岛之旅》', '成龙历险记-第85集《双魔出击》', '成龙历险记-第86集《童子军的探险记》', '成龙历险记-第87集《翅膀下的魔变》', '成龙历险记-第8集《8镜子镜子》',
             '成龙历险记-第89集《驼鹿行动》', '成龙历险记-第90集《海底探险》', '成龙历险记-第91集《西雅图上空的闪电》', '成龙历险记-第92集《特鲁的烦恼》', '成龙历险记-第93集《故地重游》',
             '成龙历险记-第94集《智斗小龙(一)》', '成龙历险记-第95集《智斗小龙(二)》']

    # rename.rename_file(path, names, '.mp4')
    rename.rename_batch(path, '侠客行', '.mp4')
