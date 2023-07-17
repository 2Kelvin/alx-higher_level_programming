import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


s1 = Square(5)
s2 = Square(2, 2)
s3 = Square(3, 1, 3, 12)


class TestClassSquare(unittest.TestCase):
    def test_object_type(self):
        self.assertTrue(type(s1) == Square)

    def test_class_instance_rec(self):
        self.assertTrue(isinstance(s1, Square))

    def test_class_instance_base(self):
        self.assertTrue(isinstance(s1, Base))

    def test_class_instance_obj(self):
        self.assertTrue(isinstance(s1, object))

    def test_class_subclass(self):
        self.assertTrue(issubclass(Square, Rectangle))

    def test_class_subclass(self):
        self.assertTrue(issubclass(Square, object))

    def test_class_subclass_base(self):
        self.assertTrue(issubclass(Square, Base))

    def test_sq_area(self):
        self.assertEqual(s1.area(), 25)

    def test_sq_area2(self):
        self.assertEqual(s2.area(), 4)

    def test_sq_area3(self):
        self.assertEqual(s3.area(), 9)

    def test_got_area(self):
        self.assertTrue("area" in dir(s1))

    def test_got_display(self):
        self.assertTrue("display" in dir(s1))

    def test_got_str(self):
        self.assertTrue("__str__" in dir(s1))

    def test_got_update(self):
        self.assertTrue("update" in dir(s1))

    def test_list_arg(self):
        with self.assertRaises(TypeError):
            Square([])

    def test_tuple_arg(self):
        with self.assertRaises(TypeError):
            Square(())

    def test_none_arg(self):
        with self.assertRaises(TypeError):
            Square(None)

    def test_float_arg(self):
        with self.assertRaises(TypeError):
            Square(4.6)

    def test_bool_arg(self):
        with self.assertRaises(TypeError):
            Square(True)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_extra_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_objects_type(self):
        self.assertTrue(type(s1) and type(s2) == Square)

    def test_string_arg(self):
        with self.assertRaises(TypeError):
            Square("2")

    def test_negative_arg(self):
        with self.assertRaises(ValueError):
            Square(-10)

    def test_negative_arg_y(self):
        with self.assertRaises(ValueError):
            Square(10, 2, -1)

    def test_dict_arg(self):
        with self.assertRaises(TypeError):
            Square(10, 2, {})

    # def test_id_none(self):
    #     self.assertEqual(s1.id, 1)

    # def test_id_none2(self):
    #     self.assertEqual(s2.id, 2)

    def test_id_none3(self):
        self.assertEqual(s3.id, 12)

    def test_got_dictionary(self):
        self.assertTrue("to_dictionary" in dir(s1))

    def test_got_to_json_string(self):
        self.assertTrue("to_json_string" in dir(Square))

    def test_list_none(self):
        self.assertEqual(s2.to_json_string(None), "[]")

    def test_list_empty(self):
        self.assertEqual(s2.to_json_string([]), "[]")

    def test_got_from_json_string(self):
        self.assertTrue("from_json_string" in dir(Square))

    def test_py_list_none(self):
        self.assertEqual(s2.from_json_string(None), [])

    def test_py_list_empty(self):
        self.assertEqual(s2.from_json_string("[]"), [])

    def test_got_create(self):
        self.assertTrue("create" in dir(Square))

    def test_got_load_from_file(self):
        self.assertTrue("load_from_file" in dir(Square))
