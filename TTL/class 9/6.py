import pandas as pd

marks = pd.read_excel('D:\codes\college\TTL\class 9\\attendanceChanged.xlsx')

marks.drop('Average Marks', axis=1, inplace=True)
marks.insert(6, 'Average Marks', 0)
marks.set_index('SL. NO.', inplace=True)

for index, row in marks.iterrows():
    score1 = int(row['QUIZ-1  (SCORE/ ABS)']) if row['QUIZ-1  (SCORE/ ABS)'] != 'ABS' else -1
    score2 = int(row['QUIZ-2  (SCORE/ ABS)']) if row['QUIZ-2  (SCORE/ ABS)'] != 'ABS' else -1
    avg = (score1 + score2) / 2 if score1 != -1 and score2 != -1 else max(score1, score2)
    marks.loc[index, 'Average Marks'] = avg

print(marks)
marks.to_excel('D:\codes\college\TTL\class 9\\attendanceChanged.xlsx')