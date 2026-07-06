# chai = 'Ginger chai'

# def prepare_chai(order):
#     print("Preparing ",order)

# prepare_chai(chai)

# -------------------------------------------------------

# chai = [1,2,3]

# def edit_chai(cup):
#     cup[1]=42

# edit_chai(chai)

# print(chai)



def make_chai(tea,milk,sugar):
    print(f"{tea} {milk} {sugar}")

make_chai("Darjeling","Yes","Low") # positional

make_chai(tea = "green",milk="Yes",sugar="Medium")

def add_nums(*nums,**extras): #args ,kwargs
    print("nums ",nums)
    print("extras ",extras)

add_nums(1,2,3,4,special_nu = 12)


# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)

def chai_order(order=None):
    if order is None:
        order = []
    order.append('Masala')
    print(order)

chai_order()
chai_order()



