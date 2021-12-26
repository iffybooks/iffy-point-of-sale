# Iffy Point of Sale

A minimal point-of-sale script using Python and a barcode scanner. 

Use the command `python3 iffy_books_point_of_sale.py` to launch the script. Use a barcode scanner (such as a modified CueCat) to enter ISBNs, then type 'done'. Enter items and prices manually, then type 'done'. Then you can enter a payment payment type (optional) and choose whether to save the transaction to a CSV file.

You'll need to read through the code and adapt it for your needs. This script looks for a file called `Iffy_Books_Inventory.csv` in your Documents directory, and saves transaction records to the directory `~/Documents/Iffy_Books_POS_Transactions/`.
