class Solution:
    def totalFine(self, n, date, car, fine):
        l=[]
        for i in range(len(car)):
            
            if date%2==0:
                if car[i]%2!=0:
                    l.append(fine[i])
            elif date%2!=0:
                if car[i]%2==0:
                    l.append(fine[i])
        return sum(l)
      
    