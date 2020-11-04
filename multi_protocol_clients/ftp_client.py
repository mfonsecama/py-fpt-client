from ftplib import FTP


class FtpClient:

    def __init__(self, host='', username='', password='', https=False):

        self.ftp = None
        self.host = host
        self.username = username
        self.password = password
        self.https = https
        self.init_client()

    def init_client(self):
        if self.https is True:
            print('TODO: Implement https')
        else:
            self.ftp = FTP(self.host)
            self.ftp.login(user=self.username, passwd=self.password)
            print(self.ftp.getwelcome())

    def list_directories(self):
        self.ftp.dir()

    def change_working_directory(self, directory):
        self.ftp.cwd(dirname=directory)

    def get_file(self, name, to_path=''):
        dest = to_path + '/' + name if to_path != '' and to_path.endswith('/') is False else to_path + name
        with open(dest, 'wb') as fp:
            self.ftp.retrbinary('RETR ' + name, fp.write)


