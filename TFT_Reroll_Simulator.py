import random

try:
    altin = int(input("Altin miktarinizi girin:"))
except ValueError:
    print("Lutfen sayi giriniz.")
else:
    while altin >= 2:
        print("Altin miktariniz:", altin, "rol lamak istiyorsaniz R, cikmak istiyorsaniz Q'ye basin.")
        secim = input("Seciminiz:")
        if secim == "R":
            altin -= 2
            print(random.choices(['1', '2', '3', '4', '5'], [15, 20, 32, 30, 3], k=5))
            if altin < 2:
                print("Yeterli altininiz kalmadi. Oyun bitti.")
                break
        elif secim == "Q":
            print("Oyun bitti. Altin miktariniz:", altin)
            break
        else:
            print("Gecersiz secim.")
    
      
