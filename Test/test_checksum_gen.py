import unittest
import os
from Client.checksum_gen import ChecksumGen


class TestChecksumGenerator(unittest.TestCase):
    def test_sha256(self):
        file_name = "example.txt"
        with open(file_name, "w") as file:
            file.write("This is an example file!")
        generator = ChecksumGen(file_name)
        checksum = generator.generate_checksum()
        os.remove(file_name)
        self.assertEqual(checksum, "dbe5822c7b06125fe6905add0c9056e76cb73b5a1621141a2126188ebf83f6a6", "Wrong checksum")
        print(f'generated checksum = {checksum}')

    def test_large_file_sha256(self):
        file_name = "big_file.txt"
        generator = ChecksumGen(file_name)
        with open(file_name, "w") as file:
            big_string = generator.MAX_MEMORY_USAGE * "aa"
            file.write(big_string)
        checksum = generator.generate_checksum()
        os.remove(file_name)
        self.assertEqual(checksum, "aedf73997fc5d20382db198895a702c144ef528b6c4e3252c80cc100fac6b9d4", "Wrong checksum")
        print(f'generated checksum = {checksum}')
