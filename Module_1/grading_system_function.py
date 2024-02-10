'''def grade(student_answers):
    answer_key = ["A", "B", "C", "D", "E"]
    score=0

  for i in range(len(student_answers)):
        if student_answers[i]== answer_key[i]:
          score_obtained = score_obtained+1
        else:
          score_obtained = score_obtained
  return score_obtained
score = grade(student_answers)
print(score_obtainedscore_obtained)'''

def grade_test(student_answers):

    answer_key = ["A", "B", "C", "D", "E"]
    score = 0

    for i in range(len(student_answers)):
        if student_answers[i] == answer_key[i]:
            score += 1  # Increment the score if the answer is correct
        else:
            score += 0  # No change in score if the answer is incorrect

    return score

score = grade_test(student_answers)
print(score)