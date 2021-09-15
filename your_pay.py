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
