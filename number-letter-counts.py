names = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"forteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",100:"hundred",1000:"thousand"}

num_list = []
letter_list = []
letters = 0
for i in range(1,1000):
    if i <= 20:
        word = names[i]
        num_list.append(i)
        letter_list.append(len(word))
        letters += len(word)
    elif i%10 == 0:
        if i < 100:
            word = names[i]
            num_list.append(i)
            letter_list.append(len(word))
            letters += len(word)

print(num_list)
print(letter_list)

print(letters)
        
         
