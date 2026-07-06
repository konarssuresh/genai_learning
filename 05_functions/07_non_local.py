chai_type= 'Ginger'

def update_order():
    chai_type = 'Elaichi'
    def kitchen():
        nonlocal chai_type # accessing from parent scope
        chai_type = 'Kesar'
    kitchen()
    print(f"after kitchen update {chai_type}")

update_order()