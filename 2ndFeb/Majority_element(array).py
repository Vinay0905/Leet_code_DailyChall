nums=[3,2,3]
#hashmap solution
def majorityElement(num:int)->int:
    coutn={}
    res,max_c=0,0
    for n in nums:
        coutn[n]=1+coutn.get(n,0)
        res=n if coutn[n]>max_c else res
        max_c=max(coutn[n],max_c)
    return res
print(majorityElement(nums))
    