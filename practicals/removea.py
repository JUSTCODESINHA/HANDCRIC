
fp = open(r"C:\Users\IAMNE\OneDrive\Desktop\test.txt","r")
fx = open(r"C:\Users\IAMNE\OneDrive\Desktop\test2.txt","w")
data = fp.readlines()
for i in data:
    if "a" in i:
        fx.write(i)

fp.close()
fx.close()
