from textwrap import fill
from turtle import width
import requests
import folium
import tkinter as tk





y_frame=60


class MyGui:
    def __init__(self, app):
        self.app=app
        self.app.title('IP 위치 확인')
        self.app.geometry('500x600+100+100')
        self.label =tk.Label(self.app, text="IP주소입력:", font=("돋음", 10))
        self.label.place(x=78, y=y_frame)
        self.input_text = tk.Entry(self.app, width=30) 
        self.input_text.place(x=150, y=y_frame)
        self.button1=tk.Button(self.app, text='검색', command=self.get_info_by_ip)
        self.button1.place(x=370,y=y_frame-2)
        
        self.frame1=tk.Frame(self.app, relief="solid", bd=2, width=400,height=400,)
        self.frame1.pack(side="left", expand=True)
        

    def get_info_by_ip(self):
        try:
            response = requests.get(url=f'http://ip-api.com/json/{str(self.input_text.get())}').json()
            
        
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
        
        
            area = folium.Map(location=[response.get('lat'), response.get('lon')], zoom_start=15,)
            folium.Marker(location=[response.get('lat'), response.get('lon')],popup='추정위치',tooltip="추정위치", icon=folium.Icon(color='red',icon='star')).add_to(area)
            area.save(f'{response.get("query")}_{response.get("city")}.html')
            i=0
            for k, v in data.items():
                    
                    self.l1 = tk.Label(self.frame1,text=k, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                    self.l2 = tk.Label(self.frame1,text=v,  width=20, fg='blue', font=('Arial',10,'bold'))

                    self.l1.grid(row=i, column=0)
                    self.l2.grid(row=i, column=1)
                    i=i+1
            tk.messagebox.showinfo("저장완료","지도가 저장되었습니다.")
        
        except requests.exceptions.ConnectionError:
            print('연결을 확인해주세요.')

def main():
    app = tk.Tk()
    my_gui=MyGui(app)
    app.mainloop()
    
    
    
if __name__ == '__main__':
    main()