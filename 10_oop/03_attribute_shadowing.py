# same like prototype chaining in javascript (objects fallback is class)

class Chai:
    temperature = 'hot'
    strength = 'Strong'

cutting = Chai()

print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = 'small'

print(f"After changing {cutting.temperature}")
print(f"Direct look into class {Chai.temperature}")
print(f"cup size is {cutting.cup}")

del cutting.temperature
del cutting.cup

print(f"After deleting {cutting.temperature}")
print(f"Direct look into class {Chai.temperature}")
print(f"cup size is {cutting.cup}")