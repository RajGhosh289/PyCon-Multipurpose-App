def calculator():
    weight = int(input("Enter you weight in lbs or Kgs: "))
    conversion_type = input("Convert To: (1)Lbs or (2)Kg: ")

    if conversion_type.startswith('1'):
        print('Your weight is ' + str(weight * 2.20) + ' pounds')
    elif conversion_type.startswith('2'):
        print('Your weight is ' + str(weight / 2.20) + ' kilos')
    else:
        print("something went wrong")