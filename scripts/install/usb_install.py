import threading


# 装包用的线程
class usb_install_thread(threading.Thread):
    def __init__(self, funcName, *args):
        threading.Thread.__init__(self)
        self.args = args
        self.funcName = funcName

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        self.funcName(*(self.args))


# # 选择设备（旧版）
# def devices_choice(i=0):
#     devicesList = get_devices()
#     if len(devicesList) >= 2:
#
#         # 连接手机 默认连接方式
#         connect_device("android:///")
#
#         # 指定设备号连接
#         connect_device("android:///" + devicesList[i][0])
#
#
# # 获取设备列表
# def get_devices():
#     adb = ADB()
#     adb.check_app()
#     devicesList = adb.devices()
#     return devicesList
#
#
# # 检查包体是否存在
# def checkapp(pakge):
#     adb = ADB()
#     if adb.check_app(pakge):
#         return True
#     else:
#         return False
#
#
# # 选择设备
# def connect(devices=None):
#     try:
#         print('正在连接设备：', devices)
#         if devices in device_info.keys():
#             connect_device("android:///")
#             connect_device("android:///" + device_info[devices])
#         elif devices in device_info.values():
#             connect_device("android:///")
#             connect_device("android:///" + devices)
#         elif devices == None:
#             devicesList = get_devices()
#             if len(devicesList) >= 2:
#                 # 连接手机 默认连接方式
#                 connect_device("android:///")
#
#                 # 指定设备号连接
#                 connect_device("android:///" + devicesList[0][0])
#     except Exception as e:
#         print('connect to adb error: ', e)
#         raise Exception


# if __name__ == '__main__':
#     print(get_devices())