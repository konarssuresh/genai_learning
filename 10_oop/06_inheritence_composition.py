class BaseChai:
    def __init__(self,type_):
        self.type = type_
        
    def prepare_chai(self):
        print(f"Preparing {self.type} chai....")

class MasalaChai(BaseChai):
    def __init__(self, type_):
        super().__init__(type_)

    def add_spices(self):
        print("Adding cardmom, ginger and clove")

# composition
class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare_chai()
    
class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai


shop = ChaiShop()
fancy = FancyChaiShop()

shop.serve()
fancy.serve()
fancy.chai.add_spices()

