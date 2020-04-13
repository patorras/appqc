import csv
from datetime import date
import datetime


#- Um caixa de texto onde o registar o batch

#- Uma caixa de texto para registar se é “registo de amostra” ou “saída de amostra” (in – out).

filename = "data.csv"

answer = ""

# all the data fieldnames
table = {"date": datetime.datetime.now(), "batch": "", "moment": ""}

col = ["date", "batch", "moment"]


while answer != "n":

    table["moment"] = input("Do you want to register in or out sample? ")

    table["batch"] = input("Please insert the batch? ")


    with open(filename, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=col)

        # write headers if necessary
        #writer.writeheader()

        # write the rows
        writer.writerow(table)
    answer = input("Do you want to add more batchs? (type y for more or n to exit) ")
    print("---------------------\n")
