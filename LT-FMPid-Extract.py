import csv
import re

def extract_data(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile, delimiter='\t')
        fieldnames = ['Book Id', 'Extracted Comments']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()

        pattern = re.compile(r'\b(REX\d+|EX\d+|A\d+)\b', re.IGNORECASE)

        for row in reader:
            book_id = row.get('Book Id', '')
            comments = row.get('Comment', '').split()

            for comment in comments:
                matches = pattern.findall(comment)
                for match in matches:
                    writer.writerow({'Book Id': book_id, 'Extracted Comments': match.upper()})

# Example usage
extract_data('librarything_mkfarchives.tsv', 'output.tsv')