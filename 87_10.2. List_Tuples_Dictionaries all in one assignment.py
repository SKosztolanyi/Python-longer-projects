#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hourcount = dict()
houremails = list()

for i in handle:
    line = i.rstrip()
    line = line.strip()
    words = line.split() # I needed to create a list of emails with words one by one
    if len(words)<1 : continue # This line excludes all the empty lines. Otherwise, I would get an error of not indexing correctly in empty lines.
    if words[0] != "From": continue # This line of code excludes those lists that don't begin with "From"
    houremails.append(words[5][0:2])

for time in houremails:
    hourcount[time] = hourcount.get(time, 0) + 1
        
frequency = sorted(hourcount.items())
for k, v in frequency:
    print k, v