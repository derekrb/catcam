import unittest

from app import app


class Test(unittest.TestCase):

    def setUp(self):
        app.testing = True
        app.debug = True
        self.app = app.test_client()
