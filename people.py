import csv
import ezgmail

class person():
    def __init__(self, row: list):
        self.__name = row[0]
        self.__address = f'{row[1]}@{row[2]}'

    def send_mail(self, header, message):
        #print(f'You sent {self.__address}: ({header}){message}')
        ezgmail.send(self.__address, header, message)

    def get_name(self):
        return self.__name


def make_people():
    filename = 'people.csv'
    file = open(f'files/{filename}', 'r')
    csv_reader = csv.reader(file, delimiter=',')
    ret = []
    next(csv_reader)
    for row in csv_reader:
        #print(row)
        test_subject = person(row)
        ret = ret + [test_subject]
    file.close()
    #print(ret)
    return ret

