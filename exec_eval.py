import os

files_to_process = [
    "files/math_sin_square.txt",
    "files/math_square_root.txt"
]
dir_path = r"c:\Users\profsor500\Desktop\python\nauka_samodzielna\zadania treningowe"
print(os.getcwd())
for file_name in files_to_process:
    with open(dir_path+'/' + file_name) as f:
        print(os.path.basename(dir_path+'/' + file_name))
        source = "".join(line for line in f.readlines())
    exec(source)
