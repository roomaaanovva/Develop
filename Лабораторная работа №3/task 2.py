# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, sep=","):
  participants1 = group1.split(sep)
  participants2 = group2.split(sep)
  return sorted(set(participants1).intersection(set(participants2)))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, '|'))

# TODO Провеьте работу функции с разделителем отличным от запятой

