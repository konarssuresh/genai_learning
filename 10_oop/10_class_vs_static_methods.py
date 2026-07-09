class ChaiOrder:
    def __init__(self,tea_type,sweetness,size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data['tea_type'],
            order_data['sweetness'],
            order_data['size']
        )
    
    @classmethod
    def from_string(cls,order_string):
        tea_type, sweetness,size = order_string.split("-")
        return cls(tea_type,sweetness,size)
    
class ChaiUtils:
    @staticmethod 
    def is_valid_size(size):
        return size.lower() in ["small",'medium','large']
    
order = ChaiOrder.from_string("Masala-Medium-Cutting")

order2 = ChaiOrder.from_dict({"tea_type":"Herbal","sweetness":"High","size":"Large"})

order3 = ChaiOrder("Iced","High","Large")

print(order.__dict__)

print(order2.__dict__)

print(order3.__dict__)

print(ChaiUtils.is_valid_size("medium"))