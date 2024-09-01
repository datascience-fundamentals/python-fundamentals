import csv
import os

# Writing into csv file
# with open("files/file-test.csv", "w", encoding="utf-8", newline="") as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(["twit_id", "user_id", "text"])
#     writer.writerow([1000, 1, "este es un twit"])
#     writer.writerow([1001, 2, "otro twit!"])

# Reading csv file content
# with open("files/file-test.csv", "r", encoding="utf-8") as archivo:
#     reader = csv.reader(archivo)
#     print(list(reader))
#     archivo.seek(0)
#     for linea in reader:
#         print(linea)

# updating csv file content
with open("files/file-test.csv") as r, open("files/file-temp.csv", "w", newline="") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)

    for linea in reader:
        if linea[0] == "1000":
            writer.writerow([1000, 1, "texto modificado"])
        else:
            writer.writerow(linea)
# os -> this library allows you to remove and rename file
os.remove("files/file-test.csv")
os.rename("files/file-temp.csv", "files/file-test.csv")
