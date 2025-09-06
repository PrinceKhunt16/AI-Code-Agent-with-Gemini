import os
import subprocess
from google.genai import types  

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f"Error: {file_path} is not in the directory."
    
    if not os.path.isfile(abs_file_path):
        return f"Error: {file_path} is not a file."

    if not file_path.endswith(".py"):
        return f"Error: {file_path} is not a Python file."
    
    try:
        final_args = ["python3", file_path]
        final_args.extend(args)
        output = subprocess.run(
            final_args, 
            cwd=abs_working_dir,
            capture_output=True,
            timeout=30
        )

        final_string = f"""
STDOUT: {output.stdout}   
STDERR: {output.stderr}     
"""
        
        if output.stdout == "" and output.stderr == "":
            final_string += f"No output produced. \n"

        if output.returncode != 0:
            final_string += f"Process exited with return code {output.returncode} \n"
    except Exception as e:
        print("Error: This error from run_python_files function.")
        return f"Error: Executing python file {e}"
    
    return final_string

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a specified Python file with Python3 interpreter, Accept the additional .",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to run, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional list of arguments to pass to the Python file.",
            ),
        },   
        required=["file_path"],
    ),
)