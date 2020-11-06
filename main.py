# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from multi_protocol_clients import FtpClient
from getpass import getpass


def read_input_action():
    value = input('>> ')
    return value


def print_help():
    return 'Help here!'


def validate_and_execute_action(action, instanced_client):
    switcher = {
        'help': print_help,
        'connect': instanced_client.connect,
        'dir': instanced_client.list_dir,
        'disconnect': instanced_client.disconnect
    }
    func = switcher.get(action, lambda: 'Invalid action')
    func()


class Client:

    def __init__(self):
        self.client = None

    def connect(self):
        if self.client is not None:
            print('Already connected, please disconnect first')
            return
        hostname = input('hostname: ')
        username = input('username: ')
        password = input('password: ')
        self.client = FtpClient(host=hostname, username=username, password=password)

    def list_dir(self):
        if self.client is not None:
            self.client.list_directories()
        else:
            print('Not connected')

    def disconnect(self):
        if self.client is not None:
            self.client.quit()
            self.client = None
            print('Successfully disconnected')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    client = Client()
    while True:
        value = read_input_action()
        validate_and_execute_action(value, instanced_client=client)
    # client = FtpClient(host='localhost', username='test', password='test')
    # client.list_directories()
    # client.get_file('TUSSPAT.pdf')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
