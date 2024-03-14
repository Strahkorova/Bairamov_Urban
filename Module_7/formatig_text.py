class team():
    list_team_name = []
    dict_team = {}
    dict_score = {}
    dict_time = {}

    def team_name(self):
        name = input("Введите название команды - ")
        team_num = input("Введите количество участников - ")
        # if 4 < int(team_num) < 21:
        #     print('В команде %s, %s участников' % (name, team_num))
        # else:
        #     if team_num[-1] == '1':
        #         print('В команде %s, %s участник' % (name, team_num))
        #     elif team_num[-1] == '2' or team_num[-1] == '3' or team_num[-1] == '4':
        #         print('В команде %s, %s участника' % (name, team_num))
        #     else:
        #         print('В команде %s, %s участников' % (name, team_num))
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
            team.dict_score[i] = score
            team.dict_time[i] = time


class play(team):

    list_1 = team.list_team_name
    dict_sc = team.dict_score
    dict_t = team.dict_time
    def result(self):
        score_1 = float(self.dict_sc[self.list_1[0]])
        score_2 = float(self.dict_sc[self.list_1[1]])
        time_1 = float(play.dict_time[self.list_1[0]])
        time_2 = float(play.dict_time[self.list_1[1]])
        if score_1 > score_2:
            print('Команда - {0} победила!'.format(self.list_1[0]))
        elif score_1 < score_2:
            print('Команда - {0} победила!'.format(self.list_1[1]))
        else:
            time_avg_1 = time_1/score_1
            time_avg_2 = time_2score_2
            if time_avg_1 > time_avg_2:
                print('Команда {0} победила затратив на одну задачу - {1:.3f}'.format(self.list_1[0], time_avg_1))
            else:
                print('Команда {0} победила затратив на одну задачу - {1:.3f}'.format(self.list_1[1], time_avg_2))



t = play()
t.team_name()
t.team_name()
t.team_score_and_time()
t.result()

