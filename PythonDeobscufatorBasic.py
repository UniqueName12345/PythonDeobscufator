import string2listhelper
import deobhelper

def get_contents_of_file(file_path):
    with open(file_path, "r") as f:
        code = f.read()
    return code

def deobscufate_file(file_path):
    code = get_contents_of_file(file_path)
    # First, take the code and delete the last line (simply a wrapper to actually launch the code)
    code = code[:-1]
    # then, extract the list from the list definition string
    list = string2listhelper.extract_list_from_def_list(code)
    # split the list by a comma
    list = list.split(",")
    # then, take every element of the list and turn it into a chr() of the element
    deobscufated_code = deobhelper.chr_ify_list(list)
    # finally, return the deobscufated code
    return deobscufated_code