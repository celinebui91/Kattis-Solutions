
while True:
    user_input = int(input())
    if user_input == -1:
        break;

    miles_total = 0
    hours_total = 0

    for i in range(0, user_input):

        # maps int with the splitted inputs and saves it to 2 variables
        miles, hours = map(int, input().split())

        miles_total += miles * (hours-hours_total)

        hours_total = hours

    print (f"{miles_total} miles")
