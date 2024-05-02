import unittest
import os
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """Test cases for HBNBCommand"""

    @classmethod
    def setUpClass(cls):
        """Creates a new instance of HBNBCommand for each test method"""
        cls.console = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """Deletes the HBNBCommand instance after all test methods have been run"""
        del cls.console

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Amenity name=\"Wifi\"")
            self.assertIn('Amenity', f.getvalue())
            self.assertIn('Wifi', f.getvalue())

            self.console.onecmd("create State name=\"California\"")
            self.assertIn('State', f.getvalue())
            self.assertIn('California', f.getvalue())

            self.console.onecmd("create City name=\"San Francisco\" state_id=\"CA\"")
            self.assertIn('City', f.getvalue())
            self.assertIn('San Francisco', f.getvalue())
            self.assertIn('CA', f.getvalue())

            self.console.onecmd("create User email=\"test@example.com\" password=\"12345\"")
            self.assertIn('User', f.getvalue())
            self.assertIn('test@example.com', f.getvalue())

            self.console.onecmd("create Place city_id=\"SF\" user_id=\"1\" name=\"My Place\"")
            self.assertIn('Place', f.getvalue())
            self.assertIn('SF', f.getvalue())
            self.assertIn('1', f.getvalue())
            self.assertIn('My Place', f.getvalue())

            self.console.onecmd("create Review place_id=\"123\" user_id=\"456\" text=\"Great place!\"")
            self.assertIn('Review', f.getvalue())
            self.assertIn('123', f.getvalue())
            self.assertIn('456', f.getvalue())
            self.assertIn('Great place!', f.getvalue())

    def test_create_wrong_syntax(self):
        """Test create command with wrong syntax"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

            self.console.onecmd("create UnknownClass")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

            self.console.onecmd("create State name")
            self.assertEqual(f.getvalue(), "** missing attribute name **\n")

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("quit")
            self.assertEqual('', f.getvalue())

    def test_EOF(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_help(self):
        """Test help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            self.assertIn("Documented commands (type help <topic>):", f.getvalue())

            self.console.onecmd("help quit")
            self.assertIn("Quit command to exit the program", f.getvalue())


if __name__ == "__main__":
    unittest.main()
