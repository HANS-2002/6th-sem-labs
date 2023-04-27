import pandas as pd

attendanceFrame = pd.read_excel('D:\codes\college\TTL\class 9\\attendanceChanged.xlsx')

print(attendanceFrame[(attendanceFrame['QUIZ-1  (SCORE/ ABS)'] == 'ABS') | (attendanceFrame['QUIZ-2  (SCORE/ ABS)'] == 'ABS')])