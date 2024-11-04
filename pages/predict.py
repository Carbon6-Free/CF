import streamlit as st
from PIL import Image
import requests
import time

url = "http://localhost:8000/make_model"

def click(file_path):
    result_image = Image.open(file_path[-4]+".png")
    return result_image

def main():
    st.title("AutoML Training")

    file_path = st.text_input("data", "/path/to/your/file.csv")
    max_trials = st.text_input("max trials:", "50")
    epochs = st.text_input("epochs:", "20")
    if st.button("학습 시작"):
        if not file_path:
            st.warning("파일 경로를 입력하세요.")
        else:
            data = {"path": file_path, "max_trials": max_trials, "epochs": epochs} 
            start_time = time.time()
            elapsed_placeholder = st.empty()

            with st.spinner("학습 중..."):
                response = requests.post(url, json=data, timeout=300)

            elapsed_time = time.time() - start_time

            elapsed_placeholder.success(f"학습 및 예측 완료! 소요 시간: {elapsed_time:.2f} seconds")

            loss_image = Image.open(f"{file_path[:-4]}_loss.png")
            pred_image = Image.open(f"{file_path[:-4]}_prediction_results.png")

            st.image(loss_image, caption="학습 결과 loss", use_column_width=True)
            st.image(pred_image, caption="예측 결과", use_column_width=True)

if __name__ == "__main__":
    main()
