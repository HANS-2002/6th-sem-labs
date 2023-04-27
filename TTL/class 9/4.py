import pandas as pd

answers = pd.read_excel('D:\codes\college\TTL\class 9\\quizAnswers.xlsx')
answers = answers.to_dict('records')
quizFrame = pd.read_excel('D:\codes\college\TTL\class 9\\quiz.xlsx')

displayFrame = pd.DataFrame(columns=['Q. No.', 'No. of Students Answered correctly',
                            'No. of Students Answered incorrectly', 'Difficulty Level(%)'])
quizFrame = quizFrame[quizFrame['Timestamp']
                      < pd.Timestamp(2023, 2, 14, 0, 0, 0)]

for ans in answers:
    correct = quizFrame[quizFrame[ans['Q. No.']] == ans['Answer']].shape[0]
    incorrect = quizFrame[quizFrame[ans['Q. No.']] != ans['Answer']].shape[0]
    displayFrame = pd.concat([displayFrame, pd.DataFrame({'Q. No.': [ans['Q. No.']], 'No. of Students Answered correctly': [correct],
                                                          'No. of Students Answered incorrectly': [incorrect], 'Difficulty Level(%)': [incorrect / (correct + incorrect) * 100]})], ignore_index=True)

displayFrame.sort_values('Difficulty Level(%)', ascending=False, inplace=True)
print(displayFrame)
