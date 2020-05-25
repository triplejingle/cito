import os
if __name__ == "__main__":
    path = os. getcwd()
    print(path)
    os.chdir('./PythonScripts')
    print(os.system("getTekstEigenschappen.py"))
    os.chdir(path)
