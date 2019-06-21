# voting_list
## Authors
21.06.2019,
authors:
* Michał Szkarłat
* Mateusz Wieczorek


## Elections to the European Parliament 2019
Its a simple application that generate votes from packed data and plot various graphs. 
Raw data source is here:
```
https://wybory.gov.pl/pe2019/pl/dane_w_arkuszach
```

## Table of contents
* [Authors](#authors)
* [Extracting data](#extracting-data)
* [Joining data](#joining-data)
* [Graphs](#graphs)


## Extracting data
After dowloading raw packages we need to procces them in order to get valid data that represent approximately 14 milions Polish voters from election to the European Parliament. To achive that we need to use <b> split_votes.py </b> file. Result data looks like this and represent each signle voter:

![splited_parties.py](https://raw.githubusercontent.com/mikiisz/voting_list/master/screenshots/splited_parties.png)
<i>Splited_parties.csv</i>

We are storing informations about:
* ID - represents signle voter
* TERYT
* JEDNOSTKA TERYTORIALNA
* GŁOSOWANIE PRZEZ POMOCNIKA
* GŁOSOWANIE NA PODSTAWIE ZAŚWIADCZENIA
* GŁOS NIEWAŻNY (oraz jego rodzaje)
* PARTIA

We do not store information about candidates and parties in same file. <b> Split_votes.py </b> generates also addictiona data file for candidates only, whitch looks like this:

![splited_candidates.py](https://raw.githubusercontent.com/mikiisz/voting_list/master/screenshots/splited_candidates.png)
<i>Splited_candidates.csv</i>
  
 We store informations about:
 * ID - represents signle voter
 * NUMER OKRĘGU
 * NUMER LISTY
 * NAZWA PARTII
 * NUMER NA LIŚCIE
 * NAZWISKO
 * IMIĘ
 * PŁĘĆ
 * ZAWÓD
 * ODDANY GŁOS
 
 Extracted data contains over 2 GB of data. To compress it without loosing information we need to use <b> split_votes.py </b>
 
 ## Joining data
Using <b> split_votes.py </b> script we can group some information from extracted data and get much smaller files.
Ressult looks like this.

### Joined parties:
![splited_candidates.py](https://raw.githubusercontent.com/mikiisz/voting_list/master/screenshots/joined_parties.png)
<i>Joined_parties.csv</i>

### Joined candidates:
![splited_candidates.py](https://raw.githubusercontent.com/mikiisz/voting_list/master/screenshots/joined_candidates.png)
<i>Joined_candidates.csv</i>

## Graphs
### Zdobyte_poparcie_dla_partii
![Zdobyte_poparcie_dla_partii.svg](./graphs/Zdobyte_poparcie_dla_partii.svg)

### Poparcie_dla_kandydatów_(top_10)
![Box_plot_dla_zawodu_ekonomista.svg](./graphs/Poparcie_dla_kandydatów_(top_10).svg)

### Poparcie_dla_kandydatów_(top_30)
![Poparcie_dla_kandydatów_(top_30).svg](./graphs/Poparcie_dla_kandydatów_(top_30).svg)

### Płeć_kandydatów.svg
![Płeć_kandydatów.svg](./graphs/Płeć_kandydatów.svg)

### Średnia_liczba_głosów_na_płeć
![Średnia_liczba_głosów_na_płeć.svg](./graphs/Średnia_liczba_głosów_na_płeć.svg)

### Średnia_liczba_głosów_na_zawód.svg
![Średnia_liczba_głosów_na_zawód.svg](./graphs/Średnia_liczba_głosów_na_zawód.svg)

### Liczba_kandydatów_danego_zawodu.svg
![Liczba_kandydatów_danego_zawodu.svg](./graphs/Liczba_kandydatów_danego_zawodu.svg)

### Box_plot_dla_zawodu_ekonomista
![Box_plot_dla_zawodu_ekonomista.svg](./graphs/Box_plot_dla_zawodu_ekonomista.svg)

### Box_plot_dla_zawodu_nauczyciel_akademicki.svg
![Box_plot_dla_zawodu_nauczyciel_akademicki.svg](./graphs/Box_plot_dla_zawodu_nauczyciel_akademicki.svg)

### Box_plot_dla_zawodu_polityk.svg
![Box_plot_dla_zawodu_polityk.svg](./graphs/Box_plot_dla_zawodu_polityk.svg)

### Box_plot_dla_zawodu_przedsiębiorca.svg
![Box_plot_dla_zawodu_przedsiębiorca.svg](./graphs/Box_plot_dla_zawodu_przedsiębiorca.svg)
