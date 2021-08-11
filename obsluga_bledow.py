import requests as req
import os
dirname = os.path.dirname(__file__)

path_i_want = os.path.join(dirname, "files")
print(os.path.exists(path_i_want))
# print(os.path.isfile("files/spis.html"))
# input("type here url:\n")
url = "https://www.python.org/dev/peps/pep-0008/#exception-names"
files_dir = "files"
filename = "mobilo.html"

try:
    content = req.get(url)
except req.exceptions.ConnectionError:
    print("connection error, probably wrong url")

try:
    with open(os.path.join(path_i_want, 'spis.html'), "w") as f:
        f.write("something wrong")
except FileNotFoundError:
    print("Error: file not found")
except PermissionError:
    print("Error: problem with permission with access to file")
except Exception:
    print("ops, unprovided error")

else:
    print("success")
