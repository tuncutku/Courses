from database import add_entry, get_entries, create_table

menu = """Please select of the following options:
1- Add new entry for today
2- View entries
3- Exit
Your selection: 
"""

welcome = "welcome to programming diary!"

print(welcome)

create_table()


def promt_new_entry():
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the date: ")
    add_entry(entry_content, entry_date)


def view_entries(entries):
    for entry in entries:
        print("{}\n{}\n\n".format(entry["content"], entry["date"]))


while (user_input := input(menu)) != "3":
    if user_input == "1":
        promt_new_entry()

    elif user_input == "2":
        view_entries(get_entries())
    else:
        print("Invalid input, please insert 1, 2 or 3")

