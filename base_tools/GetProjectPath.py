# GetProjectPath: 获取项目名称
import os


def get_project_path():
    project_path = os.path.abspath(os.path.dirname(__file__))
    return project_path


def get_root_path(project_name):
    project_path = get_project_path()
    find_str = '{}\\'.format(project_name)
    find_str_len = len(find_str)

    # print(project_path, project_name, project_path.find(find_str), find_str_len, project_path.find(
    #     find_str) + find_str_len)
    root_path = project_path[:project_path.find(find_str) + find_str_len]
    return root_path


if __name__ == '__main__':
    pro_name = 'base_tools'
    print(get_root_path(pro_name))
