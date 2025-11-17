# Ubah Data Instagram

try:
    import uuid, pytz, hmac, hashlib, urllib, shutil, base64
    import os, re, sys, json, time, random, datetime, requests
    from rich.tree import Tree
    from rich import print as printz
    from rich.panel import Panel
    from rich.console import Console
    from rich.columns import Columns
    from Temporary.Secure import Require
    from Temporary.Terminalize.Styles import style_terminal
except(Exception, KeyboardInterrupt) as e:
    try:
        from urllib.parse import quote
        __import__('os').system(f'xdg-open https://wa.me/6283140199711?text=INSTAGRAM%20ERROR%20%3A%20{quote(str(e))}')
        exit()
    except(Exception, KeyboardInterrupt) as e:
        from urllib.parse import quote
        __import__('os').system(f'xdg-open https://wa.me/6283140199711?text=INSTAGRAM%20ERROR%20%3A%20{quote(str(e))}')
        exit()

class Requ:
    def __init__(self) -> None:
        self.proxies = []
        self.MID = {}
        pass      
        
    def SetMid(self):
        return '' if len(self.MID) == 0 else random.choice(self.MID)
        
    def UseNet(self):
        return('MOBILE.LTE','MOBILE(LTE)')
        
    def Android_ID(self, username, password):
        self.xyz = hashlib.md5()
        self.xyz.update(username.encode('utf-8') + password.encode('utf-8'))
        self.hex = self.xyz.hexdigest()
        self.xyz.update(self.hex.encode('utf-8') + '12345'.encode('utf-8'))
        return self.xyz
        
    def HeadersApiLogin(self):
        return {
           'host': 'b.i.instagram.com',
           'x-ig-app-locale': 'in_ID',
           'x-ig-device-locale': 'in_ID',
           'x-ig-mapped-locale': 'id_ID',
           'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-3',
           'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
           'x-ig-bandwidth-speed-kbps': '-1.000',
           'x-ig-bandwidth-totalbytes-b': '0',
           'x-ig-bandwidth-totaltime-ms': '0',
           'x-bloks-version-id': self.Blok_ID(),
           'x-ig-www-claim': '0',
           'x-bloks-is-prism-enabled': 'false',
           'x-bloks-is-layout-rtl': 'false',
           'x-ig-device-id': 'b7b95886-a663-41e4-8025-941a72c9ac4d',
           'x-ig-family-device-id': '2ce88cf6-20e8-4b2e-bb67-8d8ed5dda357',
           'x-ig-android-id': 'android-f4d8eb2bd1b86a47',
           'x-ig-timezone-offset': str(self.timezone_offset()),
           'x-fb-connection-type': self.UseNet()[0],
           'x-ig-connection-type': self.UseNet()[1],
           'x-ig-capabilities': '3brTv10=',
           'x-ig-app-id': '567067343352427',
           'priority': 'u=3',
           'user-agent': 'Instagram 309.1.0.41.113 Android (31/10; 360dpi; 1080x2326; Vivo; V2020CA; V1950A; qcom; id_ID; 541635863)',
           'accept-language': 'id-ID, en-US',
           'x-mid': str(self.SetMid()),
           'ig-intended-user-id': '0',
           'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'content-length': '2702',
           'x-fb-http-engine': 'Liger',
           'x-fb-client-ip': 'True',
           'x-fb-server-cluster': 'True'
       }
        
    def Convert_Name(self, xxx, cookie):
        with requests.Session() as r:
            try:
                response = r.get(f'https://www.instagram.com/{xxx}/', headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3"}, cookies={'cookie': cookie}).text
                if 'user_id' in str(response):
                    return(re.findall('"user_id":"(\d+)"', str(response))[0])
            except (Exception) as e: pass
            
    def Convert_Url(self, xxx, cookie):
        with requests.Session() as r:
            try:
                response = r.get(xxx, cookies={'cookie': cookie}).text
                if 'media_id' in str(response):
                    return(re.findall('{"media_id":"(.*?)"',str(response))[0])
            except (Exception) as e: exit(e)
            
    def Facebook_Acc(self, cookie):
        with requests.Session() as r:
            try:
                self.csrftoken = re.findall('csrftoken=(.*?);',str(cookie))
                self.headers = {"Host": "www.instagram.com","content-length": "0","x-requested-with": "XMLHttpRequest","x-csrftoken": "tJdFh5wJTuFDQZvpadl2kTm0LGRSkH8w" if len(self.csrftoken) == 0 else self.csrftoken[0],"x-ig-app-id": "936619743392459","x-instagram-ajax": "1011212827","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36","content-type": "application/x-www-form-urlencoded","accept": "*/*","x-asbd-id": "129477","cookie": cookie}
                response = r.post('https://www.instagram.com/api/v1/web/fxcal/ig_sso_users/', headers = self.headers).json()
                if 'fbAccount' in str(response):
                    self.nama = response['fbAccount']['display_name']
                    self.response2 = r.get('https://accountscenter.instagram.com/profiles/', cookies = {'cookie':cookie}).text
                    self.username = re.search('{"__typename":"XFBFXFBAccountInfo","id":"(.*?)"}', str(self.response2)).group(1)
                else:
                    self.nama = None
                    self.username = (None)
            except (Exception) as e:
                self.nama = 'Response Error'
                self.username = 'Response Error'
            return('%s|%s'%(self.username, self.nama))

    def Validasi_Username(self, username):
       with requests.Session() as r:
           try:
               response = r.get("https://i.instagram.com/api/v1/users/web_profile_info/?username={}".format(username), headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3"}).json()
               return (
                   response["data"]["user"]["full_name"], 
                   response["data"]["user"]["edge_followed_by"]["count"], 
                   response["data"]["user"]["edge_follow"]["count"], 
                   response["data"]["user"]["edge_owner_to_timeline_media"]["count"],
                   response["data"]["user"]["biography"],
                   response["data"]["user"]["is_private"],
                   response["data"]["user"]["is_verified"],
                   response["data"]["user"]["profile_pic_url"],
                   response["data"]["user"]["profile_pic_url_hd"],response["data"]["user"]["profile_pic_url_hd"]
               )
           except (Exception) as e: return(None,None,None,None,None,None,None,None,None,None)
           
    def DeviceId(self):
        return 'android-%s'%(self.uuid_(True)[:16])

    def uuid_(self, abcd=None, zd=None):
        if zd is not None:
           m = hashlib.md5()
           m.update(zd.encode('utf-8'))
           i = uuid.UUID(m.hexdigest())
        else:
           i = uuid.uuid4()
           if abcd: return str(i.hex)
        return str(i)

    def adid(self, username):
        sha2 = hashlib.sha256()
        sha2.update(username.encode('utf-8'))
        abcd = sha2.hexdigest()
        return self.uuid_(False, abcd)

    def guid(self):
        return self.uuid_(False)

    def poid(self):
        return self.uuid_(False, self.guid())
        
    def Blok_ID(self):
        self.v23 = 'edf962326770574232e3938baf0c2faebdbb23703933345b000509f560bd9965'
        self.v39 = 'c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49'
        self.v09 = '9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a'
        return(random.choice([self.v09,self.v39,self.v23]))
       
    def timezone_offset(self):
        self.tim = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
        self.ofs = self.tim.utcoffset().total_seconds()/60/60
        return self.ofs    

class SecureIG:
    def __init__(self) -> None:
        self.ok = 'Secure-Ok.txt'
        self.cp = 'Secure-Cp.txt'
        self.fa = 'Secure-2f.txt'
        pass
        
    def Secure_Akun_Instagram(self):
        try:
            Console(width = 65, style = f"{style_terminal}").print(Panel("[grey50]Silakan Masukan [green]Username [grey50]And[bold green] Password[grey50], Gunakan Pemisah [red]<=>[grey50] Untuk Username Dengan Password, Pastikan Akun Tidak [yellow]Chekpoint[grey50] Dan Terpasang [red]A2F", title = f"[white]• [green]Username And Password [white]•", subtitle = "╭─────", subtitle_align = "left"))
            querty = Console().input("[grey50]   ╰─> ")
            if len(querty) >0:
                try:
                    self.username = querty.split('<=>')[0]
                    self.password = querty.split('<=>')[1]
                    self.Username_And_Password(self.username, self.password)
                    Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Secure Akun Instagram, Selamat Menikmati Dan Semoga Beruntung", title = f"[bold white]• [green]Selesai [white]•"))
                    exit()
                except (Exception) as e:
                    Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                    exit()   
            else:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Opss, Anda Tidak Memasukan Apapun, Harap Masukan '[green]Username And Password[grey50]'", title = f"[white]• [red]Error Not Found [white]•"))
                exit()          
        except (KeyboardInterrupt, Exception) as e:
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
            exit()       
            
    def Username_And_Password(self, username, password):
        byps = requests.Session()
        try:
            ua_generate = ('Instagram 63.0.0.17.94 Android (31/10; 360dpi; 1080x2326; Vivo; V2020CA; V1950A; qcom; id_ID; 253447817)')
            byps.headers.update({**Requ().HeadersApiLogin(),
                'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0',
                'x-pigeon-rawclienttime': '{:.3f}'.format(time.time()),
                'x-ig-bandwidth-speed-kbps': '{}'.format(random.randint(100,999)),
                'x-ig-bandwidth-totalbytes-b': str(random.randint(2000,5000)),
                'x-ig-bandwidth-totaltime-ms': str(random.randint(500,4000)),
                'x-ig-device-id': str(uuid.uuid4()),
                'x-ig-android-id': 'android-%s'%(Requ().Android_ID(self.username,self.password).hexdigest()[:16]),
                'x-ig-timezone-offset': str(Requ().timezone_offset()),
                'x-ig-app-id': '567067343352427',
                'user-agent': ua_generate
            })
            payload = ('params={"client_input_params":{"device_id":"'+byps.headers['x-ig-android-id']+'","login_attempt_count":1,"secure_family_device_id":"","machine_id":"'+str(byps.headers['x-mid'])+'","accounts_list":[],"auth_secure_device_id":"","has_whatsapp_installed":0,"password":"#PWD_INSTAGRAM:0:'+str(int(time.time()))+':'+self.password+'","sso_token_map_json_string":"","family_device_id":"'+str(uuid.uuid4())+'","fb_ig_device_id":[],"device_emails":[],"try_num":1,"lois_settings":{"lois_token":"","lara_override":""},"event_flow":"login_manual","event_step":"home_page","headers_infra_flow_id":"","openid_tokens":{},"client_known_key_hash":"","contact_point":"'+self.username+'","encrypted_msisdn":""},"server_params":{"should_trigger_override_login_2fa_action":0,"is_from_logged_out":0,"username_text_input_id":"18g3p8:57","layered_homepage_experiment_group":null,"should_trigger_override_login_success_action":0,"device_id":null,"login_credential_type":"none","server_login_source":"login","waterfall_id":"'+str(uuid.uuid4())+'","login_source":"Login","INTERNAL__latency_qpl_instance_id":7465439600681,"reg_flow_source":"login_home_native_integration_point","is_caa_perf_enabled":1,"is_platform_login":0,"credential_type":"password","caller":"gslr","INTERNAL__latency_qpl_marker_id":36707139,"family_device_id":null,"offline_experiment_group":null,"INTERNAL_INFRA_THEME":"harm_f","password_text_input_id":"18g3p8:58","is_from_logged_in_switcher":0,"ar_event_source":"login_home_page"}}&bk_client_context={"bloks_version":"9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a","styles_id":"instagram"}&bloks_versioning_id=9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a')
            response = byps.post('https://b.i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data = payload, allow_redirects = True).text
            if 'logged_in_user' in response.replace('\\',''):
                try:
                    ig_set_autorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response.replace('\\', ''))).group(1)
                    decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(ig_set_autorization.split('Bearer IGT:2:')[1]))
                    cookie = (';'.join(['%s=%s'%(name, value) for name, value in decode_ig_set_authorization.items()]))
                except (Exception) as e: cookie = ('cookie tidak di temukan')
                try: fullname, follower, followed, feedpost, biography, is_private, is_verified, profile_pic_url, profile_pic_url_hd, bussiness = Requ().Validasi_Username(username)
                except (UnboundLocalError) as e: pass
                try:
                    num = Require().DeltPhone(cookie)
                    statp, pone = num['Dihapus'], num['Number']
                    deleted = f'{pone} berhasil di hapus' if statp is True else f'{pone} gagal di hapus '
                    two = Require().Aktifkan2F(cookie)
                    kode, key, statf = two['kode-pemulihan'], two['SecretKey'], two['success-a2f']
                    stat2fa = 'A2F berhasil di aktifkan' if statf is not False else 'A2F gagal di aktifkan'
                    Temp = Require().AddMail(cookie)
                    email, state, inbx = Temp['email'], Temp['di-konfirmasi'], Temp['Url']
                    statd = 'berhasil di konfirmasi' if state is True else 'gagal di konfirmasi'
                    tree = Tree('\r                                             ')
                    tree = tree.add('╭ [italic green]Response Success')
                    tree.add(f'[italic grey50]Username : [green]{username}')
                    tree.add(f'[italic grey50]Fullname : [green]{fullname}')
                    tree.add(f'[italic grey50]Password : [green]{password}')
                    tree.add(f'[italic grey50]Profiles : [green]{follower}[grey50]/[green]{followed}[grey50]/[green]{feedpost}')
                    truu= tree.add('[italic green]Response 2FA')
                    truu.add(f'[italic grey50]Response : [green]{email} {statd}')
                    truu.add(f'[italic grey50]Response : [green]{inbx}')
                    truu.add(f'[italic grey50]Response : [green]{deleted}')
                    truu.add(f'[italic grey50]Response : [green]{stat2fa}')
                    truu.add(f'[italic grey50]Response : [green]{key}')
                    truu.add(f'[italic grey50]Response : [green]{kode}')
                    trua = tree.add('[italic green]Response Cookie')
                    trua.add(f'[italic grey50]Cookie : [green]{cookie}')
                    trua.add(f'[italic grey50]Bearer : [green]{ig_set_autorization}')
                    tree.add(f'[italic grey50]Useragent : [green]{byps.headers["user-agent"]}')
                    printz(tree)
                    save = f'{fullname}|{username}|{password}|{follower}|{followed}|{feedpost}|{stat2fa}|{key}|{kode}|{deleted}|{email} {statd}|{inbx}|{cookie}\n'
                except Exception as e:
                    print(e)
                    tree = Tree('\r                                             ')
                    tree = tree.add('╭ [italic green]Response Success')
                    tree.add(f'[italic grey50]Username : [green]{username}')
                    tree.add(f'[italic grey50]Fullname : [green]{fullname}')
                    tree.add(f'[italic grey50]Password : [green]{password}')
                    tree.add(f'[italic grey50]Profiles : [green]{follower}[grey50]/[green]{followed}[grey50]/[green]{feedpost}')
                    trua = tree.add('[italic green]Response Cookie')
                    trua.add(f'[italic grey50]Cookie : [green]{cookie}')
                    trua.add(f'[italic grey50]Bearer : [green]{ig_set_autorization}')
                    tree.add(f'[italic grey50]Useragent : [green]{byps.headers["user-agent"]}')
                    printz(tree)
                    save = f'{fullname}|{username}|{password}|{follower}|{followed}|{feedpost}|{cookie}\n'    
                with open('/sdcard/OK/'+self.ok,'a') as wr:
                    wr.write(save)
                    wr.close()  
            elif 'two_factor_required' in response.replace('\\',''):
                try: fullname, follower, followed, feedpost, biography, is_private, is_verified, profile_pic_url, profile_pic_url_hd, bussiness = Requ().Validasi_Username(username)
                except (UnboundLocalError) as e: pass
                tree = Tree('\r                                             ')
                tree = tree.add('╭ [italic red]Response A2F')
                tree.add(f'[italic grey50]Username : [red]{username}')
                tree.add(f'[italic grey50]Fullname : [red]{fullname}')
                tree.add(f'[italic grey50]Password : [red]{password}')
                tree.add(f'[italic grey50]Profiles : [red]{follower}[grey50]/[red]{followed}[grey50]/[red]{feedpost}')
                tree.add(f'[italic grey50]Useragent : [red]{byps.headers["user-agent"]}')
                printz(tree)
                save = f'{fullname}|{username}|{password}|{follower}|{followed}|{feedpost}\n'
                with open('/sdcard/2F/'+self.fa,'a') as wr:
                    wr.write(save)
                    wr.close() 
            elif 'challenge_required' in response.replace('\\',''):
                try: fullname, follower, followed, feedpost, biography, is_private, is_verified, profile_pic_url, profile_pic_url_hd, bussiness = Requ().Validasi_Username(username)
                except (UnboundLocalError) as e: pass
                tree = Tree('\r                                             ')
                tree = tree.add('╭ [italic yellow]Response Checkpoint')
                tree.add(f'[italic grey50]Username : [yellow]{username}')
                tree.add(f'[italic grey50]Fullname : [yellow]{fullname}')
                tree.add(f'[italic grey50]Password : [yellow]{password}')
                tree.add(f'[italic grey50]Profiles : [yellow]{follower}[grey50]/[yellow]{followed}[grey50]/[yellow]{feedpost}')
                tree.add(f'[italic grey50]Useragent : [yellow]{byps.headers["user-agent"]}')
                printz(tree)
                save = f'{fullname}|{username}|{password}|{follower}|{followed}|{feedpost}\n'
                with open('/sdcard/CP/'+self.cp,'a') as wr:
                    wr.write(save)
                    wr.close()
            elif 'ip_block' in response.replace('\\',''):
                Console().print(f"[grey50]   ──>[red] HIDUPKAN MODE PESAWAT 5 DETIK!", end='\r')
                time.sleep(3.5)  
            elif 'Harap tunggu beberapa menit sebelum mencoba lagi.' in str(response):   
                Console().print(f"[grey50]   ──>[red] HIDUPKAN MODE PESAWAT 5 DETIK!", end='\r')
                time.sleep(3.5)  
            elif 'Kesalahan' in response.replace('\\',''):
                Console().print(f"[grey50]   ──>[red] HIDUPKAN MODE PESAWAT 5 DETIK!", end='\r')
                time.sleep(3.5)  
            elif 'Maaf, terdapat masalah pada permintaan Anda.' in response.replace('\\',''):
                Console().print(f"[grey50]   ──>[red] HIDUPKAN MODE PESAWAT 5 DETIK!", end='\r')
                time.sleep(3.5)
            else:
                Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Opss, Terjadi Kesalahan [green]Username[grey50] Atau [green]Password[grey50] Yang Anda Masukan Salah, Silakan Cek [green]Username[grey50] Dan [green]Password[grey50] Anda Pastikan Benar", title = f"[white]• [red]Logged Error [white]•"))
        except (KeyboardInterrupt, requests.exceptions.ConnectionError, requests.exceptions.TooManyRedirects): Console().print(f"[bold grey50]   ──>[bold red] KONEKSI ERROR!", end='\r'); time.sleep(31); exit()