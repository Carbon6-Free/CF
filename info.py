import random
import streamlit as st
from PIL import Image

info = [
    "난방온도 2℃ 낮추고 냉방온도 2℃ 높이기",
    "전기밥솥 보온기능 사용 줄이기",
    "냉장고 적정용량 유지하기",
    "비데 절전기능 사용하기",
    "물은 받아서 사용하기",
    "텔레비전 시청 시간 줄이기",
    "세탁기 사용횟수 줄이기",
    "디지털 탄소발자국 줄이기",
    "창틀과 문틈 바람막이 설치하기",
    "가전제품 대기전력 차단하기",
    "절수 설비 또는 절수 기기 설치하기",
    "고효율 가전제품 사용하기",
    "친환경 콘텐싱 보일러 사용하기",
    "주기적으로 보일러 청소하기",
    "LED 조명으로 교체하기",
    "가정 내 지역난방배관 청소하기",
    "음식물 쓰레기 줄이기",
    "저탄소 제품 구매하기",
    "저탄소 인증 농축산물 이용하기",
    "품질이 보증되고 오래 사용 가능한 제품 사기",
    "과대포장 제품 안 사기",
    "재활용하기 쉬운 재질·구조로 된 제품 구매하기",
    "우리나라, 우리 지역 식재료 이용하기",
    "개인용 자동차 대신 대중교통 이용하기",
    "친환경 운전 실천하기",
    "자동차 타이어 공기압과 휠 정기적으로 점검하기",
    "가까운 거리는 걷거나 자전거 이용하기",
    "전기·수소 자동차 구매하기",
    "재활용을 위한 분리배출 실천하기",
    "종이타월, 핸드드라이어 대신 개인손수건 사용하기",
    "장바구니 이용하고 비닐 사용 줄이기",
    "1회용 컵 대신 다회용 컵 사용하기",
    "물티슈 덜 쓰기",
    "음식 포장 시 1회용품 줄이기",
    "인쇄 시 종이 사용 줄이기",
    "청구서, 영수증 등의 전자적 제공 서비스 이용",
    "정부, 기업, 단체 등에서 추진하는 나무 심기 운동 참여하기",
    "탄소흡수원의 중요성을 알고 보호하기",
    "기념일에 내(가족) 나무 심어 보기"
]

def carbon_info(carbon_g):
    if carbon_g < 1:
        pass
    elif carbon_g < 10:
        st.image('./pic/light4.png', width=500)
        st.write("링크 10회 방문시 형광등 40분을 사용한 탄소가 발생됩니다.")
    elif carbon_g < 20:
        st.image('./pic/light8.png', width=500)
        st.write("링크 10회 방문시 형광등 80분을 사용한 탄소가 발생됩니다.")
    elif carbon_g < 30:
        st.image('./pic/tv3.png', width=500)
        st.write("링크 10회 방문시 TV를 30분동안 사용한 탄소가 발생됩니다.")
    elif carbon_g < 40:
        st.image('./pic/phone.png', width=500)
        st.write("링크 10회 방문시 스마트폰을 2시간동안 사용한 탄소가 발생됩니다.")
    elif carbon_g < 50:
        st.image('./pic/aircon.png', width=500)
        st.write("링크 10회 방문시 에어컨을 15분동안 사용한 탄소가 발생됩니다.")
    elif carbon_g < 60:
        st.image('./pic/com4.png', width=500)
        st.write("링크 10회 방문시 컴퓨터 4시간동안 사용한 탄소가 발생합니다.")
    elif carbon_g < 70:
        st.image('./pic/wash2.png', width=500)
        st.write("링크 10회 방문시 세탁기를 20분동안 사용한 탄소가 발생합니다.")
    elif carbon_g < 80:
        st.image('./pic/oven3.png', width=500)
        st.write("링크 10회 방문시 전자레인지를 30분동안 사용한 탄소가 발생합니다.")
    elif carbon_g > 100:
        st.image('./pic/car.png', width=500)
        st.write(f"링크 10회 방문시 발생되는 탄소는 약 {int(carbon_g)}g 입니다. 차로 2.5km를 이동했을때 발생되는 탄소는 560g 입니다.")


def display_random_info():
    selected_info = random.choice(info)
    st.markdown(
        f'<div class="fixed-bottom-right">{selected_info}</div>',
        unsafe_allow_html=True
    )
