import requests
from pyfiglet import Figlet
import folium


def get_info_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        # print(response)
        
        data = {
            '[IP]': response.get('query'),
            '[통신사]': response.get('isp'),
            '[인터넷 서비스]': response.get('org'),
            '[국적]': response.get('country'),
            '[행정 구역]': response.get('regionName'),
            '[자치시]': response.get('city'),
            '[우편번호(외국기준)]': response.get('zip'),
            '[위도]': response.get('lat'),
            '[경도]': response.get('lon'),
        }
        
        for k, v in data.items():
            print(f'{k} : {v}')
        
        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')
        
    except requests.exceptions.ConnectionError:
        print('연결을 확인해주세요.')
        
        
def main():
    text = Figlet(font='slant')
    print(text.renderText('Find Ip Location'))
    ip = input('Ip주소입력: ')
    get_info_ip(ip=ip)
    
    
if __name__ == '__main__':
    main()