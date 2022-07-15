import hashlib


class ChecksumGen:
    """
    Class for creating a checksum from files, later used as a password to join a room.
    """

    def __init__(self, file_path: str):
        self.__file_path = file_path
        self.__checksum = None
        self.MAX_MEMORY_USAGE = 200000000
        """
        Max Memory usage limited to 200MB.\n
        Warning: changing this value will lock client out of joining a server in some cases.
        """

    def get_path(self) -> str:
        """
        Return saved path to file.

        :return: path to file
        """
        return self.__file_path

    def set_path(self, file_path: str):
        """
        Set path variable inside the generator object.

        :param file_path: path to file
        :return: None
        """
        self.__file_path = file_path

    def get_checksum(self) -> str or None:
        """
        Get generated checksum value, returns None if none was generated.

        :return: generated checksum or None.
        """
        return self.__checksum

    def generate_checksum(self) -> str or None:
        """
        Generate sha256 checksum from file, and both return it, and save to an internal variable.

        :return: generated checksum or None:
        """
        try:
            with open(self.__file_path, "rb") as file:
                checksum = hashlib.sha256(file.read(self.MAX_MEMORY_USAGE)).hexdigest()
                self.__checksum = checksum
                return checksum
        except FileNotFoundError:
            print(f"File {self.__file_path} does not exist")
            return None


