import csv
import metadata as md
from time import time


def main():
    input_path = './splited_data.csv'
    output_path = './joined_data.csv'

    start_time = time()

    party_votes(input_path, output_path)

    end_time = time()

    print('--- generating records took', (end_time - start_time), 'seconds ---')


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


if __name__ == "__main__":
    main()
