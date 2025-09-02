fil2 = open('output.txt','w')
w_data = input("Enter text to write to the file: ")
writing_file = fil2.write(w_data)
print("Data successfully written to output.txt.")
fil2.close()
print('\n')

fil2 = open('output.txt','a')
a_data = input("Enter additional text to append: ")
appending_file = fil2.write(a_data)
print("Data successfully appended.")
fil2.close()
print('\n')

fil2 = open('output.txt','r')
r_file1 = fil2.read()
print("Final content of output.txt:")
r_file2 = fil2.readline()

print(w_data)
print(a_data)

fil2.close()