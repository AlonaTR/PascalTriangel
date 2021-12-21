words=input("Enter the words: ")
words=words.split()
print(words)

list=[]
list.append([words[0]])
# print(list)
for letter in range(1,len(words)):
    if words[letter] == words[letter-1]:
        list[-1].append(words[letter])

    else:
        list.append([words[letter]])
        
    
        
print(list)