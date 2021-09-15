# try:
#     score = float(input('Enter Score: '))
# except:
#     print('Error: Enter number plase')
#     quit()

# if score <= 1 and score >= 0:
#     if score >= 0.9:
#         grade = 'A'
#     elif score >= 0.8:
#         grade = 'B'
#     elif score >= 0.7:
#         grade = 'C'
#     elif score >= 0.6:
#         grade = 'D'
#     else:
#         grade = 'F'
# else: grade = 'Error, plase enter number between 0 and 1'

# print(grade)
try:
    hrs = float(input('Enter Hours: '))
    rate = float(input('Enter rate: '))
except:
    print('Error, input number plz')
    quit()

def computepay(hours, rate):
    pay = 'Not a correct inputs'
    if hours > 40:
        pay = (((hours - 40) * (rate * 1.5)) + (40 * rate))
    elif hours > 0 and rate > 0:
        pay = hours * rate
    return pay

ur_pay = computepay(hrs, rate)
print(ur_pay)   