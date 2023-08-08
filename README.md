Budowa i analiza algorytmów – ćwiczenia Raport z realizacji mini projektu 
 
1. Treść zadania 

Ciąg Fibonacciego zdefiniowany jest następująco: 
Fib(1) = 1 
Fib(2) = 1 
Fib(n) = Fib(n-1) + Fib(n-2) dla n>2 
Dowolną liczbę naturalną możemy przedstawić w postaci ciągu zerojedynkowego zdefiniowanego w sposób następujący: jeżeli k-ta cyfra jest równa 1, wtedy odpowiada wartości Fib(k),
jeżeli 0 to jest równa 0 (cyfry numerujemy od prawej do lewej zaczynając od jeden). 
Przykład: 
11011101Fib = 1*21 + 1*13 + 0*8 + 1*5 + 1*3 + 1*2 + 0*1 + 1*1 
= 21 + 13 + 5 + 3 + 2 + 1 
= 4510 
Skonstruuj algorytm wyznaczający wartości dziesiętne takich ciągów zerojedynkowych. Uwaga: 
elementy ciągu Fibonacciego nie mogą być stablicowane.


2. Opis słowny algorytmu 

Dane wejściowe : liczba binarna Dane wyjściowe : liczba dziesiętna 
jest obliczany funkcją rekurencyjną, która zwraca n-ty element ciągu Fibonacciego. Funkcja sprawdza, 
czy n jest równe 1 i jeśli tak, zwraca 1. Jeśli n jest mniejsze lub równe 0, funkcja zwraca 0. W przeciwnym razie, funkcja zwraca sumę dwóch poprzednich elementów ciągu (obliczonych za pomocą wywołań rekurencyjnych). 

 
3. Zapis algorytmu w języku Python 


4.	Schemat blokowy  
 
![image](https://github.com/Semat77/Analiza_Algorytmu-Fibbonacci_bin/assets/100786337/65550669-8158-45ce-8932-9d0dfd8fb57a)

  
5.	Wykres zależności czasu wykonania do rozmiaru zadania 

Wykres otrzymany dzięki modułowi matplotlib wraz z timeit. Złożoność związana z obliczaniem ciągu Fibonacciego rekurencyjnie, gdzie każde wywołanie funkcji powoduje dwa kolejne wywołania 
  
 ![image](https://github.com/Semat77/Analiza_Algorytmu-Fibbonacci_bin/assets/100786337/f76013dd-844f-4355-a31d-4c6406925d08)

 
6. Oszacowanie złożoności czasowej 

Możemy ją przedstawić jako O(2^n), ponieważ każdy element ciągu Fibonacciego jest obliczany za pomocą dwóch poprzednich takich elementów.
Czas wykonania tego algorytmu to T(n) = T(n-1) + T(n-2) + O(1) dlatego, iż oparta jest ona na rekurencji (przez to, iż tak zaimplementowałem ciąg Fibonacciego) 
 
 
7. Symulacja danych wejściowych 

![image](https://github.com/Semat77/Analiza_Algorytmu-Fibbonacci_bin/assets/100786337/ee4a986c-f098-4819-a3aa-6b6ccce07b06)

 
8. Podsumowanie i wnioski

Algorytm ma za zadanie umożliwić użytkownikowi wprowadzenie liczby binarnej i zamianę jej na wartość dziesiętną.
Wartość dziesiętna jest obliczana jako suma odpowiednich elementów ciągu Fibonacciego, dla każdej jedynki w podanej liczbie binarnej. 
