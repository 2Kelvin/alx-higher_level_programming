import unittest
from models.base import Base


mybase = Base()
mybase2 = Base()
mybase3 = Base()
mybase4 = Base(12)
mybase5 = Base()


class TestBaseClass(unittest.TestCase):
    def test_object_type(self):
        self.assertTrue(type(mybase) == Base)

    def test_class_instance(self):
        self.assertTrue(isinstance(Base, object))

    def test_class_subclass(self):
        self.assertTrue(issubclass(Base, object))

    def test_id_none(self):
        self.assertEqual(mybase.id, 1)

    def test_id_none2(self):
        self.assertEqual(mybase2.id, 2)

    def test_id_none3(self):
        self.assertEqual(mybase3.id, 3)

    def test_id_given(self):
        self.assertEqual(mybase4.id, 12)

    def test_id_none5(self):
        self.assertEqual(mybase5.id, 4)

    def test_got_to_json_string(self):
        self.assertTrue("to_json_string" in dir(Base))

    def test_list_none(self):
        self.assertEqual(mybase2.to_json_string(None), "[]")

    def test_list_empty(self):
        self.assertEqual(mybase2.to_json_string([]), "[]")

    def test_got_save_to_file(self):
        self.assertTrue("save_to_file" in dir(Base))

    def test_got_from_json_string(self):
        self.assertTrue("from_json_string" in dir(Base))

    def test_py_list_none(self):
        self.assertEqual(mybase3.from_json_string(None), [])

    def test_py_list_empty(self):
        self.assertEqual(mybase3.from_json_string("[]"), [])

    def test_got_create(self):
        self.assertTrue("create" in dir(Base))

    def test_got_load_from_file(self):
        self.assertTrue("load_from_file" in dir(Base))


if __name__ == "__main__":
    unittest.main()
