import csv

with open("custcontact.csv", "r") as csvfile :
    custcontact_reader = csv.reader(csvfile)
    for mycust in custcontact_reader :
        print(mycust)