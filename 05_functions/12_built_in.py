def chai_flavor(flavor="masala"):
    """ Returns the flavour of chai """
    return flavor

print(chai_flavor.__doc__)
print(chai_flavor.__name__)


def generate_bill(chai=0,samosa=0):
    """
        It calculates the total bil
        for chai and samosa 

        :param chai: number of chai cups
        :param samosa: number of samosas(15 rupees each)
        : return (total amount and thanks message)
    """
    total = chai*10 + samosa*15
    return total,"Thanks"

print(generate_bill.__doc__)