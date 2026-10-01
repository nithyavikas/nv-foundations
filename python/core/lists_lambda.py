nums = [1,2,3,4,5]
print("nums",nums)
'''
y=[]
for x in nums:
    y.append(x**2)
print(y)
'''

def square(x):
    z=[]
    for x in nums:
        if x % 2 == 0:  # Even numbers
            z.append(x ** 2)
    #print(z)
    return z
print(square(nums))


print(list(map(lambda x:x*2, nums)))
print(list(filter(lambda x:x>2, nums)))
print(list(map(lambda x:x**2, list(filter(lambda x:x%2==0,nums)))))
