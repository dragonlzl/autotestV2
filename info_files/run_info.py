'''
运行前的数据准备配置
因为都是以当前接入的设备为主，所以需要按照当前接入的设备，动态进行配置
'''

from info_files import info
from scripts.common import devicesTool
from info_files import runInfo_json_handle


# 动态获取当前连接的设备信息
devicesList = devicesTool.get_devices()

# 把设备id单独放进一个list中
id_list = devicesTool.get_phone_id(devicesList)

# 写进入json文件
runInfo_json_handle.run_info_write_to_json(id_list)

# 动态获取当前渠道列表，来源info.apk_info
channal_list = [channal for channal in info.apk_info.keys()]

running_info = []


def device_run_info(devices=id_list, channal_list=channal_list):
    '''
    格式化数据，返回ddt所需要的数据格式，因为参数都是运行时获取的，所以也能整理成动态数据

    :param devices: 设备号的列表
    :param channal_list: 渠道列表
    :return: [(device, apk_path, packagename), (device, apk_path, packagename)]
    '''
    all_list = []
    run_list = []
    for device in devices:
        for channal in channal_list:
            channal_apks_list = info.apk_info[channal]
            channal_apks_num = len(channal_apks_list)
            for i in range(0, channal_apks_num):
                run_list.append(device)
                apk_path = info.apk_info[channal][i]['apk_path']
                packagename = info.apk_info[channal][i]['package_name']
                run_list.append(apk_path)
                run_list.append(packagename)
                # 添加到最大的表
                all_list.append(tuple(run_list))
                # 添加完后初始化
                run_list = []

    return all_list


def assignment_device_run_info(devices=id_list, channal_list=channal_list):
    '''
    格式化数据，返回ddt所需要的数据格式，因为参数都是运行时获取的，所以也能整理成动态数据
    自动分配专用
    自动分配方式
        1.设备数比渠道数少
            如设备为[d1,d2],渠道为[c1,c2,c3,c4]，则会让设备list变成[d1,d2,d1,d2]以和渠道1:1对应
            d1跑c1的全部包体，d2跑c2的全部包体，然后d1跑c3的全部包体，d2跑c4的全部包体
        2.设备数比渠道数多
            如设备为[d1,d2，d3，d4],渠道为[c1,c2]，则会让设备list变成[d1,d2]以和渠道1:1对应
            d1跑c1的全部包体，d2跑c2的全部包体，d3和d4，就不跑了
        3.设备数和渠道数一样多
            本来就要处理成一样多，现在既然一样多久无需处理


    :param devices: 设备号的列表
    :param channal_list: 渠道列表
    :return: [(device, apk_path, packagename), (device, apk_path, packagename)]
    '''
    all_list = []
    run_list = []

    assignment_list = assignment(devices, len(channal_list))

    for i in range(0, len(assignment_list)):
        channal_apks_list = info.apk_info[channal_list[i]]
        channal_apks_num = len(channal_apks_list)
        device = assignment_list[i]

        for j in range(0, channal_apks_num):
            run_list.append(device)
            apk_path = info.apk_info[channal_list[i]][j]['apk_path']
            packagename = info.apk_info[channal_list[i]][j]['package_name']
            run_list.append(apk_path)
            run_list.append(packagename)
            # 添加到最大的表
            all_list.append(tuple(run_list))
            # 添加完后初始化
            run_list = []

    return all_list


def assignment(source_list, target):
    '''
    分配的核心算法，目前的功能是，让source_list的长度变成target
    :param source_list: 需要变化的原list
    :param target: 想要变成的长度
    :return: 比如让source_list = [1, 2, 3], target = 7 最终返回[1, 2, 3, 1, 2, 3, 1]
    '''
    num = len(source_list)
    if num == target:
        return source_list
    elif num < target:
        diff = target - num
        for i in range(0, diff):
            source_list.append(source_list[i])
        return source_list
    else:
        for i in range(0, target):
            source_list.append(source_list[i])
        return source_list


def packagename_info(run_list=device_run_info()):
    '''
    根据ddt格式数据列表返回包名列表

    :param run_list: ddt格式数据列表
    :return: 包名列表
    '''
    packagename_list = []
    for info in run_list:
        if info[2] not in packagename_list:
            packagename_list.append(info[2])

    return packagename_list


if __name__ == '__main__':
    # print('id_list:{0}'.format(id_list))
    # print('channal_list:{0}'.format(channal_list))
    # print('info.apk_info:{0}'.format(info.apk_info))
    run_list = device_run_info()
    print('run_list:{0}'.format(run_list))
    # packagename_list = packagename_info()
    # print('packagename_list:{0}'.format(packagename_list))
    # print(assignment([1, 2, 3, 4, 5], 29))
    a_run_list = assignment_device_run_info()
    print('a_run_list:{0}'.format(a_run_list))
