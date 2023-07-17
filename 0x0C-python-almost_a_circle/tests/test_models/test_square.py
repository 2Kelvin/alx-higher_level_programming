#!/usr/bin/python3
"""Class Square unittest"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


s1 = Square(5)
s2 = Square(2, 2)
s3 = Square(3, 1, 3, 12)


class TestClassSquare(unittest.TestCase):
    """Test cases for the Square class"""

    def test_object_type(self):
        """Testing if obje is of type Square"""
        self.assertTrue(type(s1) == Square)

    def test_class_instance_rec(self):
        """If square object is a Square instance"""
        self.assertTrue(isinstance(s1, Square))

    def test_class_instance_base(self):
        """Check if object is an instance of Base"""
        self.assertTrue(isinstance(s1, Base))

    def test_class_instance_obj(self):
        """Check if object is an instance of Object"""
        self.assertTrue(isinstance(s1, object))

    def test_class_subclass(self):
        """Check if a subclass of Rectangle"""
        self.assertTrue(issubclass(Square, Rectangle))

    def test_class_subclass(self):
        """Check if a subclass of object"""
        self.assertTrue(issubclass(Square, object))

    def test_class_subclass_base(self):
        """Check if a subclass of Base"""
        self.assertTrue(issubclass(Square, Base))

    def test_sq_area(self):
        """Check square.area() calcuation"""
        self.assertEqual(s1.area(), 25)

    def test_sq_area2(self):
        """Check square.area() calcuation"""
        self.assertEqual(s2.area(), 4)

    def test_sq_area3(self):
        """Check square.area() calcuation"""
        self.assertEqual(s3.area(), 9)

    def test_got_area(self):
        """Check if rectangle has area method"""
        self.assertTrue("area" in dir(s1))

    def test_got_display(self):
        """Check if rectangle has display method"""
        self.assertTrue("display" in dir(s1))

    def test_got_str(self):
        """Check if rectangle has __str__ method"""
        self.assertTrue("__str__" in dir(s1))

    def test_got_update(self):
        """Check if rectangle has update method"""
        self.assertTrue("update" in dir(s1))

    def test_list_arg(self):
        """Expects type int not list"""
        with self.assertRaises(TypeError):
            Square([])

    def test_tuple_arg(self):
        """Expects type int not tuple"""
        with self.assertRaises(TypeError):
            Square(())

    def test_none_arg(self):
        """Expects type int not None"""
        with self.assertRaises(TypeError):
            Square(None)

    def test_float_arg(self):
        """Expects type int not float"""
        with self.assertRaises(TypeError):
            Square(4.6)

    def test_bool_arg(self):
        """Expects type int not boolean"""
        with self.assertRaises(TypeError):
            Square(True)

    def test_no_args(self):
        """Expects a size argument atleast"""
        with self.assertRaises(TypeError):
            Square()

    def test_extra_args(self):
        """More than required arguments passed"""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_objects_type(self):
        """Check type of two Square instances"""
        self.assertTrue(type(s1) and type(s2) == Square)

    def test_string_arg(self):
        """Expects type int not string"""
        with self.assertRaises(TypeError):
            Square("2")

    def test_negative_arg(self):
        """Expects greater than 0 int not negative int"""
        with self.assertRaises(ValueError):
            Square(-10)

    def test_negative_arg_y(self):
        """Expects greater than 0 int not negative int"""
        with self.assertRaises(ValueError):
            Square(10, 2, -1)

    def test_dict_arg(self):
        """Expects type int not dict"""
        with self.assertRaises(TypeError):
            Square(10, 2, {})

    def test_id_none3(self):
        """Testing given id value"""
        self.assertEqual(s3.id, 12)

    def test_got_dictionary(self):
        """Check if square has to_dictionary method"""
        self.assertTrue("to_dictionary" in dir(s1))

    def test_got_to_json_string(self):
        """Check if square has to_json_string method"""
        self.assertTrue("to_json_string" in dir(Square))

    def test_list_none(self):
        """Check None list passed to to_json_string"""
        self.assertEqual(s2.to_json_string(None), "[]")

    def test_list_empty(self):
        """Check empty list passed to to_json_string"""
        self.assertEqual(s2.to_json_string([]), "[]")

    def test_got_from_json_string(self):
        """Check if Square has from_json_string method"""
        self.assertTrue("from_json_string" in dir(Square))

    def test_got_save_to_file(self):
        """Check if Square has save_to_file method"""
        self.assertTrue("save_to_file" in dir(Square))

    def test_py_list_none(self):
        """Check None list passed to from_json_string"""
        self.assertEqual(s2.from_json_string(None), [])

    def test_py_list_empty(self):
        """Check empty list passed to from_json_string"""
        self.assertEqual(s2.from_json_string("[]"), [])

    def test_got_create(self):
        """Check if Square has create method"""
        self.assertTrue("create" in dir(Square))

    def test_got_load_from_file(self):
        """Check if Square has load_from_file method"""
        self.assertTrue("load_from_file" in dir(Square))

    def test_del(self):
        """Deleting a Square Instance"""
        self.sqq = Square(4)
        del self.sqq

    def test_size_get(self):
        """Getting the Square's size"""
        self.sq5 = Square(2)
        self.assertEqual(self.sq5.size, 2)

    def test_x(self):
        """Getting the Square's x"""
        self.sq5 = Square(9)
        self.sq5.x = 11
        self.assertEqual(self.sq5.x, 11)

    def test_y(self):
        """Getting the Square's y"""
        self.sq5 = Square(3)
        self.assertEqual(self.sq5.y, 0)

    def test_string_x(self):
        """Expects type int not string"""
        with self.assertRaises(TypeError):
            Square(5, "2")

    def test_string_y(self):
        """Expects type int not string"""
        with self.assertRaises(TypeError):
            Square(5, 7, "2")

    def test_dict_y(self):
        """Expects type int not dict"""
        with self.assertRaises(TypeError):
            Square(10, 2, {})

    def test_list_y(self):
        """Expects type int not list"""
        with self.assertRaises(TypeError):
            Square(2, 8, [])

    def test_tuple_y(self):
        """Expects type int not tuple"""
        with self.assertRaises(TypeError):
            Square(10, 33, ())

    def test_float_y(self):
        """Expects type int not float"""
        with self.assertRaises(TypeError):
            Square(2, 6, 8.9)

    def test_none_x(self):
        """Expects type int not none"""
        with self.assertRaises(TypeError):
            Square(10, None)

    def test_bool_y(self):
        """Expects type int not boolean"""
        with self.assertRaises(TypeError):
            Square(10, 2, False)

    def test_negative_arg_y(self):
        """Expects a int greater than 0"""
        with self.assertRaises(ValueError):
            Square(13, -1)

    def test_dict_x(self):
        """Expects type int not dict"""
        with self.assertRaises(TypeError):
            Square(16, {})

    def test_list_x(self):
        """Expects type int not list"""
        with self.assertRaises(TypeError):
            Square(29, [])

    def test_tuple_x(self):
        """Expects type int not tuple"""
        with self.assertRaises(TypeError):
            Square(10, ())

    def test_float_x(self):
        """Expects type int not float"""
        with self.assertRaises(TypeError):
            Square(12, 8.9)

    def test_negative_x(self):
        """Expects positive int not negative"""
        with self.assertRaises(ValueError):
            Square(10, -3)

    def test_none_x(self):
        """Expects type int not none"""
        with self.assertRaises(TypeError):
            Square(2, None)

    def test_bool_x(self):
        """Expects type int not boolean"""
        with self.assertRaises(TypeError):
            Square(10, False)

    def test_zero_size(self):
        """Expects type int not zero"""
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        """Testing the object's string output"""
        sq13 = Square(7, 4, 3, 16)
        answr = "[Square] (16) 4/3 - 7"
        self.assertEqual(sq13.__str__(), answr)

    def test_id_update(self):
        """Checking if update method works"""
        self.sq35 = Square(3)
        self.sq35.update(90)
        self.assertEqual(self.sq35.id, 90)


if __name__ == "__main__":
    unittest.main()
