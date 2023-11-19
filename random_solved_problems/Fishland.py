pr_skumria_kg = float(input())
pr_cac_kg = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

midi = 7.50
safrid = (pr_cac_kg * 0.80) + pr_cac_kg
palamud = (pr_skumria_kg * 0.60) + pr_skumria_kg

total = midi_kg * midi + safrid_kg * safrid + palamud_kg * palamud
print(f"{total:.2f}")
