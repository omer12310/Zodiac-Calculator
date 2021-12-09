Name=input("Enter Your Name:")
print ("Hello",str(Name))
print("This Program Will determine Your Zodiac Sign")
def zodiac():
        day = int(input("Enter Day of birth: "))
        month = input("Enter month of birth: ")
        if month == 'december':
            zodiac = 'Sagittarius' if (day < 22) else 'capricorn'

        elif month == 'january':
            zodiac = 'Capricorn' if (day < 20) else 'aquarius'

        elif month == 'february':
            zodiac = 'Aquarius' if (day < 19) else 'pisces'

        elif month == 'march':
            zodiac = 'Pisces' if (day < 21) else 'aries'

        elif month == 'april':
            zodiac = 'Aries' if (day < 20) else 'taurus'

        elif month == 'may':
            zodiac = 'Taurus' if (day < 21) else 'gemini'

        elif month == 'june':
            zodiac = 'Gemini' if (day < 21) else 'cancer'

        elif month == 'july':
            zodiac = 'Cancer' if (day < 23) else 'leo'

        elif month == 'august':
            zodiac = 'Leo' if (day < 23) else 'virgo'

        elif month == 'september':
            zodiac = 'Virgo' if (day < 23) else 'libra'

        elif month == 'october':
            zodiac = 'Libra' if (day < 23) else 'scorpio'

        elif month == 'november':
            zodiac = 'scorpio' if (day < 22) else 'sagittarius'
        else:
            print("You Entered Wrong Month")
        print("Your Zodiac Sign is", zodiac)

zodiac()

print("Press 1 if you wanna proceed")
print("Press 2 if you want this process to terminate")
choice = int(input("Enter Choice"))
if choice == 1:
    zodiac()
elif choice == 2:
    print ("The program terminates here")