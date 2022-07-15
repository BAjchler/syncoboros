import unittest
import Client.file_picker


class TestFilePicker(unittest.TestCase):
    """
    Class with filepicker generator tests.

    """
    def test_pick_file(self):
        """Test if path has a correct extension, raises exception when cancelled."""
        picker = Client.file_picker.FilePicker()
        path = picker.pick_file()
        extension_pos = path.rfind(".")
        extension = "*" + path[extension_pos:]
        self.assertIn(extension, picker.SUPPORTED_FORMATS[0][1])
