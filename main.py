# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from multi_protocol_clients import FtpClient


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    client = FtpClient(host='localhost', username='test', password='test')
    client.list_directories()
    client.get_file('TUSSPAT.pdf')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
