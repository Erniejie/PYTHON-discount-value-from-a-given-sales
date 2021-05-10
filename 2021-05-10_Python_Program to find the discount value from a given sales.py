#Program to find the discount value from a given sales
"Computer Programming Tutor_May 10,2021"

def ComputerDiscount(amt):
    if amt <= 0:
        return 0;
    elif amt <= 1500:
        return amt*0.018;
    elif amt <=2500:
        return amt*0.025;
    elif amt <= 5000:
        return amt*0.056;
    else:
        return amt*0.85;

if __name__=="__main__":

    selling_price = float(input("Enter Selling Price,[£]: "))
    discount=ComputerDiscount(selling_price)

    print("Discount,[£] : {}".format(discount))
