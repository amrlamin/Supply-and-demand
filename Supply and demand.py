#Supply and demand
quantity = 80.00
price = 12.00
print("{0}{1}{2}".format("YEAR", "\tQUANTITY", "\tPRICE"))
for i in range(2014, 2019):
   print("{0:2}\t{1:.2f}\t\t${2:.2f}".format(i, quantity, price))
   quantity = (5 * price) - 10
   price = 20 - (.1 * quantity)