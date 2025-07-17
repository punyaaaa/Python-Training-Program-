students = [
{"name":"raju","dept":"css","marks":[20,30,40]},
{"name":"riju","dept":"is","marks":[40,30,90]},
{"name":";punya","dept":"aiml","marks":[80,20,40]},
{"name":"nikki","dept":"is","marks":[10,30,50]}
]
for i in students:
    sum1=sum(i["marks"])
    per=sum1//3
    i["per"]=per


des=["FIRST","SECOND","THIRD","FOURTH","FIFTH"]
b=sorted(students,key=lambda x:x["per"],reverse=True)
index=1
for i in b:
    print("{} {} stands {} : {}%".format(index,i["name"],des[index-1],i["per"]))