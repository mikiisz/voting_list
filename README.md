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
* [Help](#help)


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
### Zdobyte poparcie dla partii
```
$> plot --csv-file-path ../parties/joined_parties.csv --xaxis-mode vertical  --yaxis-left 8 --yaxis-right 18 --yaxis-top 0 --yaxis-bottom 2496 --title Zdobyte_poparcie_dla_partii --xlabel Ilość_głosów --ylabel Partia
```
![Zdobyte_poparcie_dla_partii.svg](./graphs/Zdobyte_poparcie_dla_partii.svg)
##### Analiza wykresu
Na powyższym wykresie przedstawione są liczby głosów oddanych na poszczególne partie. Nie ma tu żadnych nowości, wyniki ukazane na tym wykresie pokrywają się z wynikami przedstawianymi w polskich mediach. Znaczną przewagę nad resztą partii posiadają Prawo i Sprawiedliwość oraz Koalicja Europejska.

### Zdobyte poparcie dla partii - probka 100000
```
$> plot --csv-file-path ../parties/joined_parties_1000.csv --xaxis-mode vertical  --yaxis-left 8 --yaxis-right 18 --yaxis-top 0 --yaxis-bottom 2496 --title Zdobyte_poparcie_dla_partii --xlabel Ilość_głosów --ylabel Partia
```
![Zdobyte_poparcie_dla_partii_2.svg](./graphs/Zdobyte_poparcie_dla_partii_2.svg)
##### Analiza wykresu
Z kolei na powyższym wykresie zostały przedstawione informacje na temat rozkładu tej samej cechy (ilości ważnych głosów oddanych na poszczególną partię), jednak zostały one przygotowane na podstawie próbki liczącej 100000 wpisów z całej populacji (~14 mln wpisów). Pomimo użycia wybierania próbki na podstawie zwykłego, komputerowego pseudolosowania, uzyskany wykres mocno przypomina wykres przedstawiony powyżej (słupki dla poszczególnych partii są proporcjonalnie długie). Oczywiście z powodu wybrania tylko 100000 wpisów, zmniejszyła się również ogólna liczba głosów.

### Liczba głosów nieważnych na terytorium
```
$> plot --csv-file-path ../parties/joined_parties.csv --xaxis-mode horizontal --xaxis 2 --yaxis-left 5 --yaxis-right 6 --yaxis-top 0 --yaxis-bottom 2496 --select-top 20 --title Liczba_głosów_nieważnych_na_terytorium --xlabel Liczba_głosów --ylabel Jednostka_terytorialna
```
![Liczba_głosów_nieważnych_na_terytorium.svg](./graphs/Liczba_głosów_nieważnych_na_terytorium.svg)
##### Analiza wykresu
Na powyższym wykresie zostały przedstawione 20 takich jednostek terytorialnych, gdzie ilość nieważnych głosów była największa. Nie powinno być większego zaskoczenia, że w czołówce znajdują się największe miasta Polski. Jest to oczywiście spowodowane tym, że w tych miastach mieszka bardzo dużo ludzi, stąd też liczba pomyłkowo uzupełnionych kart głosowania jest większa. Jednak są również mniejsze miasta, np. jak Gliwice czy Radom, gdzie ilość nieważnych głosów jest duża.

### Poparcie dla kandydatów (top 10 & top 30)
```
$> plot --csv-file-path ../candidates/joined_candidates.csv --xaxis-mode horizontal --xaxis 5 --yaxis-left 8 --yaxis-right 9 --yaxis-top 0 --yaxis-bottom 866 --select-top 10 --title Poparcie_dla_kandydatów_(top_10) --xlabel Ilość_głosów --ylabel Kandydat
```
![Poparcie_dla_kandydatów_(top_10).svg](./graphs/Poparcie_dla_kandydatów_(top_10).svg)

```
$> plot --csv-file-path ../candidates/joined_candidates.csv --xaxis-mode horizontal --xaxis 5 --yaxis-left 8 --yaxis-right 9 --yaxis-top 0 --yaxis-bottom 866 --select-top 30 --title Poparcie_dla_kandydatów_(top_30) --xlabel Ilość_głosów --ylabel Kandydat
```
![Poparcie_dla_kandydatów_(top_30).svg](./graphs/Poparcie_dla_kandydatów_(top_30).svg)
##### Analiza wykresów
Powyższe wykresy przedstawiają kandydatów, którzy otrzymali największe poparcie wraz z liczbą głosów na nich.

### Liczba kandydatów na partię
```
$> plot --csv-file-path ../candidates/joined_candidates.csv --xaxis-mode horizontal --xaxis 3 --yaxis-left 8 --yaxis-right 9 --yaxis-top 0 --yaxis-bottom 866 --count-mode 1 --title Liczba_kandydatów_na_partię --xlabel Liczba_kandydatów --ylabel Partia
```
![Liczba_kandydatów_na_partię.svg](./graphs/Liczba_kandydatów_na_partię.svg)
##### Analiza wykresu
Powyższy wykres przedstawia liczbę osób kandydujących do Parlamentu Europejskiego należących do poszczególnych partii. Jak można wywnioskować, pierwsza piątka partii z tego wykresu zgłosiła niemalże maksymalną liczbę swoich kandydatów.

### Średnia liczba głosów na kandydatów partii
```
$> plot --csv-file-path ../candidates/joined_candidates.csv --xaxis-mode horizontal --xaxis 3 --yaxis-left 8 --yaxis-right 9 --yaxis-top 0 --yaxis-bottom 866 --mode mean --title Średnia_liczba_głosów_na_kandydatów_partii --xlabel Średnia_liczba_głosów --ylabel Partia
```
![Średnia_liczba_głosów_na_kandydatów_partii.svg](./graphs/Średnia_liczba_głosów_na_kandydatów_partii.svg)
##### Analiza wykresu
Powyższy wykres przedstawia średnią liczbę głosów oddanych na kandydatów poszczególnych partii. Patrząc na poprzednie wykresy - Liczba kandydatów na partię oraz Zdobyte poparcie dla partii - można stwierdzić, iż dla pięciu pierwszych partii słupki mają proporcjonalną długość do długości słupków z wykresu Zdobyte poparcie dla partii. Jest to oczywiste spostrzeżenie, i nie można tego zauważyć dla pozostałych partii, ponieważ w tych partiach liczba kandydatur była znacząco mniejsza.

### Płeć kandydatów
```
$> plot --csv-file-path ../candidates/joined_candidates.csv --xaxis-mode horizontal --xaxis 6 --yaxis-left 8 --yaxis-right 9 --yaxis-top 0 --yaxis-bottom 866 --title Płeć_kandydatów --xlabel Liczba_kandydatów --ylabel Płeć --count-mode 1
```
![Płeć_kandydatów.svg](./graphs/Płeć_kandydatów.svg)
##### Analiza wykresu
Wykres powyżej przedstawia liczbę kandydatów poszczególnych płci. Można na podstawie tego wywnioskować, że męszczyźni są bardziej zainteresowani polityką niż kobiety.

### Średnia liczba głosów na płeć
```
$> plot --csv-file-path ../candidates/joined_candidates.csv --xaxis-mode horizontal --xaxis 6 --yaxis-left 8 --yaxis-right 9 --yaxis-top 0 --yaxis-bottom 866 --xlabel Średnia_liczba_głosów --ylabel Płeć --mode mean --title Średnia_liczba_głosów_na_płeć
```
![Średnia_liczba_głosów_na_płeć.svg](./graphs/Średnia_liczba_głosów_na_płeć.svg)
##### Analiza wykresu
Powyższy wykres z kolei przedstawia średnią liczbę uzyskanych głósów oddanych na kandydatów w obrębie tej samej płci. Jak widać, męszczyźni nie tylko chętniej biorą czynny udział w polityce, ale też są darzeni większym zaufaniem niż kobiety. Pomimo tego, najwięcej głosów jednak otrzymały dwie kobiety - była Pani premier oraz Pani Jadwiga Wiśniewska.

### Średnia liczba głosów na zawód
```
$> plot --csv-file-path ../candidates/joined_candidates.csv --xaxis-mode horizontal --xaxis 7 --yaxis-left 8 --yaxis-right 9 --yaxis-top 0 --yaxis-bottom 866 --select-top 20 --mode mean --title Średnia_liczba_głosów_na_zawód --xlabel Średnia_liczba_głosów --ylabel Zawód
```
![Średnia_liczba_głosów_na_zawód.svg](./graphs/Średnia_liczba_głosów_na_zawód.svg)

### Liczba kandydatów danego zawodu
```
$> plot --csv-file-path ../candidates/joined_candidates.csv --xaxis-mode horizontal --xaxis 7 --yaxis-left 8 --yaxis-right 9 --yaxis-top 0 --yaxis-bottom 866 --select-top 20 --count-mode 1 --title Liczba_kandydatów_danego_zawodu --xlabel Liczba_kandydatów --ylabel Zawód
```
![Liczba_kandydatów_danego_zawodu.svg](./graphs/Liczba_kandydatów_danego_zawodu.svg)
##### Analiza wykresów
Popatrzmy teraz na dwa powyższe wykresy. Na podstawie tego drugiego można wywnioskować, że sporą część kandydatów stanowią przedsiębiorcy, ekonomiści, prawnicy oraz politologowie, jednak żaden z tych zawodów nie uzyskał wystarczającej średniej liczby głosów na kandydata, żeby mógł się znaleść w przodującej dwudziestce jeżeli chodzi o poparcie. Jedynymi zawodami, które znalazły się w obydwu zestawieniach są: zawód parlamentarzysty, historyka, radcy prawa, lekarza, nauczyciela i wykładowcy akademickiego i pedagoga. Przeważnie kandydaci pracujący w tych zawodach są darzeni wysokim zaufaniem ze strony obywateli, ze względu na swoje wykształcenie, znajmość prawa lub po prostu za wykonywanie zawodu związanego z pomocą ludzkości. Z tego powodu dużo osób wykonujących te zawody startuje w wyborach. Na pierwszym wykresie zapewne na pierwszych pozycjach plasują sie zawody mające maksymalnie kilka przedstawicieli, stąd też nie można na podstawie tego określić stopnia zainteresowania wyborców tymi zawodami.

Następne wykresy zostały wygenerowane starszą wersją programu: zmiana polega w odwróceniu osi wykresu.

### Box plot dla zawodu ekonomista (starsza wersja programu)
```
$> plot --csv-file-path ../candidates/joined_candidates.csv --xaxis-mode horizontal --xaxis 7 --yaxis-left 8 --yaxis-right 9 --yaxis-top 0 --yaxis-bottom 866 --select-key ekonomista --title Box_plot_dla_zawodu_ekonomista --xlabel . --ylabel Liczba_głosów
```
![Box_plot_dla_zawodu_ekonomista.svg](./graphs/Box_plot_dla_zawodu_ekonomista.svg)
##### Analiza wykresu
Na podstawie powyższego wykresu oraz poprzednich można stwierdzić, że pomimo dużej liczby przedstawicieli-kandydatów zawodu ekonomista, jedynie kilka osób cieszy się wysokim poparciem - są to zapewne powszechnie znane osobliwości. Natomiast reszta kandydatów jest mało znana, co psuje średnią liczbę głosów na kandydata tego zawodu. Wszystkie wysnute wnioski potwierdza niska wartość mediany oraz rozstępu międzykwartylowego.

### Box plot dla zawodu nauczyciel akademicki (starsza wersja programu)
```
$> plot --csv-file-path ../candidates/joined_candidates.csv --xaxis-mode horizontal --xaxis 7 --yaxis-left 8 --yaxis-right 9 --yaxis-top 0 --yaxis-bottom 866 --select-key nauczyciel_akademicki --title Box_plot_dla_zawodu_nauczyciel_akademicki --xlabel . --ylabel Liczba_głosów
```
![Box_plot_dla_zawodu_nauczyciel_akademicki.svg](./graphs/Box_plot_dla_zawodu_nauczyciel_akademicki.svg)
##### Analiza wykresu
Podobnie prezentuje się wykres dla zawodu nauczyciel akademicki. Również jest kilku przedstawicieli tego zawodu czieszących sie dużym poparciem, mediana posiada zbliżoną wartość do wykresu poprzedniego. Jednak tutaj można już zaobserwować o wiele wyższą wartość kwartylu górnego, co wskazuje na to, że wielu kandydatów tego zawodu cieszyło niemałym poparciem.

### Box plot dla zawodu polityk (starsza wersja programu)
```
$> plot --csv-file-path ../candidates/joined_candidates.csv --xaxis-mode horizontal --xaxis 7 --yaxis-left 8 --yaxis-right 9 --yaxis-top 0 --yaxis-bottom 866 --select-key polityk --title Box_plot_dla_zawodu_polityk --xlabel . --ylabel Liczba_głosów
```
![Box_plot_dla_zawodu_polityk.svg](./graphs/Box_plot_dla_zawodu_polityk.svg)
##### Analiza wykresu
Na powyższym wykresie już nie widzimy wartości odstających - poparcia na kandydatów tego zawodu są tego samego rzędu wielkości. Mediana utrzymująca się na poziomie 50000 głosów poparcia na kandydata, oraz plasujący się wysoko kwarty górny i dolny mogą świadczyć o wysokim poparciu dla większości kandydatów tego zawodu. Nie ma co się dziwić temu wykresowi - politycy są to osoby powszechnie znane, to też otrzymują przeważną ilość głosów spośród wszystkich oddanych głosów.

### Box plot dla zawodu przedsiębiorca (starsza wersja programu)
```
$> plot --csv-file-path ../candidates/joined_candidates.csv --xaxis-mode horizontal --xaxis 7 --yaxis-left 8 --yaxis-right 9 --yaxis-top 0 --yaxis-bottom 866 --select-key przedsiębiorca --title Box_plot_dla_zawodu_przedsiębiorca --xlabel . --ylabel Liczba_głosów
```
![Box_plot_dla_zawodu_przedsiębiorca.svg](./graphs/Box_plot_dla_zawodu_przedsiębiorca.svg)
##### Analiza wykresu
Powyższy wykres jest podobny do wykresów pudełkowych dla zawodów ekonomista i nauczyciel akademicki, jednak tutaj ogólne poparcie na kandydatów tego zawodu jest o wiele niższe, patrząc na zakres wartości oraz niską wartość kwartylu górnego. Patrząc dodatkowo na wykres przedstawiający liczbę kandydatów danego zawodu, dokładniej na liczbę przedsiębiorców można pomyśleć, że zdecydowana większość zgłosiła swoją kandydaturę ot tak, nie będąc przy tym osobą znaną nawet w swoim województwie.

## Własny program użyty do wygenerowania wykresów - instrukcja użytkowania
Aby rozpocząć generowanie wykresów przedstawiających odpowiednie informacje, należy uruchomić python-owy, command-line-owy program po przez:
```
$> python3 main.py
```
Aby móc uruchomić program, należy mieć zainstalowaną bibliotekę numpy oraz matplotlib.

Podczas wprowadzania komend można używać znaku tabulacji do wyświetlania podpowiedzi, oraz używać klawiszy strzałek do wybierania komend z historii.

Do rysowania wykresów należy użyć polecenia ```plot```. Polecenie to przetwarza wszystkie komórki z WARTOŚCIAMI ze wskazanego zakresu, wybierając dla każdej komórki odpowiednią komórkę z ARGUMENTEM dla danej WARTOŚCI, a następnie grupuje wszystkie WARTOŚCI według ARGUMENTÓW. ARGUMENTY będą odkładane na osi Y, natomiast odpowiednio przetworzone WARTOŚCI na osi X. Polecenie ```plot``` przyjmuje następujące parametry:
```
  --csv-file-path path - określa, z którego pliku CSV znajdującego się w odpowiedniej 
  lokalizacji zadanej przez path mają zostać pobrane dane do wykresu
  
  --xaxis-mode [vertical(default)/horizontal] - określa wzajemne położenie komórek 
  pliku CSV - ARGUMENT - WARTOŚĆ. Opcja vertical będzie wskazywać, że komórka z 
  ARGUMENTEM będzie leżała w tej samej kolumnie co komórka z WARTOŚCIĄ, natomiast 
  opcja horizontal będzie wskazywać, że komórka z ARGUMENTEM będzie leżała w tym 
  samym wierszu co komórka z WARTOŚCIĄ.
  
  --xaxis value - przy opcji vertical będzie wskazywać położenie komórki z ARGUMENTEM
  jako value:{id_kolumny_komórki_z_WARTOŚCIĄ}, natomiast przy opcji horizontal będzie
  wskazywać położenie komórki z ARGUMENTEM jako {id_wiersza_komórki_z_WARTOŚCIĄ}:value.
  W przypadku opcji vertical oraz value = -1 wskazywany jest wiersz nagłówkowy pliku.
  
  --yaxis-left value - wskazuje lewy bok (pierwsza kolumna wybierana) obszaru wyboru 
  komórek z WARTOŚCIAMI
  
  --yaxis-right value - wskazuje za-prawy bok (pierwsza kolumna niewybierana) obszaru
  wyboru komórek z WARTOŚCIAMI
  
  --yaxis-top value - wskazuje górny bok (pierwszy wiersz wybierany) obszaru wyboru 
  komórek z WARTOŚCIAMI
  
  --yaxis-bottom value - wskazuje za-dolny bok (pierwszy wiersz niewybierany) obszaru
  wyboru komórek z WARTOŚCIAMI
  
  --select-top value(default=-1) - ogranicza zbiór argumentów dla wykresu do value 
  największych (pod względem odpowiedniej wartości) wyników. Dla value = -1 ograniczenie
  nie występuje.
  
  --count-mode [0(default)/1] - ustawia tryb wyliczania. Włączenie tego trybu oznacza 
  zliczenie wszystkich wystąpień danego ARGUMENTU, natomiast wyłączenie oznacza pobranie
  listy wszystkich WARTOŚCI dla poszczególnych ARGUMENTÓW.
  
  --mode [sum(default)/mean] - ustawia tryb przetwarzania danych list dla wszystkich 
  ARGUMENTÓW. Opcja sum oznacza zsumowanie wartości listy dla każdego ARGUMENTU, 
  natomiast opcja mean oznacza obliczenie zwykłej średniej z tych wartości.
  
  --select-key key - wybiera ARGUMENT o nazwie key i jedynie ten ARGUMENT przedstawia 
  na wykresie pudełkowym, działając na WARTOŚCIACH tego ARGUMENTU. Jeżeli ARGUMENT 
  o podanej nazwie nie istnieje, wykres nie jest rysowany.
  
  --title text - ustawia tytuł wykresu jako text
  
  --xlabel text - ustawia tytuł osi X jako text
  
  --ylabel text - ustawia tytuł osi Y jako text
  
  --box-plot [0(default)/1] - ustawia tryb rysowania wykresów pudełkowych. Włączenie tego
  trybu oznacza rysowanie wykresów pudełkowych dla ARGUMENTÓW zamiast wykresów słupkowych.
  
Dla parametrów --select-key, --title, --xlabel, --ylabel, w celu wprowadzenia znaku 
spacji w opcji danego parametru, należy zastosować znak '_'.
```
