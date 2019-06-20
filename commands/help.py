help_text = """
Dostępne komendy:
    - help
    - load
    - room-table
    - free
    
------------------------------------------
# help - wyświetla opis dostępnych komend
> nie przyjmuje żadnych argumentów
------------------------------------------
# load - wczytuje akrusz do programu, jeśli arkusz znajduje się w domyślnej lokalizacji ustawionej w config.json, zostanie załadowany do programu podczas jego uruchomienia, jeśli nie to trzeba podać ścieżkę do arkusza
> jako argument przyjmuje ścieżkę do arkusza - argument wymagany

przykład:
    load data/sheet.xlsx
------------------------------------------
# room-table - generuje plik pdf z informacjami o zajętości sal
> jako argument przyjmuje ścieżkę gdzie ma zostać zapisany wygenerowany pdf

przykład:
    room-table sale.pdf
------------------------------------------
# free - wyświetla informacje o wolnych salach w zależności od podanych parametrów
> dostępne argumenty
    -d <dzień tygodnia> - wyświetla sale które są wolne w podanym dniu, powtórzenie parametru powoduje sumę wyników
    -h <godzina rozpoczęcia bloku zajęć> - wyświetla sale które są wolne o podanej godzinie, powtórzenie parametru powoduje sumę wyników
    -c <pojemność sali> - wyświetla sale które mają większą pojemność niż podana
    -t <typ sali> - wyświetla sale o podanym typie (wykładowa, laboratoryjna itp)
    -r <nazwa sali> - sprawdza czy podane sale są wolne, powtórzenie parametru powoduje sumę wyników

przykład:
    free -r D17:1.38 -r D17:1.18 -d Pn -d Pt -h 8:00 -h 11:15 -c 50
------------------------------------------
Używaj znaku TAB aby skorzystać z podpowiedzi do komend


"""


class Help:

    def exec_command(self, x):
        print(help_text)
