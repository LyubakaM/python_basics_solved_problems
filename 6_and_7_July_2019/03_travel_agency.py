town_name = input()
package_type = input()
vip = input()
day_stays = int(input())

price = 0
vip_discount = 1

if day_stays <= 0:
    print('Days must be positive number!')
elif town_name not in "Bansko, Borovets, Varna, Burgas" or \
        package_type not in "noEquipment, withEquipment, noBreakfast, withBreakfast":
    print('Invalid input!')
else:
    if town_name in "Bansko, Borovets":
        if package_type == 'withEquipment':
            price = 100
            if vip == 'yes':
                vip_discount = 0.90
        elif package_type == 'noEquipment':
            price = 80
            if vip == 'yes':
                vip_discount = 0.95
    elif town_name in "Varna, Burgas":
        if package_type == 'withBreakfast':
            price = 130
            if vip == 'yes':
                vip_discount = 0.88
        elif package_type == 'noBreakfast':
            price = 100
            if vip == 'yes':
                vip_discount = 0.93
    if day_stays > 7:
        day_stays -= 1

    total_price = (price * day_stays) * vip_discount
    print(f'The price is {total_price:.2f}lv! Have a nice time!')