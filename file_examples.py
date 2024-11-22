from tricks.file_tricks import write_file, read_file

write_file('example.txt', 'Hello, World!')
print("File Contents:", read_file('example.txt'))
