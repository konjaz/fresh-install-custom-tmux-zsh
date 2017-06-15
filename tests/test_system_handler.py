import unittest
from basic_functions.system_handler import define_distro
from basic_functions.system_handler import find_user_path


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.user, self.path = find_user_path()
        self.disto = define_distro()

    def test_find_user_path_returns_not_none(self):
        self.assertNotEqual((self.user, self.path), (None, None))

    def test_find_user_path_retunrns_string(self):
        should_be = ""
        self.assertEqual((type(self.user), type(self.path)), (type(should_be), type(should_be)))

    def test_define_distro_return_tuple(self):
        should_be = ()
        self.assertEqual(type(self.disto), type(should_be))