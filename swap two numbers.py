#swapping two numbers
x=int(input("enter x value:"))
y=int(input("enter y value:"))
temp=x
x=y
y=temp
print("the value x after swap:",x)
print("the value y after swap:",y)




#def
def num(x,y):
    temp=x
    x=y
    y=temp
    print("the value x after swap:",x)
    print("the value y after swap:",y)
swap=num(5,10)



    
