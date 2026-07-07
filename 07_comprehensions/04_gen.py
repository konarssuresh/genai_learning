
items = (i for i in range(20) if i%2 ==0)

print(items) # it wont give you values. it acts lke stream (will produce next value after yeild)

for even in items:
    print(even)


daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

total_cups = (cups for cups in daily_sales if cups > 5)

total = sum(total_cups)

print(total)

