name = ["theon","edmund","daeron","alicent"]
total = [12,34,234,432]


for i in range(len(name)):
    print(f"{name[i]} paid {total[i]}")

print("--------------------------------")

for current_name, current_total in zip(name,total):
    print(f"{current_name} paid {current_total}")