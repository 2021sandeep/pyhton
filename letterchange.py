#letter change 
def replace(word):
    num_2=""
    for i in word:
        num_2+=chr(ord(i)+1)
    return num_2
word=input()

print(replace("hello"))
