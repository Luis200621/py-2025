
sueldo_base = 529_000

ventas = {
    "Luis": [300_000, 250_000, 100_000, 200_000, 180_000],
    "Dayana": [400_000, 500_000, 350_000, 300_000, 100_000],
    "Ian": [600_000, 300_000, 400_000, 100_000, 200_000]
}

print("REPORTE DE SUELDOS\n")


for vendedor, ventas_diarias in ventas.items():
    total_semanal = sum(ventas_diarias)

    if total_semanal > 1_500_000:
        bono = 0.20 * sueldo_base
    elif total_semanal > 1_000_000:
        bono = 0.10 * sueldo_base
    elif total_semanal > 500_000:
        bono = 0.05 * sueldo_base
    else:
        bono = 0


    promedio_semanal = total_semanal / len(ventas_diarias)

    sueldo_total = sueldo_base + bono


    print(f"Vendedor: {vendedor}")
    print(f" - Ventas diarias: {ventas_diarias}")
    print(f" - Total semanal: ${total_semanal:.0f}")
    print(f" - Promedio diario: ${promedio_semanal:.0f}")
    print(f" - Bono: ${bono:.0f}")
    print(f" - Sueldo total a pagar: ${sueldo_total:.0f}\n")