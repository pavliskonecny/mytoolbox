import os
import sys


class MyPyInstaller:
    def __init__(self, gui_app: bool, one_file: bool, py_file_name: str = "main.py", exe_file_name: str = "",
                 icon_path: str = "", included_folder_path: str = "", dist_path_folder: str = "",
                 open_dist_folder: bool = False):
        """

        :param gui_app: False will create console app. True will create GUI app
        :param one_file: True means one exe file. False means folder with necessary files and exe file
        :param py_file_name: Name of main PY file. Default name is "main.py"
        :param exe_file_name: Name of exe file. Default name will be the same as project folder
        :param icon_path: Path of icon file. Default value means without ico
        :param included_folder_path: Included folder to exe file. Default value means no folder
        :param dist_path_folder: Folder, where to place exe file. Default value means "dist" folder
        :param open_dist_folder: If TRUE, distribution folder with exe file will be opened. Default value means no open
        """
        self.gui_app = gui_app
        self.one_file = one_file
        self.py_file_name = py_file_name
        self.exe_file_name = exe_file_name
        self.add_exe_file_name = (exe_file_name != "")
        self.icon_name = icon_path
        self.add_icon = (icon_path != "")
        self.add_folder_name = included_folder_path
        self.add_folder = (included_folder_path != "")
        self.dist_path_folder = dist_path_folder
        self.open_dist_folder = open_dist_folder

        print("Start building ...")
        self._make_build()
        print("Build is DONE")
        if self.open_dist_folder:
            self._open_folder()

    def _make_build(self):
        project_name = self._get_project_name()
        project_folder = self._get_project_folder()

        cmd = "pyinstaller --noconfirm --log-level=WARN --clean"

        if self.one_file:
            cmd += " --onefile"

        if self.gui_app:
            cmd += " --noconsole"

        if self.add_folder:
            cmd += " --add-data " + project_folder + "\\" + self.add_folder_name + ";" + self.add_folder_name

        cmd += " " + project_folder + "\\" + self.py_file_name
        cmd += " --name " + project_name
        cmd += " --specpath " + project_folder + "\\build\\"    # for spec file
        cmd += " --workpath " + project_folder + "\\build\\"    # for build file
        
        if self.dist_path_folder:  # for distribution exe file
            cmd += " --distpath " + project_folder + "\\" + self.dist_path_folder + "\\"
        else:
            cmd += " --distpath " + project_folder + "\\dist\\"

        if self.add_icon:
            cmd += " --icon " + project_folder + "\\" + self.icon_name  # --icon MyIcon.ico

        print(cmd)
        os.system('cmd /c "' + cmd + '"')  # execute cmd

    def _get_project_name(self):
        if self.add_exe_file_name:
            return "\"" + self.exe_file_name + "\""  # "" are here because of possible spaces in the exe file name
        else:
            return os.path.basename(self._get_project_folder())  # get project name

    def _get_project_folder(self):
        # res = str(os.path.abspath(os.curdir))  #by this you will get current FILE folder, not PROJECT folder
        # res = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #you will get path without last folder
        res = sys.path[1]
        return res

    def _open_folder(self):
        dist_path = self._get_project_folder() + "\\dist\\"
        cmd = "explorer " + dist_path  # explorer C:/Users/konepa1/PycharmProjects/test/dist

        os.system('cmd /c "' + cmd + '"')  # execute cmd
