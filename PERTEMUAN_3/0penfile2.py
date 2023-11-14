# Open a file
file1 = open("test.txt", "r")
teks = "Pertemuan 3 "                                                                         

file2 = open("test.txt", "a")
file2.write(teks)
file2.close()

# Read The File
read_content = file1.read()
print(read_content)

# Close the file
file1.close()