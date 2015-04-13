# dijkstra-giz
## Wstęp
Projekt z przedmiotu Grafy na Polsko-Japońskiej Akademii Technik Komputerowych

## Treść zadania:

W Archipelagu Bajtocji jest n wysp (ponumerowanych od 1 do n). Pomiędzy
wyspami można poruszać się tylko promem, które pływają tylko pomiędzy
poszczególnymi wyspami. Bajtek musi się przemieścić
z wyspy o numerze 1 do wyspy o numerze n. Bajtek cierpi
na chorobę morską, dlatego chce zminimalizować długość podróży.
Pomóż mu w tym problemie.

* Wejście:
W pierszej linii znajdują się 2 liczby: n i m, gdzie n jest liczbą wysp,
a m liczbą połączeń pomiędzy wyspami. m następnych wierszy zawiera
3 liczby: a, b i d, które oznaczają, że prom pływa od a do b
trasą o długości d.

* Wyjście:
W pierszej linii ma się znaleźć liczba oznaczająca łączną długość
podróży. W następnej linii mają znaleźć się kolejne wyspy odwiedzane
przez Bajtka (wraz z początkową i końcową)

* Przykład wejścia:
```
4 5
1 2 4
1 3 4
2 3 5
2 1 10
3 4 1
```

* Przykład wyjścia:
```
5
1 3 4
```

* Inne wymagania:
Program ma czytać ze standardowego wejścia i wypisywać rozwiązanie
na standardowe wyjście; n < 100000, m < 200000.

## Algorytm
Wykorzystany został algorytm Dijkstry. Poniższy pseudokod zaczerpnięty z wikipedii:

```
Dijkstra(G,w,s):
   dla każdego wierzchołka v w V[G] wykonaj
      d[v] := nieskończoność
      poprzednik[v] := niezdefiniowane
   d[s] := 0
   Q := V
   dopóki Q niepuste wykonaj
      u := Zdejmij_Min(Q)
      dla każdego wierzchołka v – sąsiada u wykonaj
         jeżeli d[v] > d[u] + w(u, v) to
            d[v] := d[u] + w(u, v)
            poprzednik[v] := u
            Dodaj(Q, v)

   Wyświetl("Droga wynosi: " + [v])
```
## Instalacja:
Program wymaga zainstalowanego interptretera python wraz z biblioteką graphviz.
```
$ git clone https://github.com/lukaszsedek/dijkstra-giz.git
$ cd dijkstra-giz
$ virtualenv env
$ source env/bin/activate
$ pip install graphviz
```

## Instrukcja użytkownika:

Do uruchomienia programu wymagane są uprawdnienia administratora. Program korzysta z biblioteki graphviz, która jest wykorzystywana do
utworzenia pliku graph.png. Jest to plik przedstawiający graficzną prezentację algorytmu

```bash
$ Usage: main.py [options]

Options:
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  load initial topology from FILE
  -l LEVEL, --log=LEVEL
                        set logging level LOG, DEBUG

$ sudo python dijkstra-giz/main.py -f tests/my.txt
Password:
9
1 7 8 13 19 25
$
$ ls | grep graph
Digraph.gv
graph
graph.pdf
```
Dodatkowo w katalogu tests znajdują się trzy pliki do weryfikacji poprawoności działania algorytmu

### Struktura katalogów
```
.
├── LICENSE
├── README.md
├── dijkstra-giz
│   ├── __init__.py
│   ├── dijkstra.py
│   ├── dijkstra.pyc
│   ├── graph.py
│   ├── graph.pyc
│   ├── main.py
│   ├── vertex.py
│   ├── vertex.pyc
│   └── wiki.txt
├── docs
├── setup.py
└── tests
    ├── my.txt
    ├── test.txt
    └── wiki.txt
```

# Licencja:

Apache Common 2.0