import argparse
import sqlite3
import os
import sys


# Lets me know if I have change the working directory
DIR_CHANGE = False

# Checks to see if file was called from this directory
if os.path.dirname(__file__):
    cwd = os.getcwd()
    os.chdir(os.path.dirname(__file__))
    DIR_CHANGE = True    
else:   
    pass

# Connects to my pickup line database
conn = sqlite3.connect("sql/test.db")
c = conn.cursor()

def get_pickupline():
    """
    This function returns a random pickup line from the database.
    """
    c.execute("SELECT * FROM pickuplines ORDER BY RANDOM() LIMIT 1;")
    print(c.fetchone()[0])
    conn.close()

def get_comeback():
    """
    This function returns a random comeback line from the database.
    """
    c.execute("SELECT * FROM comebacks ORDER BY RANDOM() LIMIT 1;")
    print(c.fetchone()[0])
    conn.close()

def add_pickupline(line):
    """
    This function attempts to add a pickup line to the database.
    """
    try:
        c.execute("INSERT INTO pickuplines VALUES (?)", (line,))
        conn.commit()
        conn.close()
        print("Successfully added: ", line)
    except:
        print("Failed to add: ", line)

def add_comeback(line):
    """
    This function attempts to add a comeback line to the database.
    """
    try:
        c.execute("INSERT INTO comebacks VALUES (?)", (line,))
        conn.commit()
        conn.close()
        print("Successfully added: ", line)
    except:
        print("Failed to add: ", line)

def main(args):
    """
    This function takes the commandline arguements and calls the
    appropriate function.
    """
    if args.comeback:
        get_comeback()
    elif args.add_comeback:
        add_comeback(args.add_comeback)
    elif args.add_pickupline:
        add_pickupline(args.add_pickupline)
    else:
        get_pickupline()

# The constants used for the Commandline interface
DESCRIPTION = "A pickup line generator"
PROG = "pickupline"
EPILOG = "This project was built for my girlfriend (Jovanna Teran)"
COMEBACK = "Prints a comeback line to the screen."
ADD_PICKUPLINE = "Allows you to add a pickup line to the database."
ADD_COMEBACK = "Allows you to add a comeback line to the database."

# Command line logic
parser = argparse.ArgumentParser(description=DESCRIPTION, epilog=EPILOG,
    prog=PROG)

# This prevents users from passing multiple options at once
group1 = parser.add_mutually_exclusive_group()

# Adds the commandline options
group1.add_argument("-c","--comeback", dest="comeback", action="store_true",
        help=COMEBACK)
group1.add_argument("--add_pickupline",dest="add_pickupline",
        type=str, help=ADD_PICKUPLINE)
group1.add_argument("--add_comeback", dest="add_comeback",
        type=str, help=ADD_COMEBACK)

# Dictionary with the commandline inputs
args = parser.parse_args()


# Calling of the main funciton
main(args)

# Returns the cwd to what it was before this file was called
if DIR_CHANGE:
    os.chdir(cwd)
else:
    pass


if __name__ == '__main__':
    pass
