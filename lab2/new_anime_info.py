import csv

def process_anime_dataset(input_file, output_file):
    target_genres = {
        'Comedy', 'Action', 'Sci-Fi', 'Adventure', 'Fantasy',
        'Drama', 'Shounen', 'Romance', 'Shoujo', 'Seinen'
    }

    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8', newline='') as outfile:

        reader = csv.DictReader(infile, delimiter='\t')
        fieldnames = ['anime_ids', 'type', 'episodes', 'rating', 'members'] + list(target_genres)
        writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()

        for row in reader:
            genres = set(g.strip() for g in row['genre'].split(','))
            # Check if any target genre is present
            if not any(g in genres for g in target_genres):
                continue  # Skip if no target genre

            # Prepare the output row
            output_row = {
                'anime_ids': row['anime_ids'],
                'type': row['type'],
                'episodes': row['episodes'],
                'rating': row['rating'],
                'members': row['members']
            }
            # Add genre columns (1/0)
            for genre in target_genres:
                output_row[genre] = 1 if genre in genres else 0

            writer.writerow(output_row)

# Example usage
input_file = 'anime_info.dat'   # Replace with your input file path
output_file = 'filtered_anime.dat'  # Replace with your desired output file path
process_anime_dataset(input_file, output_file)
