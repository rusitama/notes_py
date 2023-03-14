from Note import *
import os
import csv
os.system('cls')

db_file = 'Notes.csv'

def init_data_base():
    if os.path.exists(db_file):
        open(db_file, 'r', newline='')
        #with open(db_file, 'r', newline='') as csv_file:
        #    reader = csv.reader(csv_file)
        #    for row in reader:
        #        a = 0
    else:
        open(db_file, 'w', newline='').close()

def importFromFile():
    notes = []
    with open('Notes.csv', 'r') as f:
        reader = csv.reader(f, delimiter=";")
        for row in reader:
            note = Note(row[0], row[1], row[2], row[3])
            notes.append(note)
    print("Notes imported!")
    return notes

def writeToFile(notes):
    if (len(notes) > 0):
        with open('Notes.csv', 'w') as f:
            writer = csv.writer(f, delimiter=";", lineterminator="\r")
            for x in notes:
                writer.writerow([x.title, x.body, x.date, x.id])
        print("Notes saved!")
    else:
        print("Notes are empty!")