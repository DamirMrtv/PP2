class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum1=0
        sum2=1
        for i in range(6):
            if n<=0:
            break
                
            sum1+=n%10
            sum2*=n%10
            
            n//=10
            
        return sum2-sum1