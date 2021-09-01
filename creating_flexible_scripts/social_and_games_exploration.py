from csv import reader

with open('AppleStore.csv', encoding="utf8") as data_source:
    apps_data = list(reader(data_source))

target_ratings = []
for app in apps_data[1:]:
    genre = app[11]
    user_rating = float(app[7])
    if genre == 'Social Networking' or genre == 'Games':
        target_ratings.append(user_rating)

average_rating = sum(target_ratings) / len(target_ratings)
message = f"The average rating of Social Netowrking and Games is {average_rating:.2f}"
print(message)


