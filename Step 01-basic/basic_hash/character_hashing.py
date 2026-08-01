s='Character Hashing is a technique used to count the frequency of characters in a string efficiently. Instead of searching through the string multiple times, we pre-process the string and store the frequency of each character in a Hash Table or Array.'
m=['a','e','i','o','u','z',' ','.','t','h','s']

class character_hash:
    def __init__(self,s,m):
        self.s=s
        self.m=m
        self.hash_list=[0]*256

    def counter(self):
        for i in self.s:
            self.hash_list[ord(i)]+=1

        for j in self.m:
            print(f'{j} occurs in string :{self.hash_list[ord(j)]} times')

obj=character_hash(s,m) #TC=O(N+M)   SC=O(256)
obj.counter()