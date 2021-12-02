#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#91porn无限制观看脚本


import socks
import socket
import requests
import pyperclip
import os
import win32clipboard as wc
import time
import random
import string
import urllib.parse
import webbrowser

ip = ""
port = ""
pl = []
pd = 0
proxy_mode = 0

cookie = "CLIPSHARE=rndn25n1q0osvkvli65vdvcfgf; language=cn_CN"

hdr2 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0 Waterfox/78.13.0",
    "Cookie": cookie           
}



def get_rdn_cookies():
    global cookie
    clip = ''.join(random.sample(string.ascii_lowercase + string.digits,26))
    cookie = "CLIPSHARE="+str(clip)+"; language=cn_CN"


def modify_hosts():
    try:
        fp=open("C:\\windows\\system32\\drivers\\etc\\hosts","r",encoding="utf-8")
        line = fp.read()
        if "www.91porn.com" in str(line):
            fp.close()
            return
        else:
            fp.close()
            fp=open("C:\\windows\\system32\\drivers\\etc\\hosts","a+",encoding="utf-8")
            fp.writelines("\n104.26.2.41 www.91porn.com\n")
            fp.writelines("172.67.70.4 www.91porn.com\n")
            fp.writelines("104.26.3.41 www.91porn.com\n")
            fp.close()
            os.system("ipconfig /flushdns")
        return
    except:
        print("请右键管理员权限运行!")
        os.system("pause")
        sys.exit()

def auto_switch_proxy():
    global proxies,pd,ip,port,proxy_mode
    if pd < len(pl):
        line = pl[pd]
        if str(line).startswith("socks4"):
            proxy_mode = 1
        elif str(line).startswith("socks5"):
            proxy_mode = 2
        else:
            proxy_mode = 0
        ip = line.split("/")[-1].split(":")[0]
        port = line.split(":")[-1]
        py = line
        pd += 1
        return
    else:
        pd = 0
        proxies = {}
        return

def check():
    global proxies,pl,ip,port,proxy_mode
    if os.path.exists("proxy.txt"):
        f = open("proxy.txt","r",encoding="utf-8")
        line = f.readline().strip('\n')
        if str(line).startswith("socks4"):
            proxy_mode = 1
        elif str(line).startswith("socks5"):
            proxy_mode = 2
        else:
            proxy_mode = 0        
        ip = line.split("/")[-1].split(":")[0]
        port = line.split(":")[-1]       
        while line:
            pl.append(line.strip('\n'))
            line = f.readline()
        f.close()
        return

    
def automode():
    while True:   
        os.system('cls')
        print("复制感兴趣的91porn视频链接后等待3秒")
        print("使用ublock屏蔽网页脚本后体验更佳")
        try:
            try:
                url = pyperclip.paste()
            except:
                time.sleep(1)
                continue
            if str(url).startswith("https://www.91porn.com") or str(url).startswith("https://91porn.com"):
                os.system('cls')
                try:
                    r = requests.get(url,headers=hdr2,timeout=2)
                    url2 = (r.text.split("document.write(strencode2(\"")[1].split("\"")[0])
                    url3 = urllib.parse.unquote(url2)
                    data = (url3.split("src=\'")[1].split("\'")[0])
                    if data:
                        if "//dl//" in str(data):
                            get_rdn_cookies()
                            auto_switch_proxy()
                            continue
                        else:                                    
                            webbrowser.open(data)
                            wc.OpenClipboard()
                            wc.EmptyClipboard()
                            wc.CloseClipboard()
                except:
                    try:
                        if os.path.exists("proxy.txt"):
                            if proxy_mode == 2:
                                socks.set_default_proxy(socks.SOCKS5,ip,int(port))
                                socket.socket = socks.socksocket
                            elif proxy_mode == 1:
                                socks.set_default_proxy(socks.SOCKS4,ip,int(port))
                                socket.socket = socks.socksocket
                            elif proxy_mode == 0:
                                socks.set_default_proxy(socks.HTTP,ip,int(port))
                                socket.socket = socks.socksocket
                            r = requests.get(url,headers=hdr2,timeout=2)
                            url2 = (r.text.split("document.write(strencode2(\"")[1].split("\"")[0])
                            url3 = urllib.parse.unquote(url2)
                            data = (url3.split("src=\'")[1].split("\'")[0])
                            if data:
                                if "//dl//" in str(data):
                                    get_rdn_cookies()
                                    auto_switch_proxy()
                                    continue
                                else:                                    
                                    webbrowser.open(data)
                                    wc.OpenClipboard()
                                    wc.EmptyClipboard()
                                    wc.CloseClipboard()
                            else:
                                pass
                    except:
                        get_rdn_cookies()
                        auto_switch_proxy()
                        pass
                        

                continue
            else:
                time.sleep(1)
                continue
        
        except:
            time.sleep(2)
            continue        


if __name__ == '__main__':
    os.system("cls")
    os.system("mode con cols=35 lines=3")
    check()
    auto_switch_proxy()
    automode()
