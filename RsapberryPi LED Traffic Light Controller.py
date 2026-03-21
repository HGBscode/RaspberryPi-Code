from gpiozero import LED # GPIO 핀 제어를 위한 LED 라이브러리 불러오기
from time import sleep # 지연 시간(대기 시간)을 위한 sleep 함수 불러오기

# 핀 번호 설정(변수 선언)
carLedRed = 2           # 차량 빨간불: GPIO 2번
carLedYellow = 3        # 차량 노란불: GPIO 3번
carLedGreen = 4         # 차량 초록불: GPIO 4번
humanLedRed = 20        # 보행자 빨간불: GPIO 20번
humanLedGreen = 21      # 보행자 초록불: GPIO 21번

# LED 객체 생성
carLedRed = LED(2)
carLedYellow = LED(3)
carLedGreen = LED(4)
humanLedRed = LED(20)
humanLedGreen = LED(21)

try:
    while 1: #무한반복 시작
        carLedRed.value = 0      # 차량 빨간불 OFF
        carLedYellow.value = 0   # 차량 노란불 OFF
        carLedGreen.value = 1    # 차량 초록불 ON
        humanLedRed.value = 1    # 보행자 빨간불 ON
        humanLedGreen.value = 0  # 보행자 초록불 OFF
        sleep(3.0)               # 3초 유지
        
        carLedRed.value = 0      # 차량 빨간불 OFF
        carLedYellow.value = 1   # 차량 노란불 ON
        carLedGreen.value = 0    # 차량 초록불 OFF
        humanLedRed.value = 1    # 보행자 빨간불 ON
        humanLedGreen.value = 0  # 보행자 초록불 OFF
        sleep(1.0)               # 1초 유지
        
        carLedRed.value = 1      # 차량 빨간불 ON
        carLedYellow.value = 0   # 차량 노란불 OFF
        carLedGreen.value = 0    # 차량 초록불 OFF
        humanLedRed.value = 0    # 보행자 빨간불 OFF
        humanLedGreen.value = 1  # 보행자 초록불 ON
        sleep(3.0)               # 3초 유지

except KeyboardInterrupt:
    # 사용자가 Ctrl + C를 눌러 프로그램을 종료
    pass

# 프로그램 종료 시 모든 LED등 끄기
carLedRed.value = 0
carLedYellow.value = 0        
carLedGreen.value = 0        
humanLedRed.value = 0     
humanLedGreen.value = 0