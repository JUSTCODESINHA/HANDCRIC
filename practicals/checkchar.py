
fp = open(r"C:\Users\IAMNE\OneDrive\Desktop\test.txt","r")
data = fp.read()


cnt_vowel = 0
cnt_consonents = 0
cnt_uppercase = 0
cnt_lowercase = 0

for char in data:
    if char in "aeiouAEIOU":
        cnt_vowel += 1
    else:
        cnt_consonents += 1
    
    if char.isupper():
        cnt_uppercase += 1
    else:
        cnt_lowercase += 1

    

print("TOTAL CONSONENTS =>",cnt_consonents)
print("TOTAL VOWELS =>",cnt_vowel)    
print("TOTAL UPPERCASE CHARACTERS =>",cnt_uppercase)
print("TOTAL LOWERCASE CHARACTERS =>",cnt_lowercase)



fp.close()
