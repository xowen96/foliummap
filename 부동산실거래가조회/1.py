from re import M
import numpy as np
import pandas as pd
import folium
import warnings
warnings.filterwarnings(action='ignore')


m = folium.Map(
  location=[37.5215695,126.9243115],#여의도역
  tiles='Stamen Terrain',
  zoom_start=15
)

tooltip = 'Click!'

folium.Marker(
  [37.5215695,126.9243115],#여의도역
  popup='<strong> 현재위치 </strong>',
  tooltip = tooltip,
  icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)

folium.Marker(
  [37.522053,126.922277],#본사
  popup='<strong> 한국투자증권 </strong>',
  tooltip = tooltip,
    icon=folium.Icon(color='blue', icon='bookmark')
).add_to(m)

folium.Marker(
  [37.5284304,126.9330781],#한강공원
  popup='<strong> 여의도 한강공원 </strong>',
  tooltip = tooltip,
   icon=folium.Icon(color='green', icon='bookmark')
).add_to(m)

eunpyung = pd.read_csv('/Users/owenkim/Desktop/부동산실거래가조회/locations/eunpyung.csv',encoding='cp949')
gangseo = pd.read_csv('/Users/owenkim/Desktop/부동산실거래가조회/locations/gangseo.csv',encoding='cp949')
gwanak = pd.read_csv('/Users/owenkim/Desktop/부동산실거래가조회/locations/gwanak.csv',encoding='cp949')
seocho = pd.read_csv('/Users/owenkim/Desktop/부동산실거래가조회/locations/seocho.csv',encoding='cp949')
sungbook = pd.read_csv('/Users/owenkim/Desktop/부동산실거래가조회/locations/sungbook.csv', encoding='cp949')
yongsan = pd.read_csv('/Users/owenkim/Desktop/부동산실거래가조회/locations/yongsan.csv',encoding='cp949')

eunpyung.shape
eunpyung['이미지'] = eunpyung['관광지명'] + '.jpg'
for i in range(eunpyung.shape[0]): #반복문을 통해 각 관광지 데이터를 불러와 지도에 표시함 
    folium.Marker(
      [eunpyung.iloc[i]['위도'],eunpyung.iloc[i]['경도']],#은평
      popup = f'<div style="width:100px"><strong>{eunpyung.iloc[i]["관광지명"]}</strong><br>\
      공공편익시설 : {eunpyung.iloc[i]["공공편익시설정보"]}<br>\
      주차가능수 : {eunpyung.iloc[i]["주차가능수"]}<br>\
      <img width= "80px", src = /Users/owenkim/Desktop/부동산실거래가조회/img/a.jpg><br>\
      </div>',
      tooltip = tooltip,
  ).add_to(m)

    
gangseo.shape
gangseo['이미지'] = gangseo['관광지명'] + '.jpg'
for i in range(gangseo.shape[0]):
   folium.Marker(
     [gangseo.iloc[i]['위도'],gangseo.iloc[i]['경도']],#강서
      popup = f'<div style="width:100px"><strong>{gangseo.iloc[i]["관광지명"]}</strong><br>\
      공공편익시설 : {gangseo.iloc[i]["공공편익시설정보"]}<br>\
      주차가능수 : {gangseo.iloc[i]["주차가능수"]}<br>\
      <img width= "80px", src = /Users/owenkim/Desktop/부동산실거래가조회/img/b.jpg><br>\
      </div>',
      tooltip = tooltip,
  ).add_to(m)
  
gwanak.shape
gwanak['이미지'] = gwanak['관광지명'] + '.jpg'
for i in range(gwanak.shape[0]):
   folium.Marker(
     [gwanak.iloc[i]['위도'],gwanak.iloc[i]['경도']],#관악
      popup = f'<div style="width:100px"><strong>{gwanak.iloc[i]["관광지명"]}</strong><br>\
      공공편익시설 : {gwanak.iloc[i]["공공편익시설정보"]}<br>\
      주차가능수 : {gwanak.iloc[i]["주차가능수"]}<br>\
      <img width= "80px", src = /Users/owenkim/Desktop/부동산실거래가조회/img/c.jpg><br>\
      </div>',
      tooltip = tooltip,
  ).add_to(m)
  
seocho.shape
seocho['이미지'] = seocho['관광지명'] + '.jpg'
for i in range(seocho.shape[0]):
     folium.Marker(
     [seocho.iloc[i]['위도'],seocho.iloc[i]['경도']],#서초
      popup = f'<div style="width:100px"><strong>{seocho.iloc[i]["관광지명"]}</strong><br>\
      공공편익시설 : {seocho.iloc[i]["공공편익시설정보"]}<br>\
      주차가능수 : {seocho.iloc[i]["주차가능수"]}<br>\
      <img width= "80px", src = /Users/owenkim/Desktop/부동산실거래가조회/img/d.jpg><br>\
      </div>',
      tooltip = tooltip,
  ).add_to(m)
     
sungbook.shape
sungbook['이미지'] = sungbook['관광지명'] + '.jpg'
for i in range(sungbook.shape[0]):
       folium.Marker(
     [sungbook.iloc[i]['위도'],sungbook.iloc[i]['경도']],#성북
      popup = f'<div style="width:100px"><strong>{sungbook.iloc[i]["관광지명"]}</strong><br>\
      공공편익시설 : {sungbook.iloc[i]["공공편익시설정보"]}<br>\
      주차가능수 : {sungbook.iloc[i]["주차가능수"]}<br>\
      <img width= "80px", src = /Users/owenkim/Desktop/부동산실거래가조회/img/e.jpg><br>\
      </div>',
      tooltip = tooltip,
  ).add_to(m)
     
yongsan.shape
yongsan['이미지'] = yongsan['관광지명'] + '.jpg'
for i in range(yongsan.shape[0]):
       folium.Marker(
     [yongsan.iloc[i]['위도'],yongsan.iloc[i]['경도']],#용산
      popup = f'<div style="width:100px"><strong>{yongsan.iloc[i]["관광지명"]}</strong><br>\
      공공편익시설 : {yongsan.iloc[i]["공공편익시설정보"]}<br>\
      주차가능수 : {yongsan.iloc[i]["주차가능수"]}<br>\
      <img width= "80px", src = /Users/owenkim/Desktop/부동산실거래가조회/img/f.jpg><br>\
      </div>',
      tooltip = tooltip,
  ).add_to(m)
       
       
m.save('map.html')