import requerts
s=input(请输入要翻译的单词")
dat={"kw": s}
url="https://fanyi.baidu.com/sug"
resp=requests.post(url,data=dat)
print(resp.json())
resp.close()
