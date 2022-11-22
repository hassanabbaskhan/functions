#this is the code to help you know exactly what to order when you go outside for the dine.
#don't fall a prey.

def pizza(small,smallQty,large,largeQty):
    #we will be finding the area of pizza,
    from math import pi
    a=pi
    smallPizzaArea=a*((small/2)**2)*smallQty
    largePizzaArea=a*((large/2)**2)*largeQty

    if smallPizzaArea < largePizzaArea:
        print("Order the large Pizza")
    elif smallPizzaArea == largePizzaArea:
        print("Both the orders are same")
    else:
        print("Order the small pizza")

#now it's time to apply the function....

a=int(input("Enter the size of small pizza  = "))
b=int(input("Enter the Qty of small pizza  = "))
c=int(input("Enter the size of large pizza  = "))
d=int(input("Enter the Qty of large pizza  = "))

pizza(a,b,c,d)
