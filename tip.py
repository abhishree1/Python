
bill_amount= int(input("Enter your Billing amount ").replace("$",""))
tip = input("Enter tip i.e15%,18% \or 20%) ").replace("%","")

total_amount = bill_amount+ (bill_amount*(int(tip)/100))
print(f"""Amount to be paid is ${total_amount} .
Thank You for Coming.
Visit Again!""")