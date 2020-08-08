"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:

question_file = open('questions.txt', 'r')
mock_list = [question.split('=') for question in question_file.read().splitlines()]
question_file.close()

score = 0
for question in mock_list:
    if int(question[1]) == int(input(f"{question[0]}=")):
        score += 1

result_file = open('result.txt', 'w')
result_file.write(f"Your final score is {score}/{mock_list.__len__()}.")
result_file.close()




