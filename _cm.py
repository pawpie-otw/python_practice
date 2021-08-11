import os
import zipfile
import requests
import contextlib as cl


class FileFromWeb:

    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def download_file(self):
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self

    def close(self):
        # if os.path.isfile(self.tmp_file):
        os.remove(self.tmp_file)


with cl.suppress(FileNotFoundError):
    with cl.closing(FileFromWeb(
            'https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip',
            'c:/temp/euroxref1.zip')) as ffw:
        ffw.download_file()

        with zipfile.ZipFile(ffw.tmp_file, 'r') as z:
            a_file = z.namelist()[0]
            print(a_file)
            os.chdir('c:/temp')
            z.extract(a_file, '.', None)

    os.remove(ffw.tmp_file)
