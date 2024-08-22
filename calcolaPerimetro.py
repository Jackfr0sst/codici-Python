def perimetro_figura(figura):
    if figura == "quadrato":
        print(f"il perimetro di questo quadrato è di {lato * 4}cm.")
    elif figura == "cerchio":
        print(f"la circonferenza di questo cerchio è di {2 * 3.14 * raggio}cm.")
    else:
        print(f"il perimetro di questo rettangolo è di {2 * base + 2 * altezza}cm.")

figura = input("--------------------------\nscegliere la figura di cui si vuole calcolare il perimetro\n1. Quadrato\n2. Cerchio\n3. Rettangolo\n--------------------------\nla tua scelta (nome della figura): ").lower()
if figura == "quadrato":
    lato = float(input("\ninserisci la dimensione del lato in cm: "))
    perimetro_figura(figura)

elif figura == "cerchio":
    raggio = float( input("\ninserisci la dimensione del raggio in cm: "))
    perimetro_figura(figura)

elif figura == "rettangolo":
    base = float(input("\ninserisci la dimensione della base in cm: "))
    altezza = float(input("\ninserisci la dimensione dell'altezza in cm: "))
    perimetro_figura(figura)

else:
    print("scegliere solo una delle tre figure proposte.")