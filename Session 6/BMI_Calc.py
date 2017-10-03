def bmi_calc():
    height = input('What is your height (in)?')
    height= int(height)
    weight = input('What is your weight (lbs)?')
    weight = int(weight)
    bmi = 703*(weight/(height**2))
    print('Your bmi is {:.1f}'.format(int(bmi)))
    if bmi>=30:
        print("You fat shit, you're obese")
    elif bmi>=25:
        print("You still overweight")
    elif bmi>=18.5:
        print("Damn you normal af")
    elif bmi<18.5:
        print("Eat something for once")

bmi_calc()