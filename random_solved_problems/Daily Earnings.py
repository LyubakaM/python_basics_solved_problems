br_rab_dnimesec = int(input())
pari_na_den = float(input())
dolar_lev = float(input())

zaplata_za_mesec = br_rab_dnimesec * pari_na_den
godishen_dohod = zaplata_za_mesec * 12 + (zaplata_za_mesec * 2.5)
danak = godishen_dohod * 0.25
chist_godishendohod = godishen_dohod - danak
chist_gosishendohodleva = chist_godishendohod * dolar_lev
sredna_pechalba_naden = chist_gosishendohodleva / 365

print("%.2f"%sredna_pechalba_naden)




