class Solution:
    def findUnion(self, a, b):
        arr=[]
        i,j=0,0
        n,m=len(a),len(b)
        while i<n and j<m:
            if a[i]<=b[j]:
                if not arr or arr[-1]!=a[i]:
                    arr.append(a[i])
                i+=1
            else:
                if not arr or arr[-1]!=b[j]:
                    arr.append(b[j])
                j+=1
        if i<n:
            while i<n:
                if not arr or arr[-1]!=a[i]:
                    arr.append(a[i])
                i+=1
        if j<m:
            while j<m:
                if not arr or arr[-1]!=b[j]:
                    arr.append(b[j])
                j+=1
        return arr # TC: O(n+m) SC: O(n+m)

a=[1, 2, 3, 4, 5]
b=[1, 2, 3, 6, 7]
obj=Solution()
print(obj.findUnion(a,b))