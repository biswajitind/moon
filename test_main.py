import unittest
from hello_oop import Greeter

class TestGreeter(unittest.TestCase):

    def test_default_greeting(self):
        """Test that the default greeting is 'Hello, World!'."""
        g = Greeter()
        self.assertEqual(g.greet(), "Hello, World!")

    def test_custom_greeting(self):
        """Test greeting with a custom name."""
        g = Greeter("Biswajit")
        self.assertEqual(g.greet(), "Hello, Biswajit!")


if __name__ == "__main__":
    unittest.main()
