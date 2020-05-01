# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n ==1:
            if isBadVersion(n) == True:
                return 1
        
        currentVersion = int(n/2 + 1)
        L = 1
        R = n
        while R >= L:
            previousVersion = currentVersion
            print(currentVersion)
            if isBadVersion(currentVersion) == True and isBadVersion(currentVersion -1) == False:
                return currentVersion
            
            elif isBadVersion(currentVersion) == True:
                R = currentVersion
                currentVersion = int((L+R)//2)
                
            else:
                L = currentVersion
                currentVersion = int((L+R)//2)
                
            if currentVersion == previousVersion:
                currentVersion += 1
                
