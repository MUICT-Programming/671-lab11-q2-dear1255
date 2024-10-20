# YOUR CODE HERE
# YOUR CODE HERE
lst1=[]
lst2=[]
n=int(input())
for i in range(n):
    a=int(input())
    lst1.append(a)

for i in range(n):
    a=int(input())
    lst2.append(a)

def summation (a,b):
    lst_sum=[]
    for i in range(len(a)):
        total= a[i]+b[i]
        lst_sum.append(total)
    return lst_sum
lst_sum=summation(lst1,lst2)
def find_min_max(lst_sum):
    min_value=min(lst_sum)
    max_value=max(lst_sum)
    return(min_value,max_value)
lst_sum=summation(lst1,lst2)
print(lst_sum)
print(find_min_max(lst_sum))
