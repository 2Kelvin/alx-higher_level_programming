#!/usr/bin/python3
"""Class Rectangle unittest"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


rec = Rectangle(10, 2)
rec2 = Rectangle(2, 10)
rec3 = Rectangle(10, 2, 0, 0, 12)


class TestClassRectangle(unittest.TestCase):
    """Test cases for the Base class"""

    def test_given_id(self):
        """Testing given id value"""
        self.assertEqual(rec3.id, 12)

    def test_object_type(self):
        """Testing if obje is of type Rectangle"""
        self.assertTrue(type(rec) == Rectangle)

    def test_class_instance(self):
        """If Rectangle object is of object class instance"""
        self.assertTrue(isinstance(rec, object))

    def test_class_subclass(self):
        """If Rectangle is a subclass of Base class"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_objects_type(self):
        """Comparing two Rectangle instance types"""
        self.assertTrue(type(rec) and type(rec3) == Rectangle)

    def test_string_x(self):
        """Expects type int not string"""
        with self.assertRaises(TypeError):
            Rectangle(10, 5, "2")

    def test_string_y(self):
        """Expects type int not string"""
        with self.assertRaises(TypeError):
            Rectangle(10, 5, 7, "2")

    def test_dict_y(self):
        """Expects type int not dict"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 4, {})

    def test_list_y(self):
        """Expects type int not list"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 8, [])

    def test_tuple_y(self):
        """Expects type int not tuple"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 33, ())

    def test_float_y(self):
        """Expects type int not float"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 6, 8.9)

    def test_none_x(self):
        """Expects type int not none"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 4, None)

    def test_bool_y(self):
        """Expects type int not boolean"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 7, False)

    def test_negative_width(self):
        """Expects a int greater than 0"""
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

    def test_negative_arg_y(self):
        """Expects a int greater than 0"""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_dict_x(self):
        """Expects type int not dict"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, {})

    def test_list_x(self):
        """Expects type int not list"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, [])

    def test_tuple_x(self):
        """Expects type int not tuple"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, ())

    def test_float_x(self):
        """Expects type int not float"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 8.9)

    def test_negative_x(self):
        """Expects positive int not negative"""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -3)

    def test_none_x(self):
        """Expects type int not none"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, None)

    def test_bool_x(self):
        """Expects type int not boolean"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, False)

    def test_none_height(self):
        """Expects type int not None"""
        with self.assertRaises(TypeError):
            Rectangle(10, None)

    def test_float_height(self):
        """Expects type int not float"""
        with self.assertRaises(TypeError):
            Rectangle(10, 4.6)

    def test_string_height(self):
        """Expects height int not string"""
        with self.assertRaises(TypeError):
            Rectangle(10, "java")

    def test_list_height(self):
        """Expects type int not list"""
        with self.assertRaises(TypeError):
            Rectangle(10, [8, 5])

    def test_negative_height(self):
        """Expects type int not negative int"""
        with self.assertRaises(ValueError):
            Rectangle(10, -9)

    def test_zero_width(self):
        """Expects type int not zero"""
        with self.assertRaises(ValueError):
            Rectangle(0, 9)

    def test_zero_height(self):
        """Expects type int not zero"""
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_dict_height(self):
        """Expects type int not dictionary"""
        with self.assertRaises(TypeError):
            Rectangle(10, {"i": 2, "l": 1})

    def test_tuple_height(self):
        """Expects type int not tuple"""
        with self.assertRaises(TypeError):
            Rectangle(10, (7, 5))

    def test_bool_width(self):
        """Expects int width not boolean"""
        with self.assertRaises(TypeError):
            Rectangle(True, 4)

    def test_string_width(self):
        """Expects int width not string"""
        with self.assertRaises(TypeError):
            Rectangle("Bell", 4)

    def test_float_width(self):
        """Expects width int not float"""
        with self.assertRaises(TypeError):
            Rectangle(7.4, 12)

    def test_tuple_width(self):
        """Expects width int not tuple"""
        with self.assertRaises(TypeError):
            Rectangle((1, 3, 4), 4)

    def test_dict_width(self):
        """Expects width int not dict"""
        with self.assertRaises(TypeError):
            Rectangle({"kc": 2, "lp": 9}, 4)

    def test_none_width(self):
        """Expects width int not none"""
        with self.assertRaises(TypeError):
            Rectangle(None, 4)

    def test_no_args(self):
        """Expects a width and a height"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_extra_args(self):
        """Error, pass more than required arguments"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_rec_area(self):
        """Check correct area of the rectangle"""
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_rec_area2(self):
        """Check correct area of the rectangle"""
        self.assertEqual(Rectangle(2, 10).area(), 20)

    def test_rec_area3(self):
        """Correct rectangle area with all args given"""
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_got_area(self):
        """Check if rectangle has area method"""
        self.assertTrue("area" in dir(rec))

    def test_got_display(self):
        """Check if rectangle has display method"""
        self.assertTrue("display" in dir(Rectangle(3, 4)))

    def test_got_str(self):
        """Check if rectangle has __str__ method"""
        self.assertTrue("__str__" in dir(rec))

    def test_got_update(self):
        """Check if rectangle has update method"""
        self.assertTrue("update" in dir(rec))

    def test_got_dictionary(self):
        """Check if rectangle has to_dictionary method"""
        self.assertTrue("to_dictionary" in dir(rec))

    def test_got_to_json_string(self):
        """Check if rectangle has to_json_string method"""
        self.assertTrue("to_json_string" in dir(Rectangle))

    def test_got_from_json_string(self):
        """Check if rectangle has from_json_string method"""
        self.assertTrue("from_json_string" in dir(Rectangle))

    def test_py_list_none(self):
        """Check None list passed to from_json_string"""
        self.assertEqual(rec2.from_json_string(None), [])

    def test_py_list_empty(self):
        """Check empty list passed to from_json_string"""
        self.assertEqual(rec2.from_json_string("[]"), [])

    def test_got_create(self):
        """Check if rectangle has create method"""
        self.assertTrue("create" in dir(Rectangle))

    def test_got_load_from_file(self):
        """Check if rectangle has load_from_file method"""
        self.assertTrue("load_from_file" in dir(Rectangle))

    def test_got_save_to_file(self):
        """Check if Rectangle has save_to_file method"""
        self.assertTrue("save_to_file" in dir(Rectangle))

    def test_del(self):
        """Deleting a Rectangle Instance"""
        self.rect = Rectangle(4, 8)
        del self.rect

    def test_width_get(self):
        """Getting the rectangle's width"""
        self.r5 = Rectangle(3, 9)
        self.assertEqual(self.r5.width, 3)

    def test_height_get(self):
        """Getting the rectangle's height"""
        self.r5 = Rectangle(3, 9)
        self.assertEqual(self.r5.height, 9)

    def test_x(self):
        """Getting the rectangle's x"""
        self.r5 = Rectangle(3, 9)
        self.r5.x = 11
        self.assertEqual(self.r5.x, 11)

    def test_y(self):
        """Getting the rectangle's y"""
        self.r5 = Rectangle(3, 9)
        self.assertEqual(self.r5.y, 0)

    def test_str(self):
        """Testing the object's string output"""
        r13 = Rectangle(2, 4, 3, 3, 6)
        answr = "[Rectangle] (6) 3/3 - 2/4"
        self.assertEqual(r13.__str__(), answr)

    def test_id_update(self):
        """Checking if update method works"""
        self.r5 = Rectangle(3, 9)
        self.r5.update(20)
        self.assertEqual(self.r5.id, 20)


if __name__ == "__main__":
    unittest.main()
