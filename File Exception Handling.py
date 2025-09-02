try:
   fil1 = open('sample.txt','r')
   read_line1 = fil1.readline()
   print("Reading file content: ")
   print("Line 1: ",read_line1)
   read_line2 = fil1.readline()
   print("Line 2: ",read_line2)
   fil1.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")