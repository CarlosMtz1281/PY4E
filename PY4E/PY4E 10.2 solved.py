
#PY4E 10.2 problem solved by me

#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


# Text file sample ===>  http://www.py4e.com/code3/mbox-short.txt

name = "mbox-short.txt"
handle = open(name)

counts = dict()
lis_count = list()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        hour = words[5].split(":")
        hour_num = hour[0]
        counts[hour_num] = counts.get(hour_num, 0) + 1
        
for key, value in counts.items():
    tup = key , value
    lis_count.append(tup)
    
lis_count.sort()

for key, value in lis_count:

    print(key,value)
        