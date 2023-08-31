from os.path import dirname


def folder_path():
    return dirname(__file__)


def load_images():
    folder_path1 = str(folder_path())
    image_path = folder_path1 + "/images/option_2--.png"

    image_path_2 = image_path.replace("\\", "/")

    print(image_path_2)


load_images()
