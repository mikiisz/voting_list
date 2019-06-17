from random import randint, sample
from time import time
import metadata
import csv


def main():
    regions_path = './csv_data/wyniki_gl_na_listy_po_gminach.csv'
    candidates_path = './csv_data/kandydaci.csv'
    output_party_voting = 'głosy_na_partie.csv'
    output_candidates_voting = 'głosy_na_kandydatów.csv'

    start_time = time()

    party_votes(regions_path, output_party_voting)
    candidates_votes(candidates_path, output_candidates_voting)

    end_time = time()

    print('--- generating records took', (end_time - start_time), 'seconds ---')


def party_votes(input_path, output_path):
    with \
            open(input_path) as regions_csv, \
            open(output_path, 'w') as output_csv:

        regions_reader = csv.DictReader(regions_csv)
        writer = csv.DictWriter(output_csv, fieldnames=metadata.field_party)
        writer.writeheader()

        vote_id = 1
        for i, row in enumerate(regions_reader):
            output_rows = []
            data = metadata.get_data(row)

            start = vote_id
            for party in metadata.field_party[8:]:
                vote_id = insert_parties(party, output_rows, vote_id, data)
            stop = vote_id - start
            start = 0

            for value in metadata.field_party[3:5]:
                insert_randomized_value(start, stop, value, output_rows, data)

            vote_id = insert_invalid_vote(start, stop, output_rows, vote_id,
                                          data)

            for single_row in output_rows:
                writer.writerow(single_row)

            if not vote_id % 1e6:
                print('Processing:', vote_id, '...')

            if i > 4:
                break


def candidates_votes(input_path, output_path):
    pass


def insert_parties(party, output_row, id_vote, data):
    key = TextKeeper()

    for _ in range(data.get(party)):
        update_row = {
            'ID': id_vote,
            key('TERYT'): data.get(str(key)),
            key('JEDNOSTKA TERYTORIALNA'): data.get(str(key)),
            party: 1
        }
        output_row.append(update_row)
        id_vote += 1
    return id_vote


def insert_randomized_value(id_start, id_stop, value, output_rows, data):
    for _ in range(data.get(value)):
        id_rand = randint(id_start, id_stop)
        update_row = {
            value: 1
        }
        output_rows[id_rand - 1].update(update_row)


def insert_invalid_vote(id_start, id_end, output_rows, id_vote, data):
    key = TextKeeper()
    value_1, value_2, value_3 = metadata.field_party[5:8]

    diff = 0
    for _ in range(data.get(value_1)):
        update_row = {
            'ID': id_vote,
            key('TERYT'): data.get(str(key)),
            key('JEDNOSTKA TERYTORIALNA'): data.get(str(key)),
            value_1: 1
        }
        output_rows.append(update_row)
        id_vote += 1
        diff += 1

    value_list = range(id_end, id_end + diff)
    value_2_list = sample(value_list, data.get(value_2))
    value_3_list = sample(
        [item for item in value_list if item not in value_2_list],
        data.get(value_3))

    for value_x_list in [(value_2_list, value_2), (value_3_list, value_3)]:
        for i in value_x_list[0]:
            update_row = {
                value_x_list[1]: 1
            }

            output_rows[i - 1].update(update_row)

    return id_vote


class TextKeeper:
    def __init__(self):
        self.text = None

    def __repr__(self):
        return self.text

    def __call__(self, new_text):
        self.text = str(new_text)
        return self.text


if __name__ == "__main__":
    main()
