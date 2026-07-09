

def process_order(item,quantitiy):
    try:
        price = {"masala":20}[item]
        if type(quantitiy) is not int:
            raise TypeError()
        cost = price * quantitiy
        print(f"total cose is {cost}")

    except KeyError:
        print("Sorry that chai is not on menu")
    except TypeError:
        print("Quantity must be in number")

process_order("ginger",1)
process_order("masala","two")
process_order("masala",5)