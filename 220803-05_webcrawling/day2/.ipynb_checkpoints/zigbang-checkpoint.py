# %%writefile (파일이름) -- 파일로 만들어줌.(쥬피터) 단, 주석 포함하여 맨 윗줄에서 실행하여야 한다.
# colab 에서도 사용 가능.
# 함수 만들기
import requests
import pandas as pd
import geohash2

def oneroom(addr):
    url = f'https://apis.zigbang.com/v2/search?leaseYn=N&q={addr}&serviceType=원룸'
    response = requests.get(url)
    data = response.json()["items"][0]
    lat, lng = data["lat"], data["lng"]
    
    geohash = geohash2.encode(lat, lng, precision=5)
    
    url = f'https://apis.zigbang.com/v2/items?deposit_gteq=0&domain=zigbang\
&geohash={geohash}&needHasNoFiltered=true&rent_gteq=0&sales_type_in=전세|월세&service_type_eq=원룸'
    # 참고: 문자열 길이가 너무 길어 '\'를 사용한다면
    # 함수 안에서 사용한다고 해도 들여쓰기는 하면 안된다. 들여쓰기(tab) 또한 문자로 확인하기 때문.
    response = requests.get(url)
    items = response.json()["items"]
    ids = [item["item_id"] for item in items]
    
    url = 'https://apis.zigbang.com/v2/items/list'
    params = { 
        "domain" : "zigbang",
        "withCoalition" : "true",
        "item_ids" : ids[:900]
    }
    response = requests.post(url, params)

    items = response.json()["items"]
    columns = ["item_id", "sales_type", "deposit", "rent", "size_m2", "address1", "manage_cost"]
    return pd.DataFrame(items)[columns]
