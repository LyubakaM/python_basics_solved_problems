hall_rent = int(input())
statues = hall_rent * 0.70
catering = statues * 0.85
sound_system = catering * 0.5

total = hall_rent + statues + catering + sound_system
print(f"{total:.2f}")