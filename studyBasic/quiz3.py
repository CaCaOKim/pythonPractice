#url = "http://naver.com"   #target: nav51!
url = "http://developer.co.kr"   #target: dev93!
urlch = url.replace("http://", "")
urlch = urlch[:urlch.index(".")]
password = urlch[:3]+str(len(urlch))+str(url.count("e"))+"!"
print(password)