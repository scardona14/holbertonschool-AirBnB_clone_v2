import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_prompt(self):
        self.assertEqual(self.console.prompt, '(hbnb) ')

    def test_preloop(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.preloop()
            self.assertEqual(fake_out.getvalue().strip(), '(hbnb)')

    def test_precmd(self):
        line = 'create BaseModel'
        self.assertEqual(self.console.precmd(line), line)

        line = 'BaseModel.create()'
        expected = 'create BaseModel'
        self.assertEqual(self.console.precmd(line), expected)

        line = 'BaseModel.create("name", "John")'
        expected = 'create BaseModel "name" "John"'
        self.assertEqual(self.console.precmd(line), expected)

        line = 'BaseModel.create({})'
        expected = 'create BaseModel {}'
        self.assertEqual(self.console.precmd(line), expected)

    def test_postcmd(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.postcmd(stop=False, line='')
            self.assertEqual(fake_out.getvalue().strip(), '(hbnb)')

    def test_do_quit(self):
        with self.assertRaises(SystemExit):
            self.console.do_quit('')

    def test_do_EOF(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_EOF('')
            self.assertEqual(fake_out.getvalue().strip(), '')

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.emptyline()
            self.assertEqual(fake_out.getvalue().strip(), '')

    def test_do_create(self):
        # Add your test cases here
        pass

    def test_do_show(self):
        # Add your test cases here
        pass

    def test_do_destroy(self):
        # Add your test cases here
        pass

    def test_do_all(self):
        # Add your test cases here
        pass

    def test_do_count(self):
        # Add your test cases here
        pass

    def test_do_update(self):
        # Add your test cases here
        pass

if __name__ == '__main__':
    unittest.main()