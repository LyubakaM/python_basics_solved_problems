window_frames_number = int(input())
window_frames_type = input()
delivery_type = input()

single_price = 0
discount = 1
output = 'Invalid order'

if window_frames_type == '90X130':
    single_price = 110
    if window_frames_number > 60:
        discount = 0.92
    elif window_frames_number > 30:
        discount = 0.95
elif window_frames_type == '100X150':
    single_price = 140
    if window_frames_number > 80:
        discount = 0.90
    elif window_frames_number > 40:
        discount = 0.94
elif window_frames_type == '130X180':
    single_price = 190
    if window_frames_number > 50:
        discount = 0.88
    elif window_frames_number > 20:
        discount = 0.93
elif window_frames_type == '200X300':
    single_price = 250
    if window_frames_number > 50:
        discount = 0.86
    elif window_frames_number > 25:
        discount = 0.91

if window_frames_number > 10:
    output = single_price * window_frames_number * discount
    if delivery_type == 'With delivery':
        output += 60
    if window_frames_number > 99:
        output *= 0.96
    output = f'{output:.2f} BGN'
print(output)
