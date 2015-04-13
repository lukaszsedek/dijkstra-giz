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

## Instalacja:

```
$ git clone https://github.com/lukaszsedek/dijkstra-giz.git
$ cd dijkstra-giz
$ virtualenv env
$ source env/bin/activate
$ pip install graphviz
```

## Instrukcja użytkownika:

```
$ Usage: main.py [options]

Options:
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  load initial topology from FILE
  -l LEVEL, --log=LEVEL
                        set logging level LOG, DEBUG
$ python dijkstra-giz/main.py -f tests/test.txt
```
```
Struktura katalogów

.
├── LICENSE
├── README.md
├── bin
├── dijkstra-giz
│   ├── __init__.py
│   ├── graph.py
│   ├── graph.pyc
│   ├── main.py
│   ├── vertex.py
│   └── vertex.pyc
├── docs
├-─ setup.py
└── tests
    └── test.txt

# License:
jakas