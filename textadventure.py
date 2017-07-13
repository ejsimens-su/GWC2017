print('Horoscope Teller')
print('*********************************')
name = input('What is your name?')

print('Welcome to Horoscope Teller, %s!' % (name))

y_n = input('Do you know your sign? Answer Y/N:')

if y_n == 'Y':
    horoscope_question_one = input('Great! Would you like to know your horoscope?')
    if horoscope_question_one == 'Y':
        print('Horoscopeeeeeeee')
    else:
        print('Ok. Thanks for playing!')

if y_n == 'N':
    month = input('When is your birth month?')
    day = int(input('And, what day of the month were you born on?'))
    if month == 'march' and day >= 20:
        sign = 'aries'
    if month == 'april' and day <= 20:
        sign = 'aries'
    horoscope_question = input('Your sign is %s! Would you like to know your horoscope? Answer Y/N:' % (sign))
    if horoscope_question == 'Y':
        print('Horoscopeeeeeeee')
    else:
        print('Ok. Thanks for playing!')
    #else:
        #sign = input('What is your sign?')
        #get horoscope API
        #print(horoscope)
