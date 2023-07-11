# RADY DO ŽIVOTA

print('Odpovedaj "ano" alebo "nie".')
stastna_retezec = input('Si šťastná?')
if stastna_retezec == 'ano' or stastna_retezec == 'Ano':
    stastna = True
elif stastna_retezec == 'ne' or stastna_retezec == 'Ne' or stastna_retezec == 'Nie' or stastna_retezec == 'nie':
    stastna = False
else:
    print('Nerozumiem!')            # Doplnit smycku pri nerozumiem, nech sa opyta este raz.

bohata_retezec = input('Si bohatá? ')
if bohata_retezec == 'ano' or bohata_retezec == 'Ano':
    bohata_retezec = True
elif bohata_retezec == 'ne' or bohata_retezec == 'Ne' or bohata_retezec == 'Nie' or bohata_retezec == 'nie':
    bohata_retezec = False
else:
    print('Nerozumiem!')

if  bohata_retezec and stastna:
    # Je bohatá a zároveň štǎstná, ta sa má.
    print('Gratulujem!')
elif bohata:
    # Je bohatá, ale nie je „bohatá a zároveň šťastná“,
    # takže musí byť len bohatá.
    print('Skus sa viac usmievať.')
elif stastna:
    # Tu musí byť len šťastná.
    print('Skus menej utrácať.')
else:
    # A tu vieme, že nie je ani šťastná, ani bohatá.
    print('To je mi ľúto.')
