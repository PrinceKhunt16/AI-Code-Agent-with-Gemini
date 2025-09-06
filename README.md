# AI Code Agent with Gemini

The `functions` directory contains the following files:

- `delete_file.py`:  Deletes a specified file.
- `get_file_content.py`: Gets the content of a given file.
- `delete_folder.py`: Deletes a specified folder.
- `run_python_files.py`: Runs a specified Python file.
- `get_files_info.py`: Lists files in the specified directory.
- `create_folder.py`: Creates a specified folder.
- `write_file.py`: Writes content to a specified file.

This project provides a coding agent that can be run by executing `main.py`. It allows you to create, update, and delete code, enabling you to make code changes through the agent.

`main.py` serves as the entry point for the coding agent. It likely handles user input, orchestrates the execution of different functions based on the input, and manages the overall workflow of the agent.

`call_function.py` is responsible for calling the appropriate function based on the function name provided. It acts as a dispatcher, routing requests to the correct function in the `functions` directory.
