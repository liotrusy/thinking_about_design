from csv import reader

with open('AppleStore.csv', encoding="utf8") as data_source:
    apps_data = list(reader(data_source))

genres = []
for app in apps_data[1:]:
    genre = app[11]
    genres.append(genre)

genres = set(genres)
number_of_genres = len(genres)
result_message = f"There are {number_of_genres} unique genres in the dataset."
print(result_message)

with open('genres.txt', mode="w", encoding="utf8") as output_file:
    output_file.write(result_message)
    output_file.write("\n")
    output_file.write("Here is the list of genres: \n")
    for genre in genres:
        output_file.write(genre + "\n")
