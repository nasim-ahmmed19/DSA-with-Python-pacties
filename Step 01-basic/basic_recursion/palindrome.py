def palindrome(s,l,r):
    if l>=r:
        return True
    if s[l]!=s[r]:
        return False
    return palindrome(s,l+1,r-1)

s="malayalam"
print(palindrome(s,0,len(s)-1)) #TC=O(N)   SC=O(N)