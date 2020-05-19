from unittest import SkipTest


# 跳过用例的判断，如果存在失败用例或者错误用例，直接跳过
def if_skip_case(object):
    if object._resultForDoCleanups.failures or object._resultForDoCleanups.errors:
        raise SkipTest("do not excute because {} is failed".format(object._resultForDoCleanups.failures[0][0]._testMethodName))