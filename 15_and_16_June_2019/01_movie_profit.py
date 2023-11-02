movie_name = input()
days = int(input())
tickets = int(input())
ticket_price = float(input())
movie_rent = int(input())

price_day = tickets * ticket_price
total = days * price_day
rent = (total * movie_rent)/100
diff = total - rent

print(f"The profit from the movie {movie_name} is {diff:.2f} lv.")
