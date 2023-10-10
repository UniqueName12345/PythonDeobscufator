import PythonDeobscufatorBasic
import deobhelper
import os

print("Creating temp file in working directory...")
cwd = os.getcwd()
deobhelper.store_temporary_folder(cwd + "/temp/")
file_path = "deob.py"
if os.path.exists(file_path):
    print("Deleting deob.py to avoid overwriting conflicts...")
    os.remove(file_path)
path = input("What is the path to the software you would like to deobscufate? ")
deob_code = PythonDeobscufatorBasic.deobscufate_file(path)
# save as deob.py
with open("deob.py", "w") as f:
    f.write(deob_code)
print("Saved as deob.py!")
