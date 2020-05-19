from scripts.install.usb_install import *
from scripts.common.devicesTool import *
from scripts.common import getImagePath
from info_files import info
import unittest

root = target_path.get_path(2)
button = getImagePath.png_dict(root)


class case(unittest.TestCase):
    case_isntall_skip = False
    @classmethod
    def oppo_usb_install(cls, channalNane='oppo'):
        phone = channal_phone_info[channalNane]
        try:
            sleep(10)
            if exists(Template(button['install']['pw_btn'])):
                print('找到密码输入框')
                touch(Template(button['install']['pw_btn']))
                sleep(1)
                text(phone['pw'])
                sleep(2)
                # touch(Template("image/install/button_image/install.png"))
            if exists(Template(button['install']['install'])):
                print('找到密码输入框的确定安装按钮')
                touch(Template(button['install']['install']))
                sleep(5)

            if exists(Template(button['install']['c_install'])):
                print('找到继续安装按钮')
                sleep(4)
                touch(Template(button['install']['c_install']))
                sleep(2)

            assert_exists(Template(button['install']['app_install']))
            print('找到安装按钮')

            touch(Template(button['install']['app_install']))
            print('点击安装')
            sleep(10)

        except Exception as e:
            my_screenshot()
            case.nextCaseSkip = True
            raise AssertionError(e)

        @classmethod
        def huawei_usb_install(cls, channalNane='huawei'):
            pass

        @classmethod
        def vivo_usb_install(cls, channalNane='vivo'):
            pass

    @classmethod
    def apk_install(cls, device, apk_path, apk_name):
        case.case_install_skip = False
        try:
            # self.init()
            connect(device)
            init_device("Android")
            # 如果是oppo才执行这个oppo安装
            if info.devices_info[device][0] == 'oppo':
                thread1 = usb_install_thread(cls.oppo_usb_install)

                thread1.start()
                print('正在安装apk......:{0}'.format(apk_path))

                install(apk_path)

                thread1.join()
                print('安装成功')

                start_app(apk_name)
                print('启动app:{0}'.format(apk_name))

        except Exception as e:
            my_screenshot()
            case.case_isntall_skip = True
            raise AssertionError(e)

    @classmethod
    def apk_uninstall(cls, apk_name):
        try:
            stop_app(apk_name)
            uninstall(apk_name)
            print('卸载成功:{0}'.format(apk_name))
            # assert_exists(Template(button['install']['pw_btn']))
        except Exception as e:
            my_screenshot()
            raise AssertionError(e)

    @classmethod
    def tap_login(cls):

        try:
            # 断言弹出隐私协议弹窗，在断言的api中加入了截图功能
            assert_exists(Template(button['firsttimeinstall']['title']))

            # 点击隐私协议的同意
            touch(Template(button['firsttimeinstall']['OK_bt']))
            print('点击隐私协议同意按钮')

            # 点击云存档按钮
            touch(Template(button['titlepage']['cloudsave_bt']))
            print('点击云存档按钮')

            # 断言弹出实名奖励（此手机已经进行过实名）
            sleep(3)

            # 如果有链接关闭弹出来的链接
            if exists(Template(button['realname']['link_close'])):
                touch(Template(button['realname']['link_close']))
                print('点击关闭连接')


            # 依次点击断言下一个奖励
            touch(Template(button['realname']['awark1']))
            print('点击第一个奖励')
            assert_exists(Template(button['realname']['awark2']))

            touch(Template(button['realname']['awark2']))
            print('点击第二个奖励')
            assert_exists(Template(button['realname']['awark3']))
            # assert_exists(Template(button['realname']['awark1']))

            touch(Template(button['realname']['awark3']))
            print('点击第三个奖励')

            # 断言是否弹出用户须知界面
            assert_exists(Template(button['userinstructionspage']['title']))

            # debug
            # assert_exists(Template(button['firsttimeinstall']['title']))

            print('等待5秒')
            # 等待5秒并点击同意按钮
            sleep(6)
            touch(Template(button['userinstructionspage']['OK_bt']))
            print('点击同意按钮')

            # 断言是否弹出登陆弹窗
            assert_exists(Template(button['loginpage']['pw_bt']))

            # 输入账号密码
            touch(Template(button['loginpage']['account_bt']))
            print('找到账号输入框并点击')
            text(info.tap_user_info['account1']['account'])
            print('输入账号')
            sleep(1)
            touch(Template(button['loginpage']['title']))

            touch(Template(button['loginpage']['pw_bt']))
            print('找到密码输入框并点击')
            text(info.tap_user_info['account1']['pw'])
            print('输入密码')
            touch(Template(button['loginpage']['title']))
            sleep(1)

            touch(Template(button['loginpage']['login_bt']))
            print('点击登陆按钮')

            # 断言登陆成功看到海豹宝宝并点击
            if exists(Template(button['cloudsavepage']['haibao'])):
                touch(Template(button['cloudsavepage']['haibao']))
                print('点击海豹宝宝')

            assert_exists(Template(button['cloudsavepage']['upload_bt']))
            assert_exists(Template(button['cloudsavepage']['download_bt']))
            # 断言登陆成功看到上传下载按钮
        except Exception as e:
            my_screenshot()
            raise AssertionError(e)

    @classmethod
    def tap_infocheck(cls):

        try:
            touch(Template(button['cloudsavepage']['info_bt']))
            print('点击个人信息按钮')

            assert_exists(Template(button['accountinfopage']['logout_bt']))

            assert_exists(Template(button['accountinfopage']['accounttarget']))

            touch(Template(button['accountinfopage']['close_bt']))
            print('关闭按钮')
        except Exception as e:
            my_screenshot()
            raise AssertionError(e)


