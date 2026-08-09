s=input("Enter a string :")
checked=''
for i in range(len(s)):
    if s[i]!=" "and s[i] not in checked:
        count=0
        for j in range(len(s)):
            if s[i]==s[j]:
                count+=1
        print(f"count of {s[i]} is {count}")
        checked+=s[i]