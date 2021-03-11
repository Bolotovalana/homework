# 3. Написать генератор, который будет принимать на вход имя файла
# и генерировать построчно(т.е yield каждой строки).

def read_file(file_name):
    for row in open(file_name, "r"):
        yield row


str_row = read_file("file.txt")
print(str_row.__next__())
print(str_row.__next__())
print(str_row.__next__())