from collections import defaultdict

def count_genres(dat_file):
    genre_counts = defaultdict(int)

    with open(dat_file, 'r', encoding='utf-8') as file:
        # Skip the header line
        next(file)
        for line in file:
            columns = line.strip().split('\t')
            if len(columns) < 3:
                continue  # Skip malformed lines
            genres = columns[2]
            for genre in genres.split(','):
                genre_counts[genre.strip()] += 1

    return genre_counts

# Example usage
dat_file = 'anime_info.dat'  # Replace with your .dat file path
genre_counts = count_genres(dat_file)

# Print the genre counts
print("Genre counts:")
for genre, count in sorted(genre_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{genre}: {count}")
