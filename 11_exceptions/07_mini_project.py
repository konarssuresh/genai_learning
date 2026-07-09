class InvalidChaiError(Exception):
    pass

def bill(flavor,cups):
    menu = {'masala':20,'ginger':40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("flavor not available")
        if  not isinstance(cups,int):
            raise TypeError("cups should be of type int")
        total = menu[flavor] * cups

        print(f"Bill for {cups} cups of {flavor} chai is {total} rupees")
            
    except Exception as e:
        print("error - ", e)

    finally:
        print("Thank you for visiting shop !!!")


bill("mint",2)
bill("masala","three")
bill("ginger",3)