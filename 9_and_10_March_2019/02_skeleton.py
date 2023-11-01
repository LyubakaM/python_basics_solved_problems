minutes_control = int(input())
seconds_control = int(input())
channel_len_meters = float(input())
seconds_per_100 = int(input())

control_secs = minutes_control * 60 + seconds_control
time_dec_count = channel_len_meters / 120
total_dec_time = time_dec_count * 2.5

total_time_marin = (channel_len_meters/100) * seconds_per_100 - total_dec_time
diff = total_time_marin - control_secs

if total_time_marin <= control_secs:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_time_marin:.3f}.")
else:
    print(f"No, Marin failed! He was {diff:.3f} second slower.")


