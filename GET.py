import requerts
query=input("请输入关键词")
url=f"https://www.sogo.com/web?query={query}”
resp=requerts.get(url)
print(resp.text)
resp.close()
