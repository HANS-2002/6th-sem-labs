import pandas as pd

marks = pd.read_excel('D:\codes\college\TTL\class 9\\attendanceChanged.xlsx')

displayFrame = pd.DataFrame(columns=['Sl. No.', 'Roll Number', 'Score'])

for index, row in marks.iterrows():
    score = max(int(row['QUIZ-1  (SCORE/ ABS)']) if row['QUIZ-1  (SCORE/ ABS)'] != 'ABS' else 0, int(row['QUIZ-2  (SCORE/ ABS)']) if row['QUIZ-2  (SCORE/ ABS)'] != 'ABS' else 0)
    newDataFrame = pd.DataFrame({'Sl. No.': [0], 'Roll Number': row['ROLL NO.'], 'Score': score})
    displayFrame = pd.concat([displayFrame, newDataFrame])

displayFrame.sort_values('Score', ascending=False, inplace=True)
displayFrame['Sl. No.'] = range(1, displayFrame.shape[0] + 1)
displayFrame.set_index('Sl. No.', inplace=True)
print(displayFrame.head(10))
