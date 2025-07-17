from datetime import datetime
a=input("Enter the first  date in dd/mm/yyyy format: ")
b=input("Enter the second date in dd/mm/yyyy format: ")
d1=datetime.strptime(a, "%d/%m/%Y")
d2=datetime.strptime(b, "%d/%m/%Y") 
diff=d2-d1
print("difference:",abs(diff.days), "days")