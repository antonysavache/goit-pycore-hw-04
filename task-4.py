from utils import parse_input, garbage_cleaner

contacts = {}

def add_contact(args):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args):
    name, phone = args
    contacts[name] = phone
    return "Contact changed."

def exit():
    print("Good bye!")

def hello():
    print('How can I help you?')

def all():
    if not len(contacts.keys()):
        print('No Names, no numbers')
    else:
        for name in contacts.keys():
            print(name + ':' + contacts[name])

def phone(args):
    if not len(contacts.keys()):
        print('No Names, no numbers')
    else:
        print(contacts[args[0]])

def edit(args):
    try:
        print(args)
        name, number = args
        number = garbage_cleaner(number)
        contacts[name] = number

    except Exception as e:
        print(e)

config = {
    'hello': lambda args: hello(),
    'all': lambda args: all(),
    'phone': lambda args: phone(args),
    'add': lambda args: edit(args),
    'change': lambda args: edit(args),
}

leave_commands = ['close', 'exit', 'vihod']

def main():
    data = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        try:
            command, *input_parametres = parse_input(user_input)

            for parameter in input_parametres:
                parameter = parameter.lower()

            if command in leave_commands:
                exit()
                break

            if command in config.keys():
                config[command](input_parametres)
            else:
                print("Invalid command.")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
