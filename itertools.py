import os
import itertools 


def scantree(path: str):
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_dir():
                yield entry
                yield from scantree(entry)
            else:
                yield entry
        #     if not entry.name.startswith('.') and entry.is_file():
        #         print(entry.name)


path = r'C:\Users\profsor500\Desktop\python\nauka_samodzielna\zadania treningowe'


listing = scantree(path)

for is_dir, elements in itertools.groupby(listing, key=lambda e: e.is_dir()):
    print('DIR ' if is_dir else 'FILE', len(list(elements)))
