from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt # читает опции командной строки
import sys # достур к опциям


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", 'file']) #n=amount, f=file
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2) # регулярное выражение getopt


n = 5
f = "data/contacts.json"

for o, a in opts: #картежи размерности 2(опции)
    if o == "-n":
        n = int(a) #берется значение опции и преобразуется в число? опция n
    elif o == "-f":
        f = a #путь к файлу хранится строкой  /  для использования генератора в параметрах скрипта указать (прим) -n 10 -f data/test.json


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Contact(lname=random_string("lname", 8), name=random_string("name", 4), work=random_string("workphone", 5))
             for i in range(5)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)

with open(file, "w") as out: #записываем в файл/ режим "w"==write
    jsonpickle.set_encoder_options("json", indent=2) #indent форматирует текст
    out.write(jsonpickle.encode(test_data))