# def serve_chai():
#     yield "Cup1: Masala chai"
#     yield "Cup2: Ginger chai"
#     yield "Cup3: Elaichi chai"

# stall = serve_chai()

# for cup in stall:
#     print(cup)


def get_chai_list():
    return ['cup1','cup2','cup3']

def get_chai_gen():
    yield "cup1"
    yield "cup2"
    yield "cup3"

chai = get_chai_gen()

print(next(chai))
print(next(chai))

for ch in chai:
    print(ch)

for ch in chai:
    print(ch)

for ch in chai:
    print(ch)