
def serve_chai():
    chai_type = 'masala' # loca scopt
    print(f"inside function {chai_type} chai")

chai_type = 'Lemon'
print(f"outside function {chai_type} chai")


serve_chai()


# nested functions

def chai_counter():
    chai_order = 'lemon' #enclosing a scope
    def print_order():
        chai_order = 'ginger'
        print(f"Inner {chai_order}")
    print(f"Outer {chai_order}")
    print_order()


chai_order = 'Tulsi' #global scope
print(f"Global {chai_order}")

chai_counter()


