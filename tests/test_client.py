import unittest
import filesystem_pysdk as filesystem

client: filesystem.Client = None


def setUpModule():
    print("into test_client.py")
    global client
    client, err = filesystem.new_client("system",
                                        "53fc91f6fe8ab61ca9bf5ce7c159c0c9",
                                        "http://localhost:8001",
                                        "http://localhost:8000")
    assert client is not None
    assert err is None


def tearDownModule():
    print('go out test_client.py')


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = filesystem.User("i-curve", "", filesystem.User.UType.UTypeUser)

    def test_01_add_user(self):
        with self.assertRaises(TypeError):
            client.add_user("i-curve")
        res = client.add_user(self.user)
        self.assertIsNone(res, res)

    def test_02_delete_user(self):
        res = client.delete_user("i-curve")
        self.assertIsNone(res, res)


class TestBucket(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bucket = filesystem.Bucket("i-curve", filesystem.Bucket.BType.BTypeReadWrite, False)

    def test_01_add_bucket(self):
        with self.assertRaises(TypeError):
            client.add_bucket("bucket1")

        res = client.add_bucket(self.bucket)
        self.assertIsNone(res, res)

    def test_02_delete_bucket(self):
        res = client.delete_bucket("i-curve")
        self.assertIsNone(res, res)


if __name__ == '__main__':
    unittest.main()
