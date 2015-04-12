# dijkstra-giz
## Wstęp
Projekt z przedmiotu Grafy na Polsko-Japońskiej Akademii Technik Komputerowych


## Instalacja:

```
$ git clone https://github.com/lukaszsedek/dijkstra-giz.git
$ cd dijkstra-giz
$ virtualenv env
$ source env/bin/activate
$ pip install graphviz
```

# Instrukcja użytkownika:

```
$ Usage: main.py [options]

Options:
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  load initial topology from FILE
  -l LEVEL, --log=LEVEL
                        set logging level LOG, DEBUG
$ python dijkstra-giz/main.py -f tests/test.txt
```

# License:
jakas