import os
import sys
from functions.get_files_info import get_files_info, schema_get_files_info
from functions.get_file_content import get_file_content, schema_get_file_content
from functions.write_file import write_file, schema_write_file
from functions.run_python_files import run_python_file, schema_run_python_file
from functions.delete_file import delete_file, schema_delete_file
from functions.create_folder import create_folder, schema_create_folder
from functions.delete_folder import delete_folder, schema_delete_folder
from google import genai
from google.genai import types
from dotenv import load_dotenv
from call_function import call_function

def chat_loop(client, messages, available_functions, config, verbose_flag=False):
    MAX_ITER = 20
    for i in range(0, MAX_ITER):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,
                config=config
            )

            if response is None or response.usage_metadata is None:
                print("Response is malformed")
                return messages

            if verbose_flag:
                print("\nAI Assistant:", response.text)
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            else:
                print("\nAI Assistant:", response.text)

            if response.function_calls:
                function_responses = []
                for function_call in response.function_calls:
                    result = call_function(function_call, verbose=verbose_flag)
                    function_responses.append(types.Content(
                        role="model",
                        parts=[types.Part(text=f"Function {function_call.name} returned: {result}")]
                    ))
                
                messages.extend(function_responses)
                continue

            if response.text:
                messages.append(types.Content(
                    role="model",
                    parts=[types.Part(text=response.text)]
                ))
            
            return messages

        except Exception as e:
            print(f"Error in chat loop: {str(e)}")
            return messages

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
   
    system_prompt = """
You are an advanced AI coding agent with access to a set of file system tools. Your working directory (root) is the current project folder.

Available Tools:
1. File Management:
   - get_files_info: List all files and directories in a specified path
   - get_file_content: Read and display file contents
   - write_file: Create or update files with content
   - delete_file: Remove files from the system

2. Directory Management:
   - create_folder: Create new directories
   - delete_folder: Remove directories
   - list_directory: Show directory contents

3. Code Execution:
   - run_python_file: Execute Python scripts with optional arguments

Important Notes:
- When users mention "root", they are referring to the current working directory (project root)
- All file paths should be relative to the root directory
- Do not use absolute paths
- Create paths using forward slashes (/) even on Windows
- The working directory is automatically handled by the system

Best Practices:
1. Always verify file/directory existence before operations
2. When reading multiple files, process them sequentially
3. Provide clear feedback about actions taken
4. Handle nested directory operations carefully

Example paths:
- "functions/example.py" (correct)
- "./functions/example.py" (correct)
- "/absolute/path/file.py" (incorrect)
- "C:/Windows/file.txt" (incorrect)

For complex operations:
1. First list relevant files/directories
2. Confirm the content or structure
3. Perform the requested modifications
4. Verify the changes
"""

    verbose_flag = "--verbose" in sys.argv

    messages = []

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_write_file,
            schema_run_python_file,
            schema_delete_file,
            schema_create_folder,
            schema_delete_folder,
        ]   
    )

    config = types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt
    )

    print("Welcome to AI Code Agent! Type 'exit' to quit.")
    print("="*50)

    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() in ['exit', 'quit']:
                print("\nGoodbye!")
                break
            
            if not user_input:
                continue

            messages.append(types.Content(
                role="user",
                parts=[types.Part(text=user_input)]
            ))

            messages = chat_loop(client, messages, available_functions, config, verbose_flag)

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}")
            continue

if __name__ == "__main__":
    main()

# import os
# import sys
# from functions.get_files_info import get_files_info, schema_get_files_info
# from functions.get_file_content import get_file_content, schema_get_file_content
# from functions.write_file import write_file, schema_write_file
# from functions.run_python_files import run_python_file, schema_run_python_file
# from functions.delete_file import delete_file, schema_delete_file
# from functions.create_folder import create_folder, schema_create_folder
# from functions.delete_folder import delete_folder, schema_delete_folder
# from google import genai
# from google.genai import types
# from dotenv import load_dotenv
# from call_function import call_function

# def chat_loop(client, messages, available_functions, config, verbose_flag=False):
#     MAX_ITER = 20
#     for i in range(0, MAX_ITER):
#         response = client.models.generate_content(
#             model="gemini-2.0-flash-001",
#             contents=messages,
#             config=config
#         )

#         if response is None or response.usage_metadata is None:
#             print("Response is malformed")
#             return messages

#         if verbose_flag:
#             print("\nAI Assistant:", response.text)
#             print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
#             print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
#         else:
#             print("\nAI Assistant:", response.text)

#         if response.candidates:
#             for candidate in response.candidates:
#                 if candidate is None or candidate.content is None:
#                     continue
#                 messages.append(candidate.content)
        
#         if response.function_calls:
#             for function_call_part in response.function_calls:
#                 result = call_function(function_call_part, verbose=verbose_flag)
#                 messages.append(result)
#         else:
#             return messages

# def main():
#     load_dotenv()
#     api_key = os.environ.get("GEMINI_API_KEY")
#     client = genai.Client(api_key=api_key)
   
#     system_prompt = """
# You are an advanced AI coding agent with access to a set of file system tools. Your working directory (root) is the current project folder.

# Available Tools:
# 1. File Management:
#    - get_files_info: List all files and directories in a specified path
#    - get_file_content: Read and display file contents
#    - write_file: Create or update files with content
#    - delete_file: Remove files from the system

# 2. Directory Management:
#    - create_folder: Create new directories
#    - delete_folder: Remove directories
#    - list_directory: Show directory contents

# 3. Code Execution:
#    - run_python_file: Execute Python scripts with optional arguments

# Important Notes:
# - When users mention "root", they are referring to the current working directory (project root)
# - All file paths should be relative to the root directory
# - Do not use absolute paths
# - Create paths using forward slashes (/) even on Windows
# - The working directory is automatically handled by the system

# Best Practices:
# 1. Always verify file/directory existence before operations
# 2. When reading multiple files, process them sequentially
# 3. Provide clear feedback about actions taken
# 4. Handle nested directory operations carefully

# Example paths:
# - "functions/example.py" (correct)
# - "./functions/example.py" (correct)
# - "/absolute/path/file.py" (incorrect)
# - "C:/Windows/file.txt" (incorrect)

# For complex operations:
# 1. First list relevant files/directories
# 2. Confirm the content or structure
# 3. Perform the requested modifications
# 4. Verify the changes
# """

#     verbose_flag = "--verbose" in sys.argv

#     messages = []

#     available_functions = types.Tool(
#         function_declarations=[
#             schema_get_files_info,
#             schema_get_file_content,
#             schema_write_file,
#             schema_run_python_file,
#             schema_delete_file,
#             schema_create_folder,
#             schema_delete_folder,
#         ]   
#     )

#     config = types.GenerateContentConfig(
#         tools=[available_functions],
#         system_instruction=system_prompt
#     )

#     print("Welcome to AI Code Agent! Type 'exit' to quit.")
#     print("="*50)

#     while True:
#         try:
#             user_input = input("\nYou: ").strip()
            
#             if user_input.lower() in ['exit', 'quit']:
#                 print("\nGoodbye!")
#                 break
            
#             if not user_input:
#                 continue

#             messages.append(types.Content(
#                 role="user",
#                 parts=[types.Part(text=user_input)]
#             ))

#             messages = chat_loop(client, messages, available_functions, config, verbose_flag)

#         except KeyboardInterrupt:
#             print("\nGoodbye!")
#             break
#         except Exception as e:
#             print("\nAn error occurred at main.py.")
#             print(f"\nError: {str(e)}")
#             continue

# if __name__ == "__main__":
#     main()