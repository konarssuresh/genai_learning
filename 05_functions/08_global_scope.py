chai_type = 'Plain'

def front_desk():
    def kitchen():
        global chai_type # looking for global variable
        chai_type = 'Masala'
    kitchen()

front_desk()

print(f"After update - {chai_type}")