product =[]
total =[]
def item():
#   ------Input Fuction------
    product.append(input('Enter Your Items : '))
    price=int (input('Enter unit price :'))
    quantity = int(input('Enter item quantity : '))
    total_price = price * quantity
    total.append(total_price)
    print('Total price is :', total_price, 'Tk')

#    ------Add Product----
    ch= input('Anything more (y/n) : ')
    if ch == 'Y' or ch == 'y':
        item()
    elif ch == 'N' or ch == 'n':
        pass

#    -----Item List-----
    list = len(product)
    print('Your',list, 'Item Are',*product)

#     -----Net Total-----

    netprice  = total
    sum1 = sum(total)
    print("Net Total : ", sum1, 'Tk')

#   ------Bill Method-------
    paid =int(input('Enter your amount : '))
    netprice = sum1
    if paid > netprice :
        print('Change amount :',paid-netprice, 'Tk')

    elif paid < netprice:
        print('Less amount :',netprice-paid, 'Tk')

    else:
        print('Thank you ')

    breakpoint()

item()