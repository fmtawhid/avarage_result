# example/views.py
from datetime import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    print('Your Diploma Avarage result Calculation')
sem = int(input('Enter your Semester Number: '))

if sem == 1:
    print('your result only one')
elif sem == 2:
    first = float(input('enter your First semester result: '))  # 5%
    second = float(input('enter your second semester result: '))  # 5%

    first_cal = (first * 5) / 100
    second_cal = (second * 5) / 100


    result = first_cal + second_cal 

    print("Your Diploma result is: " + str(result))
elif sem == 3:
    first = float(input('enter your First semester result: '))  # 5%
    second = float(input('enter your second semester result: '))  # 5%
    third = float(input('enter your third semester result: '))  # 5%


    first_cal = (first * 5) / 100
    second_cal = (second * 5) / 100
    third_cal = (third * 5) / 100


    result = first_cal + second_cal + third_cal 

    print("Your Diploma result is: " + str(result))
    
elif sem == 4:
    first = float(input('enter your First semester result: '))  # 5%
    second = float(input('enter your second semester result: '))  # 5%
    third = float(input('enter your third semester result: '))  # 5%
    forth = float(input('enter your forth semester result: '))  # 10%


    first_cal = (first * 5) / 100
    second_cal = (second * 5) / 100
    third_cal = (third * 5) / 100
    forth_cal = (forth * 10) / 100


    result = first_cal + second_cal + third_cal + forth_cal 

    print("Your Diploma result is: " + str(result))

elif sem == 5:
    first = float(input('enter your First semester result: '))  # 5%
    second = float(input('enter your second semester result: '))  # 5%
    third = float(input('enter your third semester result: '))  # 5%
    forth = float(input('enter your forth semester result: '))  # 10%
    fifth = float(input('enter your fifth semester result: '))  # 15%


    first_cal = (first * 5) / 100
    second_cal = (second * 5) / 100
    third_cal = (third * 5) / 100
    forth_cal = (forth * 10) / 100
    fifth_cal = (fifth * 15) / 100


    result = first_cal + second_cal + third_cal + forth_cal + fifth_cal

    print("Your Diploma result is: " + str(result))

elif sem == 6:
    first = float(input('enter your First semester result: '))  # 5%
    second = float(input('enter your second semester result: '))  # 5%
    third = float(input('enter your third semester result: '))  # 5%
    forth = float(input('enter your forth semester result: '))  # 10%
    fifth = float(input('enter your fifth semester result: '))  # 15%
    six = float(input('enter your six semester result: '))  # 20%

    first_cal = (first * 5) / 100
    second_cal = (second * 5) / 100
    third_cal = (third * 5) / 100
    forth_cal = (forth * 10) / 100
    fifth_cal = (fifth * 15) / 100
    six_cal = (six * 20) / 100


    result = first_cal + second_cal + third_cal + forth_cal + fifth_cal + six_cal 

    print("Your Diploma result is: " + str(result))
    
elif sem == 7:
    first = float(input('enter your First semester result: '))  # 5%
    second = float(input('enter your second semester result: '))  # 5%
    third = float(input('enter your third semester result: '))  # 5%
    forth = float(input('enter your forth semester result: '))  # 10%
    fifth = float(input('enter your fifth semester result: '))  # 15%
    six = float(input('enter your six semester result: '))  # 20%
    seven = float(input('enter your seven semester result: '))  # 25%


    first_cal = (first * 5) / 100
    second_cal = (second * 5) / 100
    third_cal = (third * 5) / 100
    forth_cal = (forth * 10) / 100
    fifth_cal = (fifth * 15) / 100
    six_cal = (six * 20) / 100
    seven_cal = (seven * 25) / 100

    result = first_cal + second_cal + third_cal + forth_cal + fifth_cal + six_cal + seven_cal 

    print("Your Diploma result is: " + str(result))
    
elif sem == 8:
    first = float(input('enter your First semester result: '))  # 5%
    second = float(input('enter your second semester result: '))  # 5%
    third = float(input('enter your third semester result: '))  # 5%
    forth = float(input('enter your forth semester result: '))  # 10%
    fifth = float(input('enter your fifth semester result: '))  # 15%
    six = float(input('enter your six semester result: '))  # 20%
    seven = float(input('enter your seven semester result: '))  # 25%
    eight = float(input('enter your eight semester result: '))  # 10%

    first_cal = (first * 5) / 100
    second_cal = (second * 5) / 100
    third_cal = (third * 5) / 100
    forth_cal = (forth * 10) / 100
    fifth_cal = (fifth * 15) / 100
    six_cal = (six * 20) / 100
    seven_cal = (seven * 25) / 100
    eight_cal = (eight * 10) / 100

    result = first_cal + second_cal + third_cal + forth_cal + fifth_cal + six_cal + seven_cal + eight_cal

    print("Your Diploma result is: " + str(result))
    
else:
    print('Your Semester in not find')

    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
