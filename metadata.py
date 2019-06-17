field_party = [
    'ID',
    'TERYT',
    'JEDNOSTKA TERYTORIALNA',
    'GŁOSOWANIE PRZEZ PEŁNOMOCNIKA',
    'GŁOSOWANIE NA PODSTAWIE ZAŚWIADCZENIA',
    'GŁOS NIEWAŻNY',
    '"X" OBOK KILKU KANDYDATÓW',
    '"X" OBOK ŻADNEGO KANDYDATA',
    'KOALICJA EUROPEJSKA PO PSL SLD .N ZIELONI',
    'LEWICA RAZEM - PARTIA RAZEM, UNIA PRACY, RSS',
    'POLEXIT - KOALICJA',
    'JEDNOŚĆ NARODU',
    'PRAWO I SPRAWIEDLIWOŚĆ',
    'RUCH PRAWDZIWA EUROPA - EUROPA CHRISTI',
    'WIOSNA ROBERTA BIEDRONIA',
    'KONFEDERACJA KORWIN BRAUN LIROY NARODOWCY',
    'KUKIZ\'15',
    'POLSKA FAIR PLAY',
]

all_patries = [
    'KOALICYJNY KOMITET WYBORCZY KOALICJA EUROPEJSKA PO PSL SLD .N ZIELONI '
    '- ZPOW-603-7/19',
    'KOALICYJNY KOMITET WYBORCZY LEWICA RAZEM - PARTIA RAZEM, UNIA PRACY, RSS '
    '- ZPOW-603-4/19',
    'KOALICYJNY KOMITET WYBORCZY POLEXIT - KOALICJA - ZPOW-603-14/19',
    'KOMITET WYBORCZY JEDNOŚĆ NARODU - ZPOW-603-11/19',
    'KOMITET WYBORCZY PRAWO I SPRAWIEDLIWOŚĆ - ZPOW-603-5/19',
    'KOMITET WYBORCZY RUCH PRAWDZIWA EUROPA - EUROPA CHRISTI - ZPOW-603-9/19',
    'KOMITET WYBORCZY WIOSNA ROBERTA BIEDRONIA - ZPOW-603-8/19',
    'KOMITET WYBORCZY WYBORCÓW KONFEDERACJA KORWIN BRAUN LIROY NARODOWCY '
    '- ZPOW-603-3/19',
    'KOMITET WYBORCZY WYBORCÓW KUKIZ\'15 - ZPOW-603-1/19',
    'KOMITET WYBORCZY WYBORCÓW POLSKA FAIR PLAY BEZPARTYJNI GWIAZDOWSKI '
    '- ZPOW-603-6/19',
]


def get_data(row):
    data = {
        'TERYT':
            int(row['TERYT'] or 0),

        'JEDNOSTKA TERYTORIALNA':
            str(row['Jednostka terytorialna']),

        'GŁOSOWANIE PRZEZ PEŁNOMOCNIKA':
            int(row['Liczba wyborców głosujących przez pełnomocnika'] or 0),

        'GŁOSOWANIE NA PODSTAWIE ZAŚWIADCZENIA':
            int(row['Liczba wyborców głosujących na podstawie zaświadczenia '
                    'o prawie do głosowania'] or 0),

        'GŁOS NIEWAŻNY':
            int(row['Liczba głosów nieważnych'] or 0),

        '"X" OBOK KILKU KANDYDATÓW':
            int(row['w tym z powodu postawienia znaku „X” obok nazwiska dwóch '
                    'lub większej liczby kandydatów'] or 0),

        '"X" OBOK ŻADNEGO KANDYDATA':
            int(row['w tym z powodu niepostawienia znaku „X” obok nazwiska '
                    'żadnego kandydata'] or 0),

        'KOALICJA EUROPEJSKA PO PSL SLD .N ZIELONI':
            int(row[all_patries[0]] or 0),

        'LEWICA RAZEM - PARTIA RAZEM, UNIA PRACY, RSS':
            int(row[all_patries[1]] or 0),

        'POLEXIT - KOALICJA':
            int(row[all_patries[2]] or 0),

        'JEDNOŚĆ NARODU':
            int(row[all_patries[3]] or 0),

        'PRAWO I SPRAWIEDLIWOŚĆ':
            int(row[all_patries[4]] or 0),

        'RUCH PRAWDZIWA EUROPA - EUROPA CHRISTI':
            int(row[all_patries[5]] or 0),

        'WIOSNA ROBERTA BIEDRONIA':
            int(row[all_patries[6]] or 0),

        'KONFEDERACJA KORWIN BRAUN LIROY NARODOWCY':
            int(row[all_patries[7]] or 0),

        'KUKIZ\'15':
            int(row[all_patries[8]] or 0),

        'POLSKA FAIR PLAY':
            int(row[all_patries[9]] or 0),
    }
    return data
