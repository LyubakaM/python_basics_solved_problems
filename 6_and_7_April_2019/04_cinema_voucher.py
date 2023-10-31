voucher = int(input())
item = input()
movie_tickets = 0
other = 0

while item != 'End':

    if len(item) > 8:
        voucher -= ord(item[1]) + ord(item[0])
        if voucher < 0:
            break
        movie_tickets += 1
    else:
        voucher -= ord(item[0])
        if voucher < 0:
            break
        other += 1
    item = input()

print(movie_tickets)
print(other)




