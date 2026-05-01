import urllib.request  # 웹(API) 요청을 보내기 위한 라이브러리
import json            # JSON 데이터 처리를 위한 라이브러리
import tkinter         # GUI 창 생성을 위한 라이브러리
import tkinter.font    # GUI 폰트 설정을 위한 라이브러리

API_KEY = "Enter your API key here"  # OpenWeatherMap에서 발급받은 API 키 입력

def tick1Min():
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid={API_KEY}&units=metric" # 서울 날씨 정보를 요청하는 API URL 
    
    with urllib.request.urlopen(url) as r:  # API 서버에 요청 보내기
        data = json.loads(r.read())         # 응답 데이터를 JSON 형태로 변환
    
    temp = data["main"]["temp"]             # 온도 값 추출
    humi = data["main"]["humidity"]         # 습도 값 추출
    
   
    label.config(text=f"{temp:.1f}C {humi}%")  # GUI 라벨에 온도와 습도 표시
    
    window.after(60000, tick1Min)  # 1분(60000ms) 후 함수 다시 실행 


window = tkinter.Tk()               # GUI 창 생성
window.title("TEMP HUMI DISPLAY")   # 창 제목 설정
window.geometry("400x100")          # 창 크기 설정
window.resizable(False, False)      # 창 크기 조절 비활성화

font = tkinter.font.Font(size=30)   # 폰트 크기 설정
label = tkinter.Label(window, text="", font=font)  # 텍스트 라벨 생성
label.pack()  # 라벨을 창에 배치

tick1Min()        # 프로그램 시작 시 즉시 날씨 데이터 요청
window.mainloop() # GUI 이벤트 루프 실행 (창 유지)