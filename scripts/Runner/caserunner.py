#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
用例单独执行时用到的模块，
多进程执行就是多进程运行此模块的run方法
'''

from scripts.common import HTMLTestRunner
from info_files import info
from info_files import run_info
import unittest
import time
import os

root = info.root
case_path = os.path.join(root, 'scripts', 'case')


def loadcases(caseClassName):
    '''
    根据用例的class名字加载用例，使用的是unittest.TestLoader().loadTestsFromTestCase()方式
    :param caseClassName: 用例的class名
    :return: 测试套件
    '''

    testsuite = unittest.TestLoader().loadTestsFromTestCase(caseClassName)
    return testsuite


def load_file_case(path=case_path):
    '''
    直接根据文件名去加载用例，使用此函数，必须让用例所在的.py文件名以 Test_ 开头，如Test_DemoCase.py
    :param path: case的路径
    :return: discover
    '''
    discover = unittest.defaultTestLoader.discover(
        path,
        pattern='Test_*.py',
        top_level_dir=None
    )
    return discover


def run(data, now):
    '''
    运行的核心函数

    :param data:
    :param now:
    :return:
    '''
    processId = os.getpid()
    print('子进程ID：{0}，创建进程成功'.format(processId))
    print("自动化测试开始:", now)

    # 必须 1.先加载数据
    run_info.running_info = data

    # 再 2.载入用例
    # 文件名加载方式就不需要import这个
    # from scripts.case import Test_normal

    # 指定执行
    # testsuite = loadcases(Test_normal.normalTest)

    # 指定名字格式执行
    testsuite = load_file_case()

    # 报告存放路径
    report_path = os.path.join(info.root, 'report')
    # 具体的报告名字生成
    result_path = os.path.join(report_path, "result_" + now + ".html")

    fp = open(result_path, "wb")
    # test_result = unittest.TextTestRunner(verbosity=2).run(testsuite)
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        verbosity=2,
        title=u'自动化测试报告,测试结果如下：',
        description=u'用例执行情况：'
    )

    result = runner.run(testsuite)
    fp.close()
    end = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    print("自动化测试结束:", end)
    print("报告路径:", result_path)
    print(result.failure_count)


def run_without_report(data, now):
    '''
    无报告版的
    :param data:
    :param now:
    :return:
    '''
    processId = os.getpid()
    print(now)
    print('子进程ID：{0}，创建进程成功'.format(processId))

    run_info.running_info = data

    # 文件名加载方式就不需要import这个
    # from scripts.case import Test_normal

    # 指定执行
    # testsuite = loadcases(Test_normal.normalTest)

    # 指定名字格式执行
    testsuite = load_file_case()

    # test_result = unittest.TextTestRunner(verbosity=2).run(testsuite)
    runner = unittest.TextTestRunner(verbosity=2)

    # 4、调用add_case函数返回值
    runner.run(testsuite)  # 参数为选择全部还是选择单独



