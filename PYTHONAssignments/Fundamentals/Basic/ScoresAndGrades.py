import random



for i in range(1,11):
    random_num = random.randint(60,100)
    if (random_num <=100) & (random_num >=90):
        print random_num, "Your Grade is A"

    elif (random_num <=89) & (random_num >=80):
        print random_num, "Your Grade is B"

    elif (random_num <=79) & (random_num >=70):
        print random_num, "Your Grade is C"

    else:
        print random_num, "Your Grade is D"

