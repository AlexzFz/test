message = "Hello, world!"

# Вывести сообщение в консоль
print(message)

# Записать сообщение в файл
with open("output.txt", "w") as file:
    file.write(message)
