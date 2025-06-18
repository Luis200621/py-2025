
sueldo_base = 529000

Vendedores = {
    'dayana' = [200000, 180000, 220000, 250000, 210000],
    'luis' =   [350000, 400000, 300000, 370000, 320000],
    'ian' = [100000, 150000, 120000, 110000, 130000]
}

def bono(total):
    if total > 1500000:
        return 0.20 * sueldo_base 
    elif total > 1000000:
        return 0.10 * sueldo_base
    elif total > 500000:
        return 0.5 * sueldo_base
    else:
        return 0 
    
