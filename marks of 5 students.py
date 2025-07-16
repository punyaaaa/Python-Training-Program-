import time
names=[]
marks=[]
for i in range(5):
  n=input(f"Enter name of student {i+1}: ")
  names.append(n)
  student_marks=[]
  for j in range(3):
    m=int(input(f"Enter mark {j+1} for {n}: "))
    student_marks.append(m)
  marks.append(student_marks)
  per=[]
  for i in marks:
    total=sum(i)//3
    per.append(total)
time.sleep(1)
for i in range(5):
  print(f"{i+1}. {names[i]}: {per[i]}%")