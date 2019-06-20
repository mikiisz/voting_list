import csv
import metadata as md
from time import time


def main():
    parties = './głosy_na_partie.csv'
    parties_out = './joined_data.csv'
    candidates = './głosy_na_kandydatów.csv'
    candidates_out = './joined_data_candidates.csv'

    start_time = time()

    # party_votes(parties, parties_out)
    candidates_votes(candidates, candidates_out)

    end_time = time()

    print('--- generating records took', (end_time - start_time), 'seconds ---')


def candidates_votes(input_path, output_path):
    with \
            open(input_path) as input_csv, \
            open(output_path, 'w') as output_csv:
        regions_reader = csv.DictReader(input_csv)
        writer = csv.DictWriter(output_csv, fieldnames=md.field_candidates)
        writer.writeheader()
        output_row = {}

        vote_id = 1
        for i, row in enumerate(regions_reader):
            if output_row.get(md.field_candidates[6]) == \
                    row.get(md.field_candidates[6]) and \
                    output_row.get(md.field_candidates[5]) == \
                    row.get(md.field_candidates[5]):
                output_row = current_candidate(output_row, row)
            else:
                output_row, vote_id = new_candidate(vote_id, output_row, writer,
                                                    row)

            if not i % 1e6:
                print('Processing:', i, '...')

            # if i > 4:
            #     break

        writer.writerow(output_row)


def party_votes(input_path, output_path):
    with \
            open(input_path) as input_csv, \
            open(output_path, 'w') as output_csv:
        regions_reader = csv.DictReader(input_csv)
        writer = csv.DictWriter(output_csv, fieldnames=md.field_party)
        writer.writeheader()
        output_row = {}

        vote_id = 1
        for i, row in enumerate(regions_reader):
            if output_row.get(md.field_party[1]) == row.get(md.field_party[1]):
                output_row = current_region(output_row, row)
            else:
                output_row, vote_id = new_region(vote_id, output_row, writer,
                                                 row)

            if not i % 1e6:
                print('Processing:', i, '...')

            # if i > 4:
            #     break

        writer.writerow(output_row)


def current_region(row, data):
    for value in md.field_party[3:]:
        cur_value = row.get(value) or 0
        raw_value = int(data.get(value) or 0)
        row.update({value: cur_value + raw_value})
    return row


def current_candidate(row, data):
    value = md.field_candidates[9]
    cur_value = row.get(value) or 0
    raw_value = int(data.get(value) or 0)
    row.update({value: cur_value + raw_value})
    return row


def new_region(vote_id, row, writer, data):
    if row:
        writer.writerow(row)
    row = {
        md.field_party[0]: vote_id,
        md.field_party[1]: data.get(md.field_party[1]),
        md.field_party[2]: data.get(md.field_party[2])
    }
    vote_id += 1
    return row, vote_id


def new_candidate(vote_id, row, writer, data):
    if row:
        writer.writerow(row)
    row = {}
    for value in md.field_candidates[1:9]:
        row.update({
            value: data.get(value)
        })
    row.update({
        'LICZBA GŁOSÓW': 1
    })
    row.update({
        'ID': vote_id
    })
    vote_id += 1
    return row, vote_id


if __name__ == "__main__":
    main()
