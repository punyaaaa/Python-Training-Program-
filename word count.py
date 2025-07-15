import time 
str1 = input("enter a sentence: ")
c=0
for i in range(len(str1)):
    if str1[i]==" " and str1[i-1]!=" ":
        c=c+1
time.sleep(1)
print("Number of words in the sentence:", c+1)