from csv import reader
from sys import argv

def convert_csv_to_list(file_name):
    """Converts dataset from csv file to list"""
    with open(file_name, encoding="utf8") as data_source:
        apps_data = list(reader(data_source))
    return apps_data

def calculate_average_rating(apps_data, genres_list):
    """Calculates average rating for input genres"""
    ratings = []
    for app in apps_data[1:]:
        genre = app[11]
        user_rating = float(app[7])
        if genre in genres_list:
            ratings.append(user_rating)

    average_rating = sum(ratings) / len(ratings)
    return average_rating


def create_output_message(genres_list, average_rating):
    """Returns output message with average rating info"""
    output_message = "The genres analyzed are: \n"
    for genre in genres_list:
        output_message += "- " + genre + "\n"
    output_message += f"The average rating is {average_rating:.2f}"
    return output_message

if __name__ == '__main__':
    script_name, *genres_list = argv
    apps_data = convert_csv_to_list('AppleStore.csv')
    average_rating = calculate_average_rating(apps_data, genres_list)
    output_message = create_output_message(genres_list, average_rating)
    print(output_message)
    with open('genres_average_rating.txt', mode='w', encoding="utf8") as output_file:
        output_file.write(output_message)