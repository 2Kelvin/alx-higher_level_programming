import unittest
from models.rectangle import Rectangle
from models.base import Base


rec = Rectangle(10, 2)
rec2 = Rectangle(2, 10)
rec3 = Rectangle(10, 2, 0, 0, 12)


class TestClassRectangle(unittest.TestCase):
    # def test_id_none(self):
    #     self.assertEqual(Rectangle(5, 10).id, 1)

    # def test_id_none2(self):
    #     self.assertEqual(Rectangle(6, 8).id, 2)

    def test_id_none3(self):
        self.assertEqual(rec3.id, 12)

    def test_object_type(self):
        self.assertTrue(type(rec) == Rectangle)

    def test_class_instance(self):
        self.assertTrue(isinstance(rec, object))

    def test_class_subclass(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_objects_type(self):
        self.assertTrue(type(rec) and type(rec3) == Rectangle)

    def test_string_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_negative_arg(self):
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

    def test_negative_arg_y(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_dict_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, {})

    def test_list_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, [])

    def test_tuple_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, ())

    def test_none_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10, None)

    def test_float_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 4.6)

    def test_bool_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(True, 4)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_extra_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_rec_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_rec_area2(self):
        self.assertEqual(Rectangle(2, 10).area(), 20)

    def test_rec_area3(self):
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_got_area(self):
        self.assertTrue("area" in dir(rec))

    def test_got_display(self):
        self.assertTrue("display" in dir(Rectangle(3, 4)))

    def test_got_str(self):
        self.assertTrue("__str__" in dir(rec))

    def test_got_update(self):
        self.assertTrue("update" in dir(rec))

    def test_got_dictionary(self):
        self.assertTrue("to_dictionary" in dir(rec))

    def test_got_to_json_string(self):
        self.assertTrue("to_json_string" in dir(Rectangle))

    def test_got_from_json_string(self):
        self.assertTrue("from_json_string" in dir(Rectangle))

    def test_py_list_none(self):
        self.assertEqual(rec2.from_json_string(None), [])

    def test_py_list_empty(self):
        self.assertEqual(rec2.from_json_string("[]"), [])

    def test_got_create(self):
        self.assertTrue("create" in dir(Rectangle))

    def test_got_load_from_file(self):
        self.assertTrue("load_from_file" in dir(Rectangle))


if __name__ == "__main__":
    unittest.main()
