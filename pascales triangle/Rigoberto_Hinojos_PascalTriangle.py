from math import factorial
import math


class Rigoberto_Hinojos_PascalTriangle:
  
    
    def pascal(self, num):
       
        list=[]
        
        for i in range(num): 
            newlist=[] 
            for j in range(i + 1):
                newlist.append(int((math.factorial(i)) / ((math.factorial(j)) * math.factorial(i - j))))
            list.append(newlist)
            print(newlist)
        return list
        
            
    def getChoices(self, n,k):
        choice = self.pascal(n)
        row = n-1
        coulmn = k-1
        print("\nYour Number: ")
        print(choice[row][coulmn])
        
       