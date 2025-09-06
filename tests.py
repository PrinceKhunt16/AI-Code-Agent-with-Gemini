from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_files import run_python_file

def files_info_test():
    working_dir = "calculator"

    root_contents = get_files_info(working_dir)
    print(root_contents)

    pkg_content = get_files_info(working_dir, "pkg")
    print(pkg_content)

    bin_content = get_files_info(working_dir, "/bin")
    print(bin_content)

    back_content = get_files_info(working_dir, "../")
    print(back_content)

# files_info_test()

def file_content():
    working_directory = "calculator"
    print(get_file_content(working_directory, "lorem.txt"))
    print(get_file_content(working_directory, "main.py"))
    print(get_file_content(working_directory, "pkg/calculator.py"))
    print(get_file_content(working_directory, "/bin/cat"))

# file_content()

def write_test():
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

# write_test()

def run_python_file_test():
    working_directory = "calculator"
    print(run_python_file(working_directory, "main.py", "3 + 4"))
    print(run_python_file(working_directory, "tests.py"))
    print(run_python_file(working_directory, "../main.py"))
    print(run_python_file(working_directory, "nonexist.py"))

# run_python_file_test()