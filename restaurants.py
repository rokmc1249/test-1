import requests

url = 'http://openapi.seoul.go.kr:8088/745369696e77776a333761794d6879/json/SearchPublicToiletPOIService/1/100/'

response = requests.get(url)
print(response.content)