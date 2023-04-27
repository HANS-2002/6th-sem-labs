# Using class in python add two times and display the result.
class time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        second = self.second+other.second
        minute = self.minute+other.minute + second // 60
        hour = self.hour+other.hour + minute // 60
        minute %= 60
        second %= 60
        hour %= 24
        return time(hour, minute, second)

    def __str__(self):
        return "{}:{}:{}".format(self.hour if self.hour >= 10 else '0' + str(self.hour),
                                 self.minute if self.minute >= 10 else '0' + str(self.minute),
                                 self.second if self.second >= 10 else '0' + str(self.second))


t1 = time(int(input('Hour part of 1st time: ')),
          int(input('Minute part of 1st time: ')),
          int(input('Second part of 1st time: ')))
t2 = time(int(input('Hour part of 2nd time: ')),
          int(input('Minute part of 2nd time: ')),
          int(input('Second part of 2nd time: ')))
sumt = t1+t2
print(f'Sum of {t1} and {t2} is {sumt}')
