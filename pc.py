import requerts
url="https://baidu.com”
resp=requerts.get(url)
print(resp.text)
resp.close()
