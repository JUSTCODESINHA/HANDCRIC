fp = open(r"C:\Users\IAMNE\OneDrive\Desktop\test.txt","r")
data = fp.readlines()

for sentences in data:
    for character in sentences:
        if character == ' ':
            print("#",end="")
        else:
            print(character,end="")

fp.close()

