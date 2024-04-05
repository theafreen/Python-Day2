#Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
max = int(input("enter max num"))
odd_num=[]
for i in range(1,max):
  if i%2==1:
    odd_num.append(i)
print(odd_num)
