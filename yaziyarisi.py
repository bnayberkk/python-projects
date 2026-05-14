import time

#kelime girisi/liste
print("TYPING SPEED TOURNAMENT")
print("Enter words. Type 'done' when finished")

kelime_liste_string = ""
kelime_adet = 0

while True:
    kelime = input("Enter word: ").lower()
    if kelime == "done":
        break

    if len(kelime) >=2:
        kelime_liste_string += kelime + " "
        kelime_adet += 1
        print(f"Added: {kelime}")
    else: 
        print("Word must be at least 2 letters!")

kelime_listesi = kelime_liste_string.split()

#oyuncular
print("How many players?")
oyuncusayisi = int(input("Enter number of players: "))

for i in range (1, oyuncusayisi + 1):
    print(f"PLAYER {i} 'S TURN")
    input("Press ENTER when you are ready. ")

    dogru_sayisi = 0
    sira = 1
    baslangic_suresi = time.time()

    for hedef_kelime in kelime_listesi:
        print(f"\nWord {sira}/{kelime_adet}: {hedef_kelime}")
        yazi = input("> ").lower().strip()

        if yazi == hedef_kelime:
            print("Correct!")
            dogru_sayisi+= 1
        else:
            print("Wrong!")

        sira += 1

    bitis_suresi = time.time()

#hesaplama
    toplam_sure = bitis_suresi - baslangic_suresi
    dogru_sayisi = (dogru_sayisi / kelime_adet) * 100
    wpm = (dogru_sayisi / toplam_sure) * 60 if toplam_sure > 0 else 0

    print(f"PLAYER {i} RESULTS:")
    print(f"Correct: {dogru_sayisi:}/{kelime_adet:}")
    print(f"Time: {toplam_sure:.1f}s")
    print(f"Accuracy: {dogru_sayisi:.0f}%")
    print(f"Speed: {wpm:.1f} WPM")




