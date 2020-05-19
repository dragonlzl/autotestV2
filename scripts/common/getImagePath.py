import os
from scripts.common import target_path

def file_name(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.png':
                L.append(os.path.join(root, file))
    return L


def png_dict(path):
    image_path = os.path.join(path, 'image')
    pngs_path = file_name(image_path)
    button_dict = {}
    for png_path in pngs_path:
        path_list = png_path.split('\\')
        button_dir = path_list[-2]
        if button_dir == 'button_image':
            page = path_list[-3]
            if page not in button_dict.keys():
                button_dict[page] = {}

            button_file = path_list[-1]
            button_name = button_file.split('.png')[0]
            if button_name not in button_dict[page].keys():
                button_dict[page][button_name] = png_path

    return button_dict


if __name__ == '__main__':
    root = target_path.get_path(2)
    image_path = os.path.join(root, 'image')
    pngs_path = file_name(image_path)
    print(pngs_path)
    b = png_dict(root)
    print(b)
    print(b.keys())

