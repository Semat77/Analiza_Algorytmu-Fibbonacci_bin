import timeit

print("Proszę o podanie zerojedynkowej wartości.")
liczba_binarna = input();  # bierzemy input od użytkownika


def fib_suma_binarna(licz_binarna):  # przyjmuje jako argument liczbę binarną i zwraca jej wartosc dziesietna
    for char in licz_binarna:
        if char != '0' and char != '1':
            return "Podano niepoprawną wartość, wprowadź tylko 0 i 1."
        else:
            rezultat = 0  # ustawiamy rezultat na 0
            indeks = 1  # indeks ustawiamy na 1
            licz_binarna = str(licz_binarna)  # zmieniamy zmienną na string-a
            for cyfra in licz_binarna[::-1]: #przeglądamy cały ciąg cyfr
                if cyfra == '1':
                    rezultat += fibonacci(indeks)  # jeśli cyfra jest równa 1 dodajemy jej odpowiedni element do ciągu fib
                indeks += 1 #zwiekszamy indeks o 1
            return rezultat  # zwracamy jako wartość dziesiętną
def fibonacci(rezultat): #zwraca n-ty element ciągu Fibonacciego
    if rezultat == 1:
        return 1
    elif rezultat <= 0:
        return 0
    else:
        return fibonacci(rezultat - 1) + fibonacci(rezultat - 2)  # zwraca sumę dwóch poprzednich elementów ciągu
# Wynik
print("Wynik", fib_suma_binarna(liczba_binarna))
# czas wykonania algorytmu
print("Czas wykonania:", timeit.timeit(lambda:fib_suma_binarna(liczba_binarna), number = 1), "sekund")
