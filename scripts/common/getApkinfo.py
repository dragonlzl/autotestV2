import os
import json
from scripts.common import target_path


def file_name(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.apk':
                L.append(os.path.join(root, file))
    return L


def apks_path(path, dir_list, file_list):
    dir_or_files = os.listdir(path)
    for dir_file in dir_or_files:
        dir_file_path = os.path.join(path, dir_file)
        if os.path.isdir(dir_file_path):
            dir_list.append(dir_file_path)
            apks_path(dir_file_path, dir_list, file_list)
        else:
            file_list.append(dir_file_path)


def adb_cmd_apk(filepath):
    packagename = None
    if not os.path.exists(filepath):
        return 0
    getPackage = 'aapt d badging %s | find "package"' % (filepath)
    result = os.popen(getPackage).readlines()
    for i in range(len(result)):
        package = result[i].find("name='")
        versionCodeNumber = result[i].find("' versionCode")
        packagename = result[i][package + 6:versionCodeNumber]

    return packagename


def apk_packagename(path):
    '''
    可以获取渠道名，apk名，包名，路径

    :param path: apk文件夹的路径
    :return: {
                channal:[
                    {apk_name:xx, apk_path:xx,, packagename:xx},
                    {apk_name:xx, apk_path:xx,, packagename:xx}
                    ],
                channal:[
                    {apk_name:xx, apk_path:xx,, packagename:xx}
                    ]
            }
    '''
    packages_dict = {}
    package_dict = {}
    packagename_list = []
    dir_list = []
    file_list = []
    apks_path(path, dir_list, file_list)
    for file in file_list:
        apk_name = file.split('\\')[-1]
        apk_path = file
        if '.apk' in apk_name:
            channel = file.split('\\')[-2]
            # apk_name = file.split('\\')[-1]
            packagename = adb_cmd_apk(file)
            if channel not in packages_dict.keys():
                packages_dict[channel] = []
            package_dict['apk_name'] = apk_name
            package_dict['package_name'] = packagename
            package_dict['apk_path'] = apk_path
            package_dict['apk_channel'] = channel
            packages_dict[channel].append(package_dict)
            package_dict = {}
            # package_dict[channel]['apk_name'] = apk_name
            # package_dict[channel]['package_name'] = packagename
            # package_dict[channel]['apk_path'] = apk_path
            # package_dict[channel]['apk_channel'] = channel

            packagename_list.append(packagename)

    # print(packages_dict)

    return packages_dict


def write_to_json(data):
    id = 0
    data_dict = {}
    data_list = []
    for items in data.values():
        if len(items) > 0:
            for item in items:
                data_list.append(item)
                data_dict[id] = data_list
                data_list = []
                id += 1

    jsondata = json.dumps(data_dict, indent=4, separators=(',', ': '))
    with open('test_data.json', 'w') as f:
        f.write(jsondata)
        f.close()


if __name__ == '__main__':

    print(os.path.dirname(os.getcwd()))
    root = target_path.get_path(2)

    path = os.path.join(root, 'apk')
    data = apk_packagename(path)
    # write_to_json(data)
