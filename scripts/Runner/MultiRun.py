#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing.pool import Pool
from scripts.Runner.caserunner import *
from scripts.common import devicesTool
from info_files import runInfo_json_handle
from info_files import info


devices_list = devicesTool.get_devices()

id_list = devicesTool.get_phone_id(devices_list)
path = os.path.join(info.root, 'info_files', 'device_info.json')
d_info = runInfo_json_handle.load_json(path)

# 判断如果设备不存在于设备的json文件中则添加进去
for device in id_list:
    if device not in d_info:
        d_info.append(device)
        runInfo_json_handle.run_info_write_to_json(d_info)


def dataMarket(devices=devices_list, assignment=False):
    '''
        处理运行的动态配置表，给ddt使用，符合ddt的使用格式，运行方式由这个函数最终产生的数据决定
        方式一，只有一台设备，运行全部包体 done
        方式二，有多个设备，每个设备都运行全部包体done
        方式一和方式二是默认方式，根据当前连接的设备数量自动判断
        方式三，有多个设备，分别运行不同的包体 ing
        return: {
                    device_id1:[
                        (device_id1, apk_path1, packagename1),
                        (device_id1, apk_path2, packagename2),
                        (device_id1, apk_path3, packagename3)
                        ],
                    devices_id2:[
                        (device_id1, apk_path1, packagename1),
                        (device_id1, apk_path2, packagename2),
                        (device_id1, apk_path3, packagename3)
                        ]
                }
        '''

    data_dict = {}
    device_num = len(devices)
    if assignment is False:
        _info = run_info.device_run_info()
    else:
        _info = run_info.assignment_device_run_info()

    # 只有一个设备的情况下，可以用这个run_info.device_run_info()
    if len(id_list) < 2:

        data_dict[id_list[0]] = info

    else:
        item_list = []
        for num in range(device_num):
            for i in range(0, len(_info)):
                if id_list[num] in _info[i]:
                    item_list.append(_info[i])
            data_dict[id_list[num]] = item_list
            item_list = []

    return data_dict


def m_run(func=run):
    '''
    多进程运行
    :param func: 执行函数
    :return: 没返回值
    '''
    data_dict = dataMarket()
    print('data_dict:{0}'.format(data_dict))
    if len(devices_list) >= 2:
        for i in range(len(run_info.running_info)):
            d_info = runInfo_json_handle.load_json(path)
            if devices_list[i][0] not in d_info:
                offline_device = devices_list[i][0]
                print('{0} is not ready'.format(offline_device))
                break
            else:
                print('{0} is ready'.format(devices_list[i][0]))

    # 创建进程池
    p = Pool(8)

    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    print(len(data_dict))

    # 多进程运行
    for i in range(0, len(data_dict)):
        # 执行数据，主要是传给ddt的数据
        run_data = data_dict[id_list[i]]
        p.apply_async(func, args=(run_data, now,))

    p.close()
    p.join()


if __name__ == '__main__':
    # m_run(run_without_report)
    print(dataMarket(assignment=True))

