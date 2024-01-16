import unittest
import filesystem_pysdk as filesystem

client: filesystem.Client = None


def setUpModule():
    print(f"into test_filesystem.py")
    global client
    client, err = filesystem.new_client("system",
                                        "53fc91f6fe8ab61ca9bf5ce7c159c0c9",
                                        "http://localhost:8001",
                                        "http://localhost:8000")
    assert client is not None
    assert err is None


def tearDownModule():
    print(f"go out test_filesystem.py")


class TestFilesystem(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.file = filesystem.File("bucket", "test/a.py", 0)
        self.file2 = filesystem.File("bucket", "test2/b.py", 0)

    def test_01_upload_file(self):
        with self.assertRaises(TypeError):
            client.upload_file("file1", None)
        with self.assertRaises(TypeError):
            client.upload_file(self.file, None)
        with open("test_client.py", "rb") as f:
            res = client.upload_file(self.file, f)
            self.assertIsNone(res, res)

    def test_02_move_file(self):
        res = client.move_file(self.file, self.file2)
        self.assertIsNone(res, res)
        pass

    def test_03_copy_file(self):
        res = client.copy_file(self.file2, self.file)
        self.assertIsNone(res, res)

    def test_04_download_file(self):
        res = client.download_file(self.file)
        self.assertIsNotNone(res, res)
        self.assertNotEqual(type(self), str)
        print(res)

    def test_05_delete_file(self):
        res = client.delete_file(self.file)
        self.assertIsNone(res, res)
        res = client.delete_file(self.file2)
        self.assertIsNone(res, res)


if __name__ == '__main__':
    unittest.main()
