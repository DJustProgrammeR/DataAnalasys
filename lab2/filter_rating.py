import csv

def extract_anime_ids(filtered_anime_file):
    anime_ids = set()
    with open(filtered_anime_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            anime_ids.add(row['anime_ids'])
    return anime_ids

def filter_ratings(rating_file, output_file, anime_ids):
    with open(rating_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8', newline='') as outfile:

        reader = csv.DictReader(infile, delimiter='\t')
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames, delimiter='\t')
        writer.writeheader()

        for row in reader:
            if row['Anime_ID'] in anime_ids:
                writer.writerow(row)


filtered_anime_file = 'filtered_anime.dat'
rating_file = 'anime_ratings.dat'
output_file = 'filtered_ratings.dat'

anime_ids = extract_anime_ids(filtered_anime_file)
filter_ratings(rating_file, output_file, anime_ids)
