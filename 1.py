Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def input_error(func):
...     def wrapper(*args, **kwargs):
...         try:
...             return func(*args, **kwargs)
...         except KeyError:
...             return "Enter user name"
...         except ValueError:
...             return "Give me name and phone please"
...         except IndexError:
...             return "Contact not found"
... 
...     return wrapper
... 
... 
... def hello():
...     return "How can I help you?"
... 
... 
... @input_error
... def add_contact(command, contacts):
...     _, name, phone = command.split()
...     contacts[name] = phone
...     return f"Contact {name} added with phone {phone}"
... 
... 
... @input_error
... def change_contact(command, contacts):
...     _, name, phone = command.split()
...     contacts[name] = phone
...     return f"Phone number for {name} changed to {phone}"
... 
... 
... @input_error
... def phone(command, contacts):
...     _, name = command.split()
...     return f"Phone number for {name}: {contacts[name]}"
... 

@input_error
def show_all(contacts):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def good_bye():
    return "Good bye!"


def main():
    commands = {
        "hello": hello,
        "add": add_contact,
        "change": change_contact,
        "phone": phone,
        "show all": show_all,
        "good bye": good_bye,
        "close": good_bye,
        "exit": good_bye
    }

    contacts = {}

    while True:
        user_input = input("Enter a command: ").lower()

        if user_input in commands:
            if user_input == "good bye":
                print(commands[user_input]())
                break
            elif user_input == "show all":
                print(commands[user_input](contacts))
            else:
                command_result = commands[user_input](user_input, contacts)
                print(command_result)
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
