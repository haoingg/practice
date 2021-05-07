from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus

url = 'http://ws.bus.go.kr/api/rest/stationinfo/getStationByName'
queryParams = '?' + urlencode({quote_plus('ServiceKey') : 'kNSQvU5WeosgTXwCx1mTthdz93%2BlLXHKA7ZtzbuNArBuUVVP4akW5xsfp6R5JYuMH106DwcuJRTqXJHI4q%2BNjA%3D%3D', quote_plus('stSrch') : '당산역' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)

# getArrInfoByRouteList (Python 샘플 코드)

from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus

url = 'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '서비스키', quote_plus('stId') : '', quote_plus('busRouteId') : '', quote_plus('ord') : '' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)

# 하영 practice
# 일반 인증키
# kNSQvU5WeosgTXwCx1mTthdz93%2BlLXHKA7ZtzbuNArBuUVVP4akW5xsfp6R5JYuMH106DwcuJRTqXJHI4q%2BNjA%3D%3D