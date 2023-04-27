import pandas as pd

attendanceFrame = pd.read_excel('D:\codes\college\TTL\class 9\\attendance.xlsx')
quizFrame = pd.read_excel('D:\codes\college\TTL\class 9\quiz.xlsx')

for index, row in attendanceFrame.iterrows():
    curQuizFrame = quizFrame[row['ROLL NO.'] == quizFrame['ROLL']]
    quiz1Array = curQuizFrame[curQuizFrame['Timestamp'] < pd.Timestamp(2023, 2, 14, 0, 0, 0)]['Score'].values
    quiz2Array = curQuizFrame[curQuizFrame['Timestamp'] >= pd.Timestamp(2023, 2, 14, 0, 0, 0)]['Score'].values
    attendanceFrame.loc[index, 'QUIZ-1  (SCORE/ ABS)'] = quiz1Array[0] if len(quiz1Array) else 'ABS'
    attendanceFrame.loc[index, 'QUIZ-2  (SCORE/ ABS)'] = quiz2Array[0] if len(quiz2Array) else 'ABS'

attendanceFrame.to_excel('D:\codes\college\TTL\class 9\\attendanceChanged.xlsx')
