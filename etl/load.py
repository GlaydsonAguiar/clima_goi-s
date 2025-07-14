import csv
import os

def save_to_csv(data, filename='data/clima_goias.csv'):
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)
