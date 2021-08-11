import requests
import os
import shutil


def save_url_to_file(url, file_path):

    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)


url = 'http://www.mobilo24.eu/spis/'
dir = 'c:/temp/'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    os.path.isfile(tmpfile_path) and os.remove(
        tmpfile_path)
    save_url_to_file(url, tmpfile_path)
    shutil.copy(tmpfile_path, file_path)
except Exception as e:
    print("error:", e)
else:
    print("success")
finally:
    os.path.isfile(tmpfile_path) and os.remove(
        tmpfile_path) and print(f"{tmpfile_path} removed!")
