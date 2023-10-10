import PythonDeobscufatorBasic

path = input("What is the path to the software you would like to deobscufate?")
try:
    PythonDeobscufatorBasic.deobscufate_python_code(path)
    print("Saved as deob.py!")
except Exception as e:
    print("An error occurred:", e)