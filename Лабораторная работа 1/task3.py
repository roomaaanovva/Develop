list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

center_index = len(list_players) // 2

first_team = list_players[:center_index]
second_team = list_players[center_index:]

print("Первая команда:", first_team)
print("Вторая команда:", second_team)