hrs = input("Enter Hours:")
h = float(hrs)
rate=input("enter rate:")
r= float(rate)
print(h,r)
if h<=40:
    rp= h*r
    print(rp)
else:
    otp=40*r+(h-40)*r*1.5
    print(otp)