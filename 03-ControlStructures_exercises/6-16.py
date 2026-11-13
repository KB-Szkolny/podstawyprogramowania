###
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#
washing_product = input("Select washing program: (j)acket, (u)nderwear, (s)hoes ")
rinse = input("Extra rinse? (y/n) ")
spin = input("Extra spin? (y/n ")

washing_time = 0

if washing_product == 'j' or washing_product == 'J':
    washing_time += 40
    washing_product = 'Jacket'
if washing_product == 'u' or washing_product == 'U':
    washing_time += 70
    washing_product = 'Underwear'
if washing_product == 's' or washing_product == 'S':
    washing_time += 20
    washing_product = 'Shoes'
else:
    print("Wrong character typed!")


if rinse == 'y' or rinse == 'Y':
    rinse = True
    spin = False
    washing_time += 15
elif spin == 'y' or spin == 'Y':
    spin = True
    rinse = False
    washing_time += 9
else:
    print("Wrong character typed!")

print(f'Washing product: {washing_product}')
print(f'Rinse: {rinse}')
print(f'Spin: {spin}')
print(f'Total washing time: {washing_time}')