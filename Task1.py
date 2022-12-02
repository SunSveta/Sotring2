import csv

def get_by_date(date="2017-08-08", name="PCLN", filename='dump3.csv'):
    with open("all_stocks_5yr.csv") as r_file:
        reader = csv.DictReader(r_file)
        for row in reader:
            for i in row:
                if row['date'] == date:
                    if row['Name'] == name:
                        with open(filename, 'a',newline="") as w_file:
                            writer = csv.DictWriter(w_file, fieldnames=row.keys())
                            writer.writerow(row)

print(get_by_date(date="2017-08-08", name="PCLN", filename='dump3.csv'))