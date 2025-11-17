import os, sys, requests
from rich.console import Console
from bs4 import BeautifulSoup as bs
from Temporary.CreateACC.payloadsFB import Main

class Requdable:
    def __init__(self) -> None:
        pass
        
    def clear_terminalize(self):
        os.system('clear' if 'linux' in sys.platform.lower() else 'cls')
        
    def Banner(self):
        self.clear_terminalize()
        Console().print('''[b white]\r
  _____             __      _______ 
 / ___/______ ___ _/ /____ / __/ _ ) [b white]Author: [b green]Zoraa Dev[b white]
/ /__/ __/ -_) _ `/ __/ -_) _// _  | [b white]Status: [b green]Premiun[b green]
\___/_/  \__/\_,_/\__/\__/_/ /____/ [b white]Version: [b green]2.0                                                            
''')
        return (True)
        
    def Running(self):
        self.Banner()
        Console().print(' [b green]01[b white]) pembuatan Fb type otomatis\n [b green]02[b white]) tambahkan informasi profile\n [b green]03[b white]) chek akun aktif\n [b green]04[b white]) lihat hasil\n [b red]00[b white]) exit')
        query = Console().input('\n [b green]# [b white]Masukan pilihan: ')
        if query =='1' or query =='01':
            Console().print('\n [b green]#[b white]) save As result OK: sdcard/OK/createFB_success.txt\n [b green]#[b white]) save As result CP: sdcard/CP/createFB_invalid.txt\n\n [b green]![b white]) gunakan Control dan Z (Ctrl + Z) untuk berhenti create FB')
            while True:
                try: self.LoopingCreate()
                except (KeyboardInterrupt) as e: break
                
        elif query =='3' or query =='03':
            try:
                Console().print('\n [b green]![b white]) pengecekan akun FB active\n')
                self.GetInfoProfile()
                exit()
            except (Exception) as e: sys.exit(e) 
                
        elif query =='4' or query =='04':
            try:
                Console().print('\n [b green]01[b white]) result FB success\n [b green]02[b white]) result FB checkpoint')
                choose = Console().input('\n [b green]# [b white]Masukan pilihan: ')
                self.Result(choose)
                exit()
            except (Exception) as e: sys.exit(e)    
            
        else: exit()
        
    def Result(self, choose):
        if choose in ('1','01'):
            for buka in open('/sdcard/OK/createFB_success.txt').readlines():
                try:
                    Console().print(f"\n[b green]•[white] userID : [green]{buka.split('|')[0]}\n[b green]•[white] username : [b green]{buka.split('|')[1]}\n[b green]•[white] password : [b green]{buka.split('|')[2]}\n[b green]•[white] ultah : [b green]{buka.split('|')[3]}\n[b green]•[white] email : [b green]{buka.split('|')[4]}\n[b green]•[white] cookies : [b green]{buka.split('|')[5]}")
                except Exception as e:
                    Console().print(f"\n[b green]•[white] userID : [b green]{buka.split('|')[0]}\n[b green]•[white] username : [b green]{buka.split('|')[1]}\n[b green]•[white] password : [b green]{buka.split('|')[2]}")
                    
        elif choose in ('2','02'):
            for buka in open('/sdcard/CP/createFB_invalid.txt').readlines():
                try:
                    Console().print(f"\n[b red]•[white] userID : [b red]{buka.split('|')[0]}\n[b red]•[white] username : [b red]{buka.split('|')[1]}\n[b red]•[white] password : [b red]{buka.split('|')[2]}\n[b red]•[white] ultah : [b red]{buka.split('|')[3]}\n[b red]•[white] email : [b red]{buka.split('|')[4]}\n[b red]•[white] cookies : [b red]{buka.split('|')[5]}")
                except Exception as e:
                    Console().print(f"\n[b red]•[white] userID : [b red]{buka.split('|')[0]}\n[b red]•[white] username : [b red]{buka.split('|')[1]}\n[b red]•[white] password : [b red]{buka.split('|')[2]}")
                    
    def get_facebook_profile_info(self, username):
        response = requests.get(f'https://www.facebook.com/{username}')
        if response.status_code == 200:
            soup = bs(response.text, 'html.parser')
            profile_name = soup.find('title').text
            if profile_name:
                return profile_name
            else:
                return "Nama tidak ditemukan"
        else:
            return "Profil tidak dapat diakses"
                    
    def GetInfoProfile(self):
        with open('/sdcard/OK/createFB_success.txt', 'r') as file:
            usernames = file.readlines()
        for username in usernames:
            username = username.strip()
            if username:
                name = self.get_facebook_profile_info(username.split('|')[0])
                Console().print(f' [b green]#[white] Username: [green]{username.split('|')[0]} [white]> Nama: [green]{name}')
        
    def LoopingCreate(self):
        try:
            main = Main()
            main.Create_Nama()
            main.Response_Nama()
            main.Create_Birthday()
            main.Response_Birthday()
            main.Create_Gender()
            main.Response_Gender()
            main.Create_Email()
            main.Response_Email()
            main.Create_Password()
            main.Response_Password()
            main.Next_Response()
            main.Next_Konfirmasi()
        except (Exception, ConnectionError) as e: self.LoopingCreate()
