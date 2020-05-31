import unittest

class TestMain(unittest.TestCase):

    def test_main_home(self):
        from .. import main

        with main.app.app_context():
            response = main.home()

            self.assertTrue(response)

if __name__ == '__main__':
    unittest.main()