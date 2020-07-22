import requests


def find_the_smartest(names_list):
    dict_of_stats = {}
    for name in names_list:
        response = requests.get(f'https://www.superheroapi.com/api.php/2619421814940190/search/{name}')
        intelligence = response.json()['results'][0]['powerstats']['intelligence']
        dict_of_stats.update({name: int(intelligence)})
    highest_intel = 0
    name_of_hero = ''
    for name, stat in dict_of_stats.items():
        if stat > highest_intel:
            highest_intel = stat
            name_of_hero = name
    print(f'Самый умный супергерой: {name_of_hero} ({highest_intel} баллов)')


list_of_names = ['Thanos', 'Hulk', 'Captain America']
find_the_smartest(list_of_names)