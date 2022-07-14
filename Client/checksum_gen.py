import hashlib


class ChecksumGen:
    def __init__(self, file_path):
        self.file_path = file_path
        self.__checksum = None
        self.MAX_MEMORY_USAGE = 200000000

    def get_path(self):
        return self.file_path

    def set_path(self, file_path):
        self.file_path = file_path

    def generate_checksum(self):
        with open(self.file_path, "rb") as file:
            checksum = hashlib.sha256(file.read(self.MAX_MEMORY_USAGE)).hexdigest()
            self.__checksum = checksum
            return checksum
