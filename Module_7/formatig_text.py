class team():
    list_team_name = []
    dict_team = {}
    dict_score = {}
    dict_time = {}
    list_time_arg = []

    def team_name(self):
        name = input("Введите название команды - ")
        team_num = input("Введите количество участников - ")
        if 4 < int(team_num) < 21:
            print('В команде %s, %s участников' % (name, team_num))
        else:
            if team_num[-1] == '1':
                print('В команде %s, %s участник' % (name, team_num))
            elif team_num[-1] == '2' or team_num[-1] == '3' or team_num[-1] == '4':
                print('В команде %s, %s участника' % (name, team_num))
            else:
                print('В команде %s, %s участников' % (name, team_num))
        team.list_team_name.append(name)
        team.dict_team[name] = team_num

    def team_all(self):
        dict = team.dict_team
        dict1 = team.dict_score
        dict2 = team.dict_time
        for command in dict:
            print('В команде - %s, количество участников = %s,' % (command, dict[command]),
                  'участники решили = {0} задач за {1} секунд'.format(dict1[command], dict2[command]))

    def team_score_and_time(self):
        list = team.list_team_name
        for i in list:
            score = input('Введите количество решенных задач командой {0} - '.format(i))
            time = input('Введите время за которое команда {0} решила задачи - '.format(i))
            self.dict_score[i] = score
            self.dict_time[i] = time
            self.list_time_arg.append(float(time)/float(score))

class rules():
    file_name = 'Правила.txt'
    def play_rules(self):
        with open(self.file_name, mode='r', encoding='utf8') as file:
            for line in file:
                print(line)
        print(file.closed)



class play(team, rules):

    def challenge_result(self):
        time_arg_1 = float(self.list_time_arg[0])
        time_arg_2 = float(self.list_time_arg[1])
        score_1 = float(self.dict_score[self.list_team_name[0]])
        score_2 = float(self.dict_score[self.list_team_name[1]])

        if time_arg_1 > time_arg_2 or time_arg_1 == time_arg_2 and score_1 > score_2:
            print('Команда {0} победила затратив на одну задачу - {1:.3f}'.format(self.list_team_name[0], time_arg_1))
        elif time_arg_1 < time_arg_2 or time_arg_1 == time_arg_2 and score_1 < score_2:
            print('Команда {0} победила затратив на одну задачу - {1:.3f}'.format(self.list_team_name[0], time_arg_1))
        else:
            task_total = score_1 + score_2
            time = (time_arg_1+time_arg_2)/2
            print('Команда {0} и {1} сиграли в ничью! Вместе они решили - {2:.2f} задачи и затратили '
                  'на решение одной задачи в среднем - {3:2f}'.format(self.list_team_name[0], self.list_team_name[1], task_total, time))

t = play()
t.play_rules()
t.team_name()
t.team_name()
t.team_score_and_time()
t.challenge_result()
t.team_all()




