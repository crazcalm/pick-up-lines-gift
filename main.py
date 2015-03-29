import argparse

DESCRIPTION = "A pickup line generator"
EPILOG = "This project was built for my girlfriend (Jovanna Teran)"
COMEBACK = "Prints a comeback line to the screen."
ADD_PICKUPLINE = "Allows you to add a pickup line to the database."
ADD_COMEBACK = "Allows you to add a comeback line to the database."

parser = argparse.ArgumentParser(description=DESCRIPTION, epilog=EPILOG)

group1 = parser.add_mutually_exclusive_group()

group1.add_argument("-c","--comeback", dest="comeback", action="store_true",
        help=COMEBACK)
group1.add_argument("--add_pickupline",dest="add_pickupline",
        type=str, help=ADD_PICKUPLINE)

group1.add_argument("--add_comeback", dest="add_comeback",
        type=str, help=ADD_COMEBACK)

args = parser.parse_args()
print(args)