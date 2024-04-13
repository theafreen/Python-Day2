#Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
max = int(input("enter max num"))
odd_num=[]
for i in range(1,max):
  if i%2==1:
    odd_num.append(i)
print(odd_num)

#find-words-containing-character/ leetcode 
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        store=[]
        low=0
        for word in words:
            if x in word:
                store.append(low)
            low+=1
        return store
