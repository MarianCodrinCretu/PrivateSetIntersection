import csv
import string
import random
import xlsxwriter


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str



def generateFile(n):
    file = open("testFile_"+str(n)+".csv", "a")
    csvWriter = csv.writer(file, lineterminator='\n')
    csvWriter.writerow(['Coloana 1', 'Coloana 2', 'Coloana 3'])

    file.close()

    for i in range(n):
        file = open("testFile_" + str(n) + ".csv", "a")
        csvWriter = csv.writer(file, lineterminator='\n')
        coloana1 = get_random_string(16)
        coloana2 = get_random_string(32)
        coloana3 = get_random_string(50)
        csvWriter.writerow([coloana1, coloana2, coloana3])

        file.close()

# for i in range(11,16):
#     generateFile(int(2**i))

generateFile(512)




