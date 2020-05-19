from airtest.core.android.android import *
from airtest.core.api import *
from info_files import info
from info_files import runInfo_json_handle


# device_info =devices_info

path = os.path.join(info.root, 'info_files', 'device_info.json')
d_info = runInfo_json_handle.load_json(path)


# 选择设备（旧版）
def devices_choice(i=0):
    devicesList = get_devices()
    if len(devicesList) >= 2:

        # 连接手机 默认连接方式
        connect_device("android:///")

        # 指定设备号连接
        connect_device("android:///" + devicesList[i][0])


def get_phone_id(devicesList):
    id_list = []
    for i in range(len(devicesList)):
        id_list.append((devicesList[i][0]))

    return id_list


# 获取设备列表
def get_devices():
    '''

    :return: (devices,,des)
    '''
    adb = ADB()
    # adb.check_app()
    devicesList = adb.devices()
    return devicesList


# 检查包体是否存在
def checkapp(pakge):
    adb = ADB()
    if adb.check_app(pakge):
        return True
    else:
        return False


# 选择设备
def connect(device=None):
    try:
        print('正在连接设备{0}, 设备id:{1}'.format(info.devices_info[device][1], device))
        if device in d_info:
            connect_device("android:///")
            connect_device("android:///" + device)
        elif device is None:
            devicesList = get_devices()
            if len(devicesList) >= 2:
                # 连接手机 默认连接方式
                connect_device("android:///")

                # 指定设备号连接
                connect_device("android:///" + devicesList[0][0])
    except Exception as e:
        print('connect to adb error: ', e)
        raise AssertionError


if __name__ == '__main__':
    print(get_devices())