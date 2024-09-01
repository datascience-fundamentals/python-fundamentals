from io import open

# only writing
# texto = "Hola mundo!"
# archivo = open("files/hola-mundo.txt", "w") # open a file with writting mode (w). In this mode all content is replaced
# archivo.write(texto) # It allows you to change the file content with the new text
# archivo.writelines(["linea1\n", "linea2"]) # It allows you to change the file content with the list of text
# archivo.close()


# only reading
# archivo = open("files/hola-mundo.txt", "r") # open a file with reading mode (r)
# file_content = archivo.read() # It allows you to read all file content
# archivo.close()
# print(file_content)

# reading a list
# archivo = open("files/hola-mundo.txt", "r")
# texto = archivo.readlines() # It allows you to get an array of file text lines
# archivo.close()
# print(texto)

# with and seek
# using with, its no longer required to use close method
# with open("files/hola-mundo.txt", "r") as archivo:
#     print(archivo.readlines())
#     # It comes back the pointer to the file's first position,
#     # because above we have used readlines which has read all file content
#     # So, the poiter is currently located in the la last character of the file
#     archivo.seek(0)
#     for linea in archivo:
#         print(linea)

# agregar
# open a file with adding mode (a+)
# archivo = open("files/hola-mundo.txt", "a+")
# archivo.write("\nChao mundo :(")  # It allows you add new content to the file
# archivo.close()

# simultaneous reading and writing
# open a file with reading and writting mode (r+). In this mode the quantity of characters
# which the new content represent, will be replaced.
with open("files/hola-mundo.txt", "r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    archivo.write("linea")
