#PY4E 8.5 Solved by me 

#Instructions: Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

# Text file sample ===>  http://www.py4e.com/code3/mbox-short.txt



fname = "mbox-short.txt"

fh = open(fname)
number = 0
for line in fh:
   
    if line.startswith("From "):
 #Notice the space after the word from to avoid any line starting in "From:"
        words = line.split()
        print(words[1])
        number = number + 1
        continue
 
print("There were", number, "lines in the file with From as the first word")
