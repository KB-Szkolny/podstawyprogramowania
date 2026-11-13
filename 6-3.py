###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = input('Is the first light switch on? (Y/N): ')
light_switch2 = input('Is the second light switch on? (Y/N): ')

if light_switch1 == 'Y' or light_switch1 == 'y':
    light_switch1 = True
else:
    light_switch1 = False

if light_switch2 == 'Y' or light_switch2 == 'y':
    light_switch2 = True
else:
    light_switch2 = False

bulbs_on = 0

if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 2
# if light_switch1 and light_switch2:
#     bulbus_on = 3
print(f'Active light bulbs: {bulbs_on}')