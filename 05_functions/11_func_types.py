def pure_chai(cups):
    return cups * 10

total_chai = 0

# not recommended 
def impure_chai(cups):
    global total_chai
    total_chai += cups


chai_types = ['light','kadak','ginger','kadak']

strong_chai = list(filter(lambda chai:chai == "kadak",chai_types))

print(strong_chai)
print(chai_types)