
import unittest
from .todo import add_todo, list_todos, remove_todo

class TestTodoFunctions(unittest.TestCase):

    def test_add_todo(self):
        todos = []
        add_todo(todos, "Buy groceries")
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0], "Buy groceries")

    def test_list_todos_empty(self):
        todos = []
        # Capture the output of list_todos
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        list_todos(todos)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "No todos yet!")

    def test_list_todos_not_empty(self):
        todos = ["Buy groceries", "Do laundry"]
        # Capture the output of list_todos
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        list_todos(todos)
        sys.stdout = sys.__stdout__
        expected_output = "1. Buy groceries\n2. Do laundry"
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

    def test_remove_todo(self):
        todos = ["Buy groceries", "Do laundry"]
        remove_todo(todos, "1")
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0], "Do laundry")

    def test_remove_todo_invalid_index(self):
        todos = ["Buy groceries"]
        # Capture the output of remove_todo
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        remove_todo(todos, "2")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Invalid todo index.")

    def test_remove_todo_invalid_input(self):
       todos = ["Buy groceries"]
       # Capture the output of remove_todo
       import io
       import sys
       captured_output = io.StringIO()
       sys.stdout = captured_output
       remove_todo(todos, "abc")
       sys.stdout = sys.__stdout__
       self.assertEqual(captured_output.getvalue().strip(), "Invalid input. Please enter the number of the todo to remove.")


if __name__ == '__main__':
    unittest.main()
