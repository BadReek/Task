student1 = 'danila'
appraisals1 = [4, 5, 5, 4, 3, 4, 4, 5, 3, 5, 2]
quantity1 = 11

student2 = 'ilya'
appraisals2 = [4, 4, 5, 3, 5, 4, 3, 4, 4, 5, 5]
quantity2 = 11

student3 = 'george'
appraisals3 = [3, 5, 2, 4, 5, 2, 3, 4, 4, 2, 2]
quantity3 = 11

for sum_123 in appraisals1:
        total_sum1 = total_sum1 + sum_123
        print(total_sum1)
for sum_123 in appraisals2:
        total_sum2 = total_sum1 + sum_123
        print(total_sum2)
for sum_123 in appraisals3:
        total_sum3 = total_sum3 + sum_123
        print(total_sum3)

def average_score(student, appraisals, quantity):
    score = total_sum / quantity

    print('Средний бал по матиматике: ' + str(score))

    if score > 3:
        return student + 'молодец, хорошо учишься!'
    else:
        return student + 'тебе нужно подтянуть знания по матиматике!'

score1 = average_score(student1, appraisals1, quantity1)
score2 = average_score(student2, appraisals2, quantity2)
score3 = average_score(student3, appraisals3, quantity3)
print(score1)
print(score2)
print(score3)
