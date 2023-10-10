import shutil
import concurrent.futures
import os

def create_temp_folder():
    """
    Creates a temporary folder in the current working directory.

    Returns:
        str: The path of the newly created temporary folder.
    """
    temp_folder = os.path.join(os.getcwd(), "temp")
    os.makedirs(temp_folder, exist_ok=True)
    return temp_folder

def copy_file_to_temp(file_path, temp_folder):
    """
    Copy a file to a temporary folder.

    :param file_path: The path of the file to be copied.
    :type file_path: str
    :param temp_folder: The path of the temporary folder.
    :type temp_folder: str
    :return: The path of the copied file in the temporary folder.
    :rtype: str
    """
    temp_file_path = os.path.join(temp_folder, os.path.basename(file_path))
    shutil.copyfile(file_path, temp_file_path)
    return temp_file_path

def remove_last_line(file_path):
    """
    Remove the last line from the file located at the specified file path.

    Parameters:
        file_path (str): The path to the file.

    Returns:
        None
    """
    with open(file_path, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        file.writelines(lines[:-1])

def find_code_start_line(file_path):
    """
    Finds the starting line of code in the specified file.

    Parameters:
        file_path (str): The path to the file to be searched.

    Returns:
        int: The line number where the code starts.
    """
    code_start = None
    with open(file_path, "r") as file:
        for i, line in enumerate(file):
            if "code = [" in line:
                code_start = i + 1
                break
    code_start -= 1  # Exclude the final ']'
    return code_start

def strip_outer_layers(file_path, code_start):
    """
    Given a file path and a code start index, this function reads the content of the file and returns a list of code lines starting from the code start index.

    Args:
        file_path (str): The path to the file to read.
        code_start (int): The index of the first line of code to include in the result.

    Returns:
        list: A list of code lines starting from the code start index.
    """
    code = []
    with open(file_path, "r") as file:
        for i, line in enumerate(file):
            if i >= code_start:
                code.append(line.strip())
    return code

def convert_to_chr(element):
    """
    Convert an element to its corresponding character representation.

    Parameters:
        element (int): The element to be converted.

    Returns:
        str: The character representation of the element.
    """
    return chr(int(element))

def convert_code_to_string(code):
    """
    Converts a list of codes to a string representation.
    
    Args:
        code (list): A list of codes to be converted.
        
    Returns:
        str: The string representation of the codes.
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(convert_to_chr, code)
        code = list(results)
    code_string = "".join(code)
    return code_string

def save_deobfuscated_file(code_string):
    """
    Saves the deobfuscated code to a file.

    Parameters:
        code_string (str): The deobfuscated code to be saved.

    Returns:
        None
    """
    deob_file_path = os.path.join(os.getcwd(), "temp", "deob.py")
    with open(deob_file_path, "w") as file:
        file.write(code_string)
    shutil.move(deob_file_path, os.path.join(os.getcwd(), "output", "deob.py"))

def delete_temp_folder():
    """
    Deletes the temporary folder.

    This function deletes the temporary folder created during the execution of the program.

    Parameters:
        None

    Return:
        None
    """
    shutil.rmtree(os.path.join(os.getcwd(), "temp"))

def deobfuscate_file(file_path):
    """
    Deobfuscates a file by performing the following steps:
    1. Creates a temporary folder.
    2. Copies the specified file to the temporary folder.
    3. Removes the last line from the temporary file.
    4. Finds the line number where the code starts in the temporary file.
    5. Strips the outer layers of the code from the temporary file starting from the code start line.
    6. Converts the code to a string.
    7. Saves the deobfuscated code as a file.
    8. Deletes the temporary folder.

    Parameters:
        file_path (str): The path of the file to be deobfuscated.

    Returns:
        None
    """
    temp_folder = create_temp_folder()
    temp_file_path = copy_file_to_temp(file_path, temp_folder)
    remove_last_line(temp_file_path)
    code_start = find_code_start_line(temp_file_path)
    code = strip_outer_layers(temp_file_path, code_start)
    code_string = convert_code_to_string(code)
    save_deobfuscated_file(code_string)
    delete_temp_folder()