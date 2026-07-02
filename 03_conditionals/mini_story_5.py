order_amount = input("enter order amount. ")

amount_number_val = int(order_amount)


delivery_fee = 30 if amount_number_val < 300 else 0

print(f"Amount to pay is {amount_number_val+delivery_fee}")