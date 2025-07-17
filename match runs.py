n=int(input("Enter a number of teams: "))
teams=[]
for i in range(n):
    a=input("Enter team name: ")
    teams.append(a)
meet=int(input("enter num if meeting bw one pair"))
match=[]
for i in range(n-1):
    for j in range(i+1,n):
        for k in range(meet):
            match.append((teams[i],teams[j]))
print("---------------")
index=1
for i in match:
    print(f"Match {index}: {i[0]} vs {i[1]}")
    index+=1
    