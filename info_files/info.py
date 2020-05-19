'''
存储一些配置信息
关键信息：
    root:根目录（其他文件目录都是基于根目录）
    channal_phone_info：渠道（oppo/vivo/华为等渠道）对应的安装apk时的密码
    tap_user_info：tap渠道的登陆账号和密码
    devices_info：常用的设备信息
    channal_info：渠道分类，用于定义一个手机执行某一个分类的包的测试


'''

from scripts.common.getApkinfo import *
import os

root = r'D:\PycharmProjects\tool\autotestV2'


apk_path = os.path.join(root, 'apk')
# 动态获取当前要测的apk信息
apk_info = apk_packagename(apk_path)

report_path = os.path.join(root, 'report')
bug_png_path = os.path.join(root, 'bug_image')

channal_phone_info = {
    'oppo': {
        'pw': 'xxxx'
    }
}

tap_user_info = {
    'account1': {
        'account':  'xxxx', 'pw': 'xxxx'
    },
    'account2': {
        'account':  'xxxx', 'pw': 'xxxx'
        }

}

devices_info = {
    '5PZTCUOJZTJFEM5S': ['oppo', 'oppo_A83'],
    '86248021': ['oppo', 'oppo_A5']
}

