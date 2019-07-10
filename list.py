list =[]
list.append('a')
print(list)

def even(min,max):
    list=[]
    
    for a in range(min,max):
        if  a % 2 ==0: 
            list.append(a)
            
              
    return list

values = even(2,10)
print(values)
values = even(3,15)
print(values)
values = even(2,8)
print(values)
values = even(25,100)
print(values)
print(100,200)
