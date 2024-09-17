# Использование %:
team1_num = 5
team2_num = 6

str_1 = "В команде Мастера кода участников: %d !" % (team1_num)
str_2 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)

print(str_1)
print(str_2)
# Использование format():
score_2 = 42
team1_time = 18015.2

str_3 = "Команда Волшебники данных решила задач: {} !".format(score_2)
str_4 = "Волшебники данных решили задачи за {} с !".format(team1_time)

print(str_3)
print(str_4)
# Использование f - строк:
score_1 = 40
score_2 = 42
challenge_result = 'Победа команды Волшебники данных!'
tasks_total = 82
time_avg = 350.4

str_5 = f"Команды решили {score_1} и {score_2} задач."
str_6 = f"Результат битвы: {challenge_result}"
str_7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."

print(str_5)
print(str_6)
print(str_7)
