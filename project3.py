
#convert 2 patterns of British English to American English 

#open the input file 
with open('hello.txt') as hello_doc:
    hello_content = hello_doc.read()

import re

hello_new1 = re.sub(r"\b(\w{2,})our\b", r"\1or", hello_content) # change words ending with 'our' to 'or'
# print(hello_new1)

hello_new2 = re.sub(r"\b(\w+[aeiou])ll(\w+)\b", r"\1l\2", hello_new1) #for doubled spelling ‘L’ in verbs ending in a vowel plus ‘L’, convert it to single 'l'
print(hello_new2)

#write the output file 
with open("hello_output.txt", "w") as hello_output_doc:
    hello_output_doc.write(str(hello_new2))
