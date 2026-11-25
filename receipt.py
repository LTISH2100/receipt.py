item1_name = "Notebook"
item1_price = float("4.99")#changed to a float
item1_qty = int("2")#changed to an integer

item2_name = "Pen Pack"
item2_price = float("7.50")#changed to a float
item2_qty = int("1")#changed to an integer

item3_name = "Backpack"
item3_price = float("34.99")#changed to a float
item3_qty = int("1")#changed to an integer

tax_rate = float("0.075")   # 7.5% sales tax


item1_total= item1_price*item1_qty
item2_total= item2_price*item2_qty
item3_total= item3_price*item3_qty
subtotal=item2_total+item2_total+item3_total
tax_total=tax_rate*subtotal
grand_total=tax_total+subtotal

print("="*40)
print("STORE RECEIPT")
print("="*40)


print(f"{item1_name}${item1_price}*{item1_qty} {item1_total}")
print(f"{item2_name}${item2_price}*{item2_qty} {item2_total}")
print(f"{item3_name}${item3_price}*{item3_qty} {item3_total}")

print ("-"*40)
print(f"Subtotal: {subtotal:.2f}")
print(f"Tax ({tax_rate * 100}%): ${tax_total:.2f}")

print("="*40)
print(f"TOTAL: {grand_total}")
print("="*40)