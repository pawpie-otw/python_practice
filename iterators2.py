import csv

file_path = r"C:\Users\profsor500\Desktop\python\nauka_samodzielna\zadania treningowe\files\iterable2.csv"

with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # for row in csvreader:
    #     print('|'.join(row))
    while True:
        try:
            print(next(csvreader))
        except StopIteration:
            print("stop while loop")
            break
