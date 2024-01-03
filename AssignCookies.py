class Solution(object): #Creating a class
    def findContentChildren(self, g, s): #Creating a function
        g.sort()
        s.sort()
        i=0
        j=0
        while i<len(g) and j <len(s):
            if s[j]>=g[i]:
                i+=1
            j+=1
        return i 

obj= Solution() #Creating object of class
g = [1,2,3]
s = [1,1]
print(obj.findContentChildren(g,s)) #passing two arrays as arguments 