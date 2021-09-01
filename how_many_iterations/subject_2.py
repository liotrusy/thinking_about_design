from csv import reader

with open('AppleStore.csv', encoding="utf8") as data_source:
    apps_data = list(reader(data_source))
    apps_data

price_point = 9
apps_above_price_point = []

n_apps_below_price_point = 0

for app in apps_data[1:]:
    price = float(app[4])
    if price > 9:
        rating = float(app[7])
        apps_above_price_point.append(rating)
    else:
        n_apps_below_price_point += 1
        
n_apps_more_9 = len(apps_above_price_point)
avg_rating = sum(apps_above_price_point) / n_apps_more_9