name = input()
adult_ticket_num = int(input())
child_ticket_num = int(input())
net_adult_price = float(input())
service_tax = float(input())

net_kid_ticker = net_adult_price - (net_adult_price * 0.70)
adult_price_tax = net_adult_price + service_tax
kid_price_tax = net_kid_ticker + service_tax
total_tickets = (child_ticket_num * kid_price_tax) + (adult_ticket_num * adult_price_tax)
profit = total_tickets * 0.2

print(f"The profit of your agency from {name} tickets is {profit:.2f} lv.")