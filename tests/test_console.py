#!/usr/bin/python3
"""
Test of console.py
"""
import unittest
from io import StringIO
from console import HBNBCommand
import sys
from os import getenv


class TestConsole(unittest.TestCase):
    """
    test cases
    """
    def setUp(self):
        self.hbtn = HBNBCommand()

    def test_exists(self):
        """
        check process
        """
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)

    @classmethod
    def get_S(cls):
        """
        get stringio
        """
        tempout = StringIO()
        sys.stdout = tempout
        return tempout.getvalue()

    def test_create_error(self):
        """
        test create
        """
        tempout = StringIO()
        sys.stdout = tempout

        self.hbtn.onecmd("create")
        self.assertEqual(tempout.getvalue(), '** class name missing **\n')
        tempout.close()

        tempout = StringIO()
        sys.stdout = tempout
        HBNBCommand().do_create("base")
        self.assertEqual(tempout.getvalue(), '** class doesn\'t exist **\n')
        tempout.close()

        tempout = StringIO()
        sys.stdout = tempout
        if getenv("HBNB_TYPE_STORAGE") != "db":
            HBNBCommand().do_create("BaseModel")
            self.assertTrue(tempout.getvalue() != "")
        tempout.close()
        sys.stdout = sys.__stdout__


if __name__ == "__main__":
    unittest.main()
