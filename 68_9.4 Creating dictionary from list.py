## 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the
## greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
## The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
## After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
# text = handle.read() # This is where the problem is
# I created a one long list of words, whereas, I had to have many lists by emails.
allemails = dict()
listemails = list()

for i in handle:
    line = i.rstrip()
    line = line.strip()
    words = line.split() # I needed to create a list of emails with words one by one
    if len(words)<1 : continue # This line excludes all the empty lines. Otherwise, I would get an error of not indexing correctly in empty lines.
    if words[0] != "From": continue # This line of code excludes those lists that don't begin with "From"
    listemails.append(words[1])
    
print listemails # checking if the creation of list was correct

for address in listemails:
	allemails[address] = allemails.get(address, 0) +1
    
print allemails # Checking if i created correct dictionary
  
mostemails = None  
emailcount = None 
for email, count in allemails.items():
    if mostemails is None or emailcount < count:
        mostemails = email
        emailcount = count      
# This for loop returns a key and the biggest value in the dictionary
    
print mostemails, emailcount 
# The result is the most emails from certain address
