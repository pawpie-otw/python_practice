import urllib.request as req
import os

data_dir = r"C:\Users\profsor500\Desktop\python\nauka_samodzielna\zadania treningowe\files"

pages = [

    {'name': 'mobilo',
     'url': 'http://www.mobilo24.eu/'},
    {'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/'},
    {'name': 'kursy',
     'url': 'http://www.kursyonline24.eu/'}]

for page in pages:
    file_name = page['name']+".html"
    try:
        req.urlretrieve(page['url'], data_dir+'/'+file_name)
    except Exception:
        print("blad, exception:", Exception)
else:
    print("wszystkie strony pobrano prawidłowo")
