secret_word = ""
c_com_true = False
o_com_true = False
n_com_true = False
while True:
    expression = input()
    if c_com_true and n_com_true and o_com_true:
        print(secret_word, end=" ")
        secret_word = ""
        c_com_true = False
        n_com_true = False
        o_com_true = False
    if expression == "End":
        break
    letter = expression[0]
    if letter.isalpha():
        if letter == 'c' and not c_com_true:
            c_com_true = True
            continue
        elif letter == 'c' and c_com_true:
            secret_word += letter
            continue
        if letter == 'o' and not o_com_true:
            o_com_true = True
            continue
        elif letter == 'o' and o_com_true:
            secret_word += letter
            continue
        if letter == 'n' and not n_com_true:
            n_com_true = True
            continue
        elif letter == 'n' and n_com_true:
            secret_word += letter
            continue
        secret_word += letter
    else:
        continue
