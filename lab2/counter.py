def count_filtered_titles(dat_file, target_genres):
    total_titles = 0
    matching_titles = 0

    with open(dat_file, 'r', encoding='utf-8') as file:
        next(file)  # Skip header
        for line in file:
            total_titles += 1
            columns = line.strip().split('\t')
            if len(columns) < 3:
                continue  # Skip malformed lines
            genres = columns[2].split(',')
            genres = {g.strip() for g in genres}
            # Check if any of the target genres are present
            if any(genre in genres for genre in target_genres):
                matching_titles += 1

    return matching_titles

# Example usage
dat_file = 'anime_info.dat'  # Replace with your .dat file path
target_genres = {
    'Comedy', 'Action', 'Sci-Fi', 'Adventure', 'Fantasy', 'Drama', 'Shounen',
    'Romance','Shoujo', 'Seinen'
}

matching_titles = count_filtered_titles(dat_file, target_genres)
print(f"Number of titles with at least one of the specified genres: {matching_titles}")
