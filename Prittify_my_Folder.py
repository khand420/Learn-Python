import os

def soldier(path, file, format):
    os.chdir(path)
    i = 1
    files = os.lisdir(path)
    with open(file) as f:
        filelist - f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize()) 

    if os.path.splitext(file)[1] == format:
        os.rename(file, f"{i} format")
        i += 1

soldier(r"C:\Users\Danish khan\Desktop\E-Commerce\Static",r"E:\CODE\python\LEARN PYTHON\khamd.txt",".png")