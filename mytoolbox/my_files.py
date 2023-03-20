import os
import sys
import json


def read_file(f_name: str) -> str:
    """
    read text file
    """
    if not _is_abs_path(f_name):
        f_name = get_external_path() + "\\" + f_name
    with open(f_name, mode='r', encoding='utf-8', newline='') as file:
        return file.read()


def write_file(f_name: str, text: str):
    """
    write text file
    """
    if not _is_abs_path(f_name):
        f_name = get_external_path() + "\\" + f_name
    with open(f_name, mode='w', encoding='utf-8', newline='') as file:
        print(text, file=file)


def copy_file(source_path: str, destination_path: str):
    if not _is_abs_path(source_path):
        source_path = get_external_path() + "\\" + source_path
    if not _is_abs_path(destination_path):
        destination_path = get_external_path() + "\\" + destination_path
    # destination folders have to exist as first!!!
    from shutil import copyfile
    copyfile(source_path, destination_path)


def copy_dir(source_dir: str, destination_dir: str, rewrite: bool = True):
    if not _is_abs_path(source_dir):
        source_dir = get_external_path() + "\\" + source_dir
    if not _is_abs_path(destination_dir):
        destination_dir = get_external_path() + "\\" + destination_dir

    from shutil import copytree, rmtree
    if rewrite:
        if exist_dir(destination_dir):
            rmtree(destination_dir)
    copytree(source_dir, destination_dir)


def exist_file(file_name: str) -> bool:
    """
    function return bool of existing file
    """
    if not _is_abs_path(file_name):
        file_name = get_external_path() + "\\" + file_name
    return os.path.isfile(file_name)


def exist_dir(directory_name: str) -> bool:
    """
    function return bool of existing directory
    """
    if not _is_abs_path(directory_name):
        directory_name = get_external_path() + "\\" + directory_name
    return os.path.isdir(directory_name)


def get_abs_path(file_name: str) -> str:
    """
    function return absolute path from relative file name
    """
    if not _is_abs_path(file_name):
        file_name = get_external_path() + "\\" + file_name
    return os.path.abspath(file_name)


def get_file_name(file_path: str) -> str:
    """
    function return file name from absolute file path
    """
    return os.path.basename(file_path)


def get_project_dir_path() -> str:
    """
    function return absolute project folder path
    """
    # res = str(os.path.abspath(os.curdir))  #by this you will get current FILE folder, not PROJECT folder
    # res = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #by this you will get path without last folder
    return str(sys.path[1])


def get_dir(file_path: str) -> str:
    """
    function return absolute current directory path
    """
    if not _is_abs_path(file_path):
        file_path = get_external_path() + "\\" + file_path
    return os.path.dirname(file_path)


def get_cur_dir() -> str:
    """
    function return absolute current directory path
    """
    return os.curdir


def make_dir(directory_name: str) -> bool:
    """
    function create directory if it doesn't exist
    """
    if not _is_abs_path(directory_name):
        directory_name = get_external_path() + "\\" + directory_name
    if not exist_dir(directory_name):
        os.mkdir(directory_name)
        return True
    return False


def write_json(json_file_name: str, data: object):
    if not _is_abs_path(json_file_name):
        json_file_name = get_external_path() + "\\" + json_file_name
    try:
        j_data = json.dumps(data, ensure_ascii=False, indent=2)
        write_file(json_file_name, j_data)
    except Exception as ex:
        raise SyntaxError("JSON writing error: " + str(ex))


def read_json(json_file_name: str) -> str:
    if not _is_abs_path(json_file_name):
        json_file_name = get_external_path() + "\\" + json_file_name
    try:
        j_data = json.loads(read_file(json_file_name))
        return j_data
    except Exception as ex:
        raise SyntaxError("JSON reading error: " + str(ex))


def get_files_with_extension(extension: str) -> list:
    if not extension.startswith("."):
        extension = "." + extension

    files = []
    for file in os.listdir(get_external_path()):
        if file.endswith(extension):
            files.append(file)

    return files


def get_drive_from_path(file_path: str) -> str:
    if not _is_abs_path(file_path):
        file_path = get_external_path() + "\\" + file_path
    drive_tail = os.path.splitdrive(file_path)
    return drive_tail[0]  # Like - C:
    # return drive_tail[1]  # Like - \User\Documents\file.txt


def get_internal_path() -> str:
    """
    :return: Return internal path of actual executed file
    In case of exe file return e.g. C:\\Temp\\_MEI36202
    In case of PyCharm return e. g. C:\\Users\\konepa1\\PycharmProjects\\gFIT_steps_generator
    get_internal_path + get_external_path will have the same result in case of PyCharm
    """
    return os.path.dirname(sys.modules['__main__'].__file__)


def get_external_path() -> str:
    """
    :return: Return external path of actual executed file
    In case of exe file return e.g. C:\\Users\\konepa1\\Desktop
    In case of PyCharm return e. g. C:\\Users\\konepa1\\PycharmProjects\\gFIT_steps_generator
    get_internal_path + get_external_path will have the same result in case of PyCharm
    """
    if getattr(sys, 'frozen', False):
        # one-file execution file folder
        return os.getcwd()
    else:
        # PyCharm development folder
        # return os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 3)[0]
        return os.getcwd()


def _is_abs_path(path: str) -> bool:
    return os.path.isabs(path)
