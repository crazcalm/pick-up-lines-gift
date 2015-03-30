import argparse
import sqlite3

conn = sqlite3.connect("sql/test.db")
c = conn.cursor()

def get_pickupline():
    c.execute("SELECT * FROM pickuplines ORDER BY RANDOM() LIMIT 1;")
    print(c.fetchone()[0])
    conn.close()

def get_comeback():
    c.execute("SELECT * FROM comebacks ORDER BY RANDOM() LIMIT 1;")
    print(c.fetchone()[0])
    conn.close()

def add_pickupline(line):
    try:
        c.execute("INSERT INTO pickuplines VALUES (?)", (line,))
        conn.commit()
        conn.close()
        print("Successfully added: ", line)
    except:
        print("Failed to add: ", line)

def add_comeback(line):
    try:
        c.execute("INSERT INTO comebacks VALUES (?)", (line,))
        conn.commit()
        conn.close()
        print("Successfully added: ", line)
    except:
        print("Failed to add: ", line)

def main(args):
    if args.comeback:
        get_comeback()
    elif args.add_comeback:
        add_comeback(args.add_comeback)
    elif args.add_pickupline:
        add_pickupline(args.add_pickupline)
    else:
        get_pickupline()

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

main(args)


if __name__ == '__main__':
    pass