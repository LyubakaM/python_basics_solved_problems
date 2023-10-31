from sys import  maxsize
n_movies = int(input())
high = - maxsize
low = maxsize
high_name = ""
low_name = ""
ave_count = 0
for movie in range(n_movies):
    movie_name = input()
    rating = float(input())
    ave_count += rating
    if rating > high:
        high = rating
        high_name = movie_name
    elif rating < low:
        low = rating
        low_name = movie_name
ave_end = (ave_count / n_movies)
print(f"{high_name} is with highest rating: {high:.1f}")
print(f"{low_name} is with lowest rating: {low:.1f}")
print(f"Average rating: {ave_end:.1f}")
