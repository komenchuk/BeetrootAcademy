# Создаем новый файл и делаем в нём запись
f = open('myfile.txt', 'w')
f.write('Hello file world!')
f.close()

# Открываем файл на чтение
f = open('myfile.txt', 'r')
f.close()