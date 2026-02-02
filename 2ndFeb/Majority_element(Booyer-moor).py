nums=[3,2,3]
#Booyer-moor solution 
def majorityElement(nums):
    res,count=0,0
    for n in nums:  
        if count==0:
            res=n
        count+=(1 if n==res else -1)
    return res

print(majorityElement(nums))