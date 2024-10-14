import re
import mesop.labs as mel
from collections.abc import Generator


contacts: dict[str, str] = {}

def parse_input(user_input: str) -> tuple[str, list[str]]:
    cmd, *args = user_input.split()
    cmd: str = cmd.strip().lower()
    return cmd, args

def check_name_valid(name: str) -> bool:
    return re.fullmatch(pattern='[A-Za-z]{2,32}', string=name) is not None

def check_phone_valid(phone: str) -> bool:
    return re.fullmatch(pattern='[+0-9]{2,20}', string=phone) is not None

def show_hello() -> Generator[str]:
    yield 'Hi. How can i help you? \n\n Type "help" to get the list of available commands.'

def show_help() -> Generator[str]:
    yield 'Available commands: \n\n'
    yield 'add [name] [phone] \n\n'
    yield 'change [name] [new_phone] \n\n'
    yield 'phone [name] \n\n'
    yield 'all \n\n'
    yield 'help \n\n'
    
def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 2:
        return f'add: accepts 2 input arguments, but {len(args)} were provided.'
    
    name, phone = args

    if not check_name_valid(name=name):
        return 'Name can contain only letters A-Z, a-z'

    if not check_phone_valid(phone=phone):
        return 'Phone number can contain only characters: + 0-9'
    
    contacts[name] = phone

    return 'Contact added.'

def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 2:
        return f'change: accepts 2 input arguments, but {len(args)} were provided.'
    
    name, new_phone = args

    if name not in contacts.keys():
        return f'There is no contact with name {name}. Please, add this contact first.'
    
    contacts[name] = new_phone

    return 'Contact updated.'

def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 1:
        return f'phone: accepts 1 input argument, but {len(args)} were provided.'

    name: str = args[0]

    if name not in contacts.keys():
        return f'Contact with name {name} is absent.'
    
    return f'{name} : {contacts[name]}'

def show_all(args: list[str], contacts: dict[str, str]) -> Generator[str]:
    if len(args) != 0:
        yield f'show: accepts 0 input arguments, but {len(args)} were provided.'
    
    if len(contacts.items()) > 0:
        for name, phone in contacts.items():
            yield f'{name} : {phone} \n\n'
    else:
        yield 'There are no contacts in address book yet.'

def show_goodbye() -> str:
    return 'Good bye!'
    
def transform(input: str, history: list[mel.ChatMessage]) -> str | Generator[str]:
    try:
        cmd, args = parse_input(user_input=input)

        match cmd:
            case 'hello' | 'hi':
                return show_hello()
            case 'add':
                return add_contact(args=args, contacts=contacts)
            case 'change':
                return change_contact(args=args, contacts=contacts)
            case 'phone':
                return show_phone(args=args, contacts=contacts)
            case 'all':
                return show_all(args=args, contacts=contacts)
            case 'close' | 'exit':
                return show_goodbye()
            case 'help' | '"help"' | _:
                return show_help()

    except Exception as e:
        return show_help()