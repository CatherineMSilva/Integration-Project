# Catherine Silva
"""Catherine's final integration project for COP1500"""

# This program was created to randomly generate different workouts and useful
# information regarding your time at the gym.
# It will first create some randomly generated workouts depending on the string
# or words attached to a specific muscle group that was identified
# Secondly, the program will ask questions regarding how long you have worked
# out and will calculate how many calories you have burned based on the input
# Third, the program will calculate how much more time you should workout
# Fourth, the program will calculate how many more/less days you should workout
# based on your current weekly days you input
# Fifth, the program will then create some calculations about your cardio
# habits
# based on the distance and time input
# And lastly, the program will calculate your necessary protein intake for the
# day based on body weight

import random


def good_input(msg):
    """This Function makes sure the user can only input a whole integer"""
    input_invalid = True
    good_int = 0
    while input_invalid:
        try:
            good_int = int(input(msg))
            input_invalid = False
        except ValueError:
            print("Error. try inputting a whole number.")
    return good_int


def introduction():
    """This function introduces the program to the user"""
    print("Hello there! I hope you're ready for your workout!")
    print("Here are some randomly generated workouts for you to try based "
          "on the muscle group you want to focus on.")
    print("your options are: 'bicep', 'legs', 'chest', or 'back'")


def type_of_workout():
    """This function contains the list of possible options for a workout"""
    bicep = ("Barbell bicep curl", "Cable hammer curls", "chin ups",
             "Close grip lat pull downs", "pull ups", "preacher curls",
             "decline curl")
    legs = ("Leg Press", "Squats", "Bulgarian Split Squats", "leg curl",
            "Dead Lift", "Good mornings", "Weighted lunges", "Hip thrusts")
    chest = ("Incline bench press", "Chest fly's", "Push ups",
             "Single arm press", "dumbbell pull overs", "dumbbell bench"
                                                        "press",
             "seated chest press")
    back = ("Barbell rows", "Cable rows", "Single arm dumbbell rows",
            "Pull ups, Delt fly's", "Straight arm pulldowns",
            "Weighted hyper-extensions")

    workout_choice = input("\nwhat muscle group would you like to focus on? :")
    if workout_choice == "bicep":
        for x in range(3):
            bicep_workout = random.choice(bicep)
            print(bicep_workout)
    elif workout_choice == "legs":
        for x in range(3):
            leg_workout = random.choice(legs)
            print(leg_workout)
    elif workout_choice == "chest":
        for x in range(3):
            chest_workout = random.choice(chest)
            print(chest_workout)
    elif workout_choice == "back":
        for x in range(3):
            back_workout = random.choice(back)
            print(back_workout)
    else:
        print("Sorry, that input was invalid. Please try again.")
        type_of_workout()


# Total calories burned
def calories_burned(minutes_of_workout):
    """This function calculates the total calories burned by user"""
    calories_burned_calculation = minutes_of_workout * 6.16
    return calories_burned_calculation


# Multiplication was used to calculate the calories burned from the integer
# input of the user and the average calories burned per minute for someone
# of 135 pounds.


def minutes_left_of_workout(minutes_of_workout):
    """This function calculates the minutes left for users workout"""
    while minutes_of_workout < 90:
        minutes_left = 90 - minutes_of_workout
        print("You have", minutes_left, "minutes left of your workout",
              sep="  ")
        break
    while minutes_of_workout == 90:
        print("you have completed your daily workout goal! Congrats!")
        break
    while minutes_of_workout > 90:
        print("You have exceeded your daily workout goal, feel free to "
              "finish your workout at anytime.")
        break


# The "sep =" function is used to replace the space that would usually be
# made with the comma, with something else.
# In this case I just added an empty space between the string and the integer.


def num_of_workout_days():
    """This function calculates the correct number of days needed for a
    sufficient workout schedule"""
    num_of_days = good_input("\nHow many days of the week do you workout? : ")
    days_input = num_of_days % 5
    # The modulus function is used to find the remainder of an integer.
    # In this case, the remainder of the two integers that are being divided
    # will yield how many more/less days the user has of their workout week.
    num_of_days_left = 5 - days_input
    # Integer subtraction between the number assigned to 5 and "days_Input".
    if num_of_days < 5:
        print("It is recommended you workout", num_of_days_left,
              "more days to see better progress", end=".")
    # The "end =" function is used to add something to the end of your print
    # statement. In this case i added a period.
    if num_of_days > 5 or num_of_days == 5:
        print("It is recommended you only workout 5 days a week.\nAllow your "
              "body to rest!")


# If function is used to create outputs based on true/false statements. In this
# case, the print statements will only be shown if the if statement above
# it is true.

def cardio_calculations():
    """This function calculates the time per mile for the users run"""
    cardio_miles = good_input("\n\nHow much did you run today? "
                              "(distance in miles) : ")
    cardio_time = good_input("How long did you run for? (time in minutes) : ")
    time_per_mile = cardio_time / cardio_miles
    print("Your time per mile is ", time_per_mile, "min/mile")
    print("keep up the good work!              " * 2)


# The "* 2" function in this case is being applied to a string which will
# yield the string in "" to be printed twice (for emphasis and excitement).


# protein Intake
def protein_intake():
    """This function calculates the protein intake needed based on body
    weight"""
    print(
        "\nWhat a great workout you had! Don't forget to eat the necessary"
        " amount of protein to catalyze muscle growth.")
    body_weight = good_input("What is your current body weight (lbs)?: ")
    grams_protein = (.45 ** 2)
    initial_protein_intake = grams_protein * body_weight
    rounded_protein_intake = initial_protein_intake // 1
    # The "//" function is used to divide the float by one and
    # transforms it into a non decimal integer after the calculation is made.
    # I chose to use this function because it makes the protein
    # intake output a non-decimal integer
    print("You should be eating around ", rounded_protein_intake,
          "grams of protein daily", end=".")


def reflections():
    """This function asks the user to reflect on the workout they completed"""
    reflection_answer = input("\n\nDid you have a good workout?: ")
    if reflection_answer == "yes":
        print("Great! Make sure to get some rest and crush your next workout!")
    elif reflection_answer == "no":
        print("That's okay, write down some ways you can try to push "
              "yourself next time and try again tomorrow!")
    else:
        print("Error, please try answering with 'yes' or 'no'")
        reflections()


def main():
    """This function puts all previous functions together allowing the
    program to run"""
    introduction()
    type_of_workout()
    minutes_of_workout = good_input("\nHow many minutes have you worked out "
                                    "so far? : ")
    calories_calculation = calories_burned(minutes_of_workout)
    print("you've burned", calories_calculation,
          "calories so far! keep up the good work!")
    minutes_left_of_workout(minutes_of_workout)
    num_of_workout_days()
    cardio_calculations()
    protein_intake()
    reflections()


# Call To Main
main()

# Citation:
# https://www.w3schools.com/python/python_conditions.asp
# https://www.tutorialspoint.com/generating-random-number-list-in-python
# https://www.codegrepper.com/code-examples/python/
# how+to+generate+random+words+in+python
# https://www.healthline.com/nutrition/eat-after-workout#:~:text=It'
# s%20recommended%20that%20you%20consume,after%20a%20workout%20(%201%20).
# https://www.webmd.com/diet/features/water-for-weight-loss-diet#1
# https://sites.google.com/site/profvanselow/course/cop-1500
