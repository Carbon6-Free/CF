# Carbon6 Free

파일구조
```
├── assets # 웹페이지 결과에 뜨는 탄소 등급 에셋
│   ├── *.png
├── carbonfree.json # firebase에서 수집한 웹페이지별 메타데이터
├── chromedriver
├── cutoff.txt
├── info.py # 웹페이지 우측 하단에 개인이 실천할 수 있는 탄소줄이는법 툴팁을 띄우기위한 기능
├── lib
│   ├── crawler_module.py # 웹페이지의 자원 데이터를 크롤링하는 모델. firebase에도 저장된다
│   ├── cutoff.py # carbonfree.json을 기반으로 [0, 5, 10, 20, 30, 50, 100]% 구간을 판별하는 탄소값 측정 및 cutoff.txt에 저장
│   ├── graph.py # 결과화면에 보여줄 시각화 코드
│   └── network_carborn.py # 웹페이지 방문시 발생하는 탄소 예측계산
├── main.py # streamlit기반으로 웹페이지를 검색하고 탄소를 측정하고, cutoff등급에 따라 검색한 웹페이지의 탄소등급을 보여주는 기능
└── style.py # streamlit보다 상위의 html, css, js개념에서 디자인 스타일 지정 기능
```

