import csv
import re

def extract_data(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile, delimiter='\t')
        fieldnames = ['Book Id', 'Extracted REX Comments', 'Extracted EX Comments', 'Extracted A Comments']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()

        pattern = re.compile(r'\b(REX\d+|EX\d+|A\d+)\b', re.IGNORECASE)

        for row in reader:
            book_id = row.get('Book Id', '')
            comments = row.get('Comment', '').split()

            extracted_rex = [match for comment in comments for match in pattern.findall(comment) if match.upper().startswith('REX')]
            extracted_ex = [match for comment in comments for match in pattern.findall(comment) if match.upper().startswith('EX')]
            extracted_a = [match for comment in comments for match in pattern.findall(comment) if match.upper().startswith('A')]

            writer.writerow({
                'Book Id': book_id,
                'Extracted REX Comments': ' '.join(extracted_rex),
                'Extracted EX Comments': ' '.join(extracted_ex),
                'Extracted A Comments': ' '.join(extracted_a)
            })

# Example usage
extract_data('librarything_mkfarchives.tsv', 'output.tsv')
