import hello
import unittest

class TestHello(unittest.TestCase):
    def setUp(self) -> None:
        self.client = hello.app.test_client()
        self.client.testing = True

    def test_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_contents(self):
        expected = "Hello World!"
        self.assertEqual(hello.hello(), expected)

if __name__ == '__main__':
    unittest.main()