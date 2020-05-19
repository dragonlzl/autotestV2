'''
运行时的数据准备，主要是把数据写到json，或者从json读取

'''
from info_files import info
import json
import os

path = os.path.join(info.root, 'info_files')


def run_info_write_to_json(data=[], filename=path + '\\device_info.json'):
    with open(filename, 'w') as file_obj:
        json.dump(data, file_obj)


def load_json(filename):
    with open(filename) as file_obj:
        data = json.load(file_obj)

    return data


if __name__ == '__main__':
    # run_list = [(1, 2), (3, 4)]

    run_list = [(1, 2), (3, 4)]
    run_info_write_to_json(run_list, filename=path + '\\device2_info.json')

    print(type(load_json(path + '\\device_info.json')))


