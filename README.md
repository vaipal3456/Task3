file1 = open('sample.txt1', 'r')
reading_file = file1.read()
print(reading_file)

file1.close()


file1 = open('Output.txt','w')
writing_file = file1.write('Hello, Python!')
print(writing_file)
file1.close()

file1 = open('Output.txt','a')
appending_file = file1.write('\nLearning file handling in python')
file1.close()

file1 = open('Output.txt','r')
reading_file = file1.read()
print(reading_file)
file1.close()
