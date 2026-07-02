# strings
chai_type = "ginger chai"
customer_name = "Suresh"

print(f"Order for {customer_name} : {chai_type} please")

chai_description = "Aromatic and Bold"

print(f"First word: {chai_description[0:8:1]}")
print(f"Last Word :{chai_description[12:]}")
print(f"last word :{chai_description[::-1]}")

label_text  = "Chai SpEÊcial"
encoded_label = label_text.encode("utf-8")
print(f"Encoded label:{encoded_label}")
print(f"non encoded label : {label_text}")
decoded_label = encoded_label.decode("utf-8")
print(f"decoded encoded label {decoded_label}")