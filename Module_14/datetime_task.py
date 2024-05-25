from datetime import datetime


class SuperDate(datetime):


    TIME_OF_DAY = {
        'Morning': (6, 12),
        'Day': (12, 18),
        'Evening': (18, 0),
        'Night': (0, 6),
    }

    SEASONS = {
        1: 'Winter',
        2: 'Winter',
        3: 'Spring',
        4: 'Spring',
        5: 'Spring',
        6: 'Summer',
        7: 'Summer',
        8: 'Summer',
        9: 'Autumn',
        10: 'Autumn',
        11: 'Autumn',
        12: 'Winter',
    }

    def get_season(self):
        return self.SEASONS[self.month]

    def get_season_2(self):
        current_month = self.month
        if 1 <= current_month < 3 or current_month == 12:
            return 'Winter'
        elif 3 <= current_month < 6:
            return 'Spring'
        elif 6 <= current_month < 9:
            return 'Summer'

        return 'Autumn'

    def get_time_of_day(self):
        hour = self.hour
        for time, (start, end) in self.TIME_OF_DAY.items():
            if start <= hour < end:
                return time


if __name__ == '__main__':
    superDate = SuperDate(2024, 5, 5, 2)
    print('season -> ', superDate.get_season())
    print('season 2 -> ', superDate.get_season_2())
    print('time of day -> ', superDate.get_time_of_day())
