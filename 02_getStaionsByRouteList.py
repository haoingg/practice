import requests, xmltodict, json
key = 'kNSQvU5WeosgTXwCx1mTthdz93%2BlLXHKA7ZtzbuNArBuUVVP4akW5xsfp6R5JYuMH106DwcuJRTqXJHI4q%2BNjA%3D%3D'
busRouteId = 100100124 #x좌표, y좌표 구해지기 이전 임의 지정
url = 'http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?ServiceKey={}&busRouteId={}'.format(key, busRouteId)

content = requests.get(url).content
dict = xmltodict.parse(content)
staionId = json.dumps(dict['ServiceResult']['msgBody']['itemList'][0]['arsId'], ensure_ascii = False)
busRouteId = json.dumps(dict['ServiceResult']['msgBody']['itemList'][0]['busRouteId'], ensure_ascii = False)
seq = json.dumps(dict['ServiceResult']['msgBody']['itemList'][0]['seq'], ensure_ascii = False)

jsonstaionId = json.loads(staionId)
jsonsbusRouteId = json.loads(busRouteId)
jsonseq = json.loads(seq)

print(jsonstaionId)
print(jsonsbusRouteId)
print(jsonseq)

#print(len(jsonObj))