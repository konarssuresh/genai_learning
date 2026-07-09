class Chai:
    origin = 'India'


Chai.is_hot = True
print(Chai.origin)
print(Chai.is_hot)

# creating objects from class chai

masala = Chai()

print(f"Masals origin {masala.origin}")
print(f"Masala is_hot {masala.is_hot}")


masala.is_hot = False
masala.origin = "China"

print(f"Masals origin {masala.origin}")
print(f"Masala is_hot {masala.is_hot}")

print(Chai.origin)
print(Chai.is_hot)

masala.flavor = "Mint"

print(masala)