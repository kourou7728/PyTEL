from urllib import request

url = 'http://httpbin.org/get'

res =  request.urlopen(url=url)

print(res)
print(type(res.read().decode('utf-8')))
