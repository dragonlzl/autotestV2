import xlwt
from scripts.common.getImagePath import *


def creatExcel(data_dict):
    workbook = xlwt.Workbook()
    ws = workbook.add_sheet('element_data')
    ws.write(0, 0, label='页面')
    ws.write(0, 1, label='控件名称')
    ws.write(0, 2, label='路径')

    row = 1

    # pages_list = list(data_dict.keys())
    for page in data_dict.keys():
        for element_name in data_dict[page].keys():
            button = data_dict[page][element_name]
            ws.write(row, 0, label=page)
            ws.write(row, 1, label=element_name)
            ws.write(row, 2, label=button)
            row += 1

    workbook.save('excel.xlsx')


if __name__ == '__main__':
    root = target_path.get_path(2)
    b = png_dict(root)
    creatExcel(b)


