from ddt import ddt, data, unpack
from scripts.install.usb_install import *
import unittest
from scripts.case.all_case import case
from info_files import run_info

# run_list = run_info.device_run_list
# packagename_list = run_info.packagename_info(run_list=run_list)

# aa = [('5PZTCUOJZTJFEM5S', apk_info['4399'][0]['apk_path'], apk_info['4399'][0]['package_name']), ('5PZTCUOJZTJFEM5S', apk_info['tap'][0]['apk_path'], apk_info['tap'][0]['package_name'])]

# root = root_path.get_root_path()
# apk_path = os.path.join(root, 'apk')
# report_path = os.path.join(root, "report")
#
# apk_info = apk_info
# oppo_info = phone_info['oppo']
# button = getImagePath.png_dict(root)


info = run_info.running_info
print('run_info:{0}'.format(info))

@ddt
class normalTest(unittest.TestCase):

    # run_list = run_info.run_info()
    # ackagename_list = run_info.packagename_info(run_list=run_list)

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(*info)
    @unpack
    def test_01_normal(self, device, apk_path, apk_name):
        # if_skip_case(self)
        case.apk_install(device=device, apk_path=apk_path, apk_name=apk_name)
        if apk_name == 'com.ChillyRoom.DungeonShooter':
            case.tap_login()
            case.tap_infocheck()
        case.apk_uninstall(apk_name=apk_name)

    # def test_02_number(self):
    #     # if_skip_case(self)
    #     try:
    #         self.assertEqual(1, 2)
    #     except Exception:
    #         raise AssertionError
    #
    # def test_03_number(self):
    #     # if_skip_case(self)
    #     try:
    #         self.assertEqual(1, 1)
    #     except Exception:
    #         raise AssertionError

    # @data((1, 2), (3, 4))
    # @data(*aaa)
    # @unpack
    # def test_04_number(self, a, b, c):
    #     try:
    #         print(a, b, c)
    #         self.assertEqual(1, 1)
    #     except Exception:
    #         raise AssertionError


if __name__ == '__main__':

    # run_list = run_info.run_info()
    #
    # testsuite = unittest.TestSuite()
    # testsuite.addTest(ParamTestCase.ParametrizedTestCase.parametrize(normalTest, param=run_list))
    testsuite = unittest.TestLoader().loadTestsFromTestCase(normalTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(testsuite)
