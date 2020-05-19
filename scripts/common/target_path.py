import os


def get_path(p=0):
    '''
    获取当前目录，上级目录，上上级目录，上上上级目录
    :param p: 0.当前目录，1.上级目录 2.上上级目录 3.上上上级目录......4
    :return:
    '''
    path = os.getcwd()
    file_or_dir_list = path.split('\\')
    length = len(file_or_dir_list)

    if p in range(0, length+1):
        path_list = file_or_dir_list[0:length-p]
        path = '\\'.join(path_list)
        return path
    else:
        return os.getcwd()


if __name__ == '__main__':
    print(get_path(0))
    print(get_path(1))
    print(get_path(2))
    print(get_path(3))
    print(get_path(4))
    print(get_path(5))
    print(get_path(6))
    print(get_path(7))
