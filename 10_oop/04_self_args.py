class Chaicup:
    size = "150" #ml

    def describe(self):
        return f"this is cup or size {self.size}ml"


cup = Chaicup()
print(cup.describe())

print(Chaicup.describe(self=cup))