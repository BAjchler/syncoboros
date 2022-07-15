from tkinter import filedialog
import time

class FilePicker:
    """
    Class for storing allowed extensions, and picking a valid file.
    """

    SUPPORTED_FORMATS = [("supported file types", ["*.3gp", "*.asf", "*.wmv", "*.au", "*.avi", "*.flv", "*.mov",
                                                   "*.mp4", "*.ogm", "*.ogg", "*.mkv", "*.mka", "*.ts", "*.mpg",
                                                   "*.mp3", "*.mp2", "*.nsc", "*.nsv", "*.nut", "*.ra", "*.ram", "*.rm",
                                                   "*.rv", "*.rmbv", "*.a52", "*.dts", "*.aac", "*.flac", "*.dv",
                                                   "*.vid", "*.tta", "*.tac", "*.ty", "*.wav", "*.dts", "*.xa"])]
    """
    All of extensions that are accepted by VLC.\n
    Warning: List may be incomplete.
    """
    def __init__(self):
        self.__path = None

    def get_path(self) -> str:
        """
        Get video file path.

        :return: stored path to video.
        """
        return self.__path

    def pick_file(self) -> str:
        """
        Pick file path from a file dialog.

        :return: path to picked video.
        :raises Exception: if path to file is empty
        """
        path = filedialog.askopenfilename(filetypes=self.SUPPORTED_FORMATS)
        if not path:
            raise Exception("Path not specified.")
        self.__path = path
        return path



