score = input("Enter Score: ")
s=float(score)
try:
    if (s>0.00 and s<1.0):
        if s<0.6:
            print("F")
        elif (s>=0.9):
            print("A")
        elif(s>=0.8 and s<0.9):
            print("B")
        elif(s>=0.7 and s<0.8):
            print("C")
        else:            #(s>=0.6 and s<0.7):
            print("D")

except:
    if(s>1.0 and s<0.00):
       print("error")