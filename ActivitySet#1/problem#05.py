def computepay(h, r):
           if h>40:
                pay=h*r+(0.5)*r*(h-40)
                
           else:
                   pay=r*h
           return pay   
                
hrs = input("Enter Hours:")
h=float(hrs)
r=float(input("Enter Rate:"))

pay= computepay(h,r)
print("Pay", pay)