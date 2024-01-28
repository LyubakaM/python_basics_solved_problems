for i in range(number_n):
    numbers = float(input())
    if i % 2:
        even_count += numbers
        if numbers > even_max:
            even_max = numbers
        if even_min > numbers:
            even_min = numbers
    else:
        odd_count += numbers
        if numbers > odd_max_count:
            odd_max_count = numbers
        if odd_min_count > numbers:
            odd_min_count = numbers
if number_n == 0:
    print(f"OddSum={odd_count:.2f},")
    print(f"OddMin=No,")
    print("OddMax=No,")
    print(f"EvenSum={even_count:.2f},")
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
elif number_n == 1:
    print(f"OddSum={odd_count:.2f},")
    print(f"OddMin={odd_min_count:.2f},")
    print(f"OddMax={odd_max_count:.2f},")
    print(f"EvenSum={even_count:.2f},")
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
else:
    print(f"OddSum={odd_count:.2f},")
    print(f"OddMin={odd_min_count:.2f},")
    print(f"OddMax={odd_max_count:.2f},")
    print(f"EvenSum={even_count:.2f},")
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")
