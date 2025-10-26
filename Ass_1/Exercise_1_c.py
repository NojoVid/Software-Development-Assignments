## c) Calculates net and gross price of a property (m²) in € + tax
print('\nHello there!')
area = float(input("What is the area of the property (in m²)? "))
price = 50
tax = 0.035

net_price = area * price
tax_price = net_price * tax
gross_price = net_price + tax_price

output_net = "\nThe property's net cost is " + str(int(net_price)) + "€."
output_gross = "The property's gross cost is " + str(int(gross_price)) + "€, meaning you pay " + str(int(tax_price)) + "€ in taxes.\n"

if area <= 0:
    print('\nYou must enter a valid number!\n')
else:
    print(output_net)
    print(output_gross)