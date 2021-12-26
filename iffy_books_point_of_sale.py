import csv
import os
from pprint import pprint
from datetime import datetime

print('\n'*200)
print("    ✨ Thanks for visiting Iffy Books! ✨")
print("            https://iffybooks.net")
print('\n'*4)

## Load inventory CSV file as a list of lists
inventory_lol = []
with open(os.path.expanduser("~/Documents/Iffy_Books_Inventory.csv")) as fi:
	csv_reader = csv.reader(fi)
	for row in csv_reader:
		inventory_lol.append(row)

## Remove CSV header
inventory_lol = inventory_lol[1:]

## Create title and price dictionaries
title_dict = {}
price_dict = {}
for row in inventory_lol:
	title = row[0]
	product_codes = [item.strip() for item in row[2].split("\n")]
	try:
		price = float(row[8])
	except:
		print("Error:")
		price = -1
		print(row[8])
		print(row)

	for code in product_codes:
		title_dict[code] = title
		price_dict[code] = price


## Initialize list of lists for the current transaction
transaction_lol = []

## Enter ISBN codes using barcode scanner
print("** Find price by ISBN **")
print("Type 'done' to finish.")
while True:
	barcode = input("Enter an ISBN: ")
	barcode = barcode.split(' ')[0]
	if barcode == "done":
		break
	elif barcode != "":
		
		try:
			print()
			title = title_dict[barcode]
			print(">> Title: " + title)
			price = price_dict[barcode]
			print(">> Price: $" + str(price).zfill(2))
			row = [title, barcode, price]
			transaction_lol.append(row)
			print()
		except:
			print("\nThat ISBN wasn't found. Enter the price manually instead.\n")

## Enter prices manually
print("\n\n** Enter prices manually **")
print("Type 'done' to finish.")
while True:
	title = input("Enter the title/item: ")
	if title == "done":
		break
	
	price = float(input("Enter the price: "))
	barcode = ""
	row = [title, barcode, price]
	transaction_lol.append(row)
	print()


## Print transaction details
print("\n"*20)
for row in transaction_lol:
	print ("  ".join([str(item) for item in row]))

## Calculate subtotal
subtotal = 0
for title, barcode, price in transaction_lol:
	subtotal += price

subtotal = round(subtotal, 2)

# Calculate total with sales tax
total_with_tax = subtotal*1.08
total_with_tax = round(total_with_tax, 2)

## Add subtotal and total to transaction list of lists
transaction_lol.append(["","Subtotal:", subtotal])
transaction_lol.append(["","Total with tax:", total_with_tax])


## Print total and subtotal
print()
print("*"*50)
print("Subtotal: $" + str(subtotal).zfill(2))
print("Total with tax: $" + str(total_with_tax).zfill(2))
print("*"*50)
print()


## Enter payment type
payment_type = input("Payment type: ")
transaction_lol.append(["","Payment type: ", payment_type])


## Save transaction to CSV file
csv_filename = "Transaction_" + str(datetime.now())[:-7].replace(' ',"_").replace(':',".") + ".csv"
csv_path = os.path.join(os.path.expanduser("~/Documents/Iffy_Books_POS_Transactions/"), csv_filename)

save_input = input("\nType 'save' to save: ")
if save_input.lower() == 'save':
	with open(csv_path, 'w') as fo:
		csv_writer = csv.writer(fo)
		csv_writer.writerows(transaction_lol)
		print("Saved to CSV!")
