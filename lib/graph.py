import pandas as pd
import plotly.express as px
import streamlit as st

def preprocess_data(data):
    preprocessed_data = {}
    for website, details in data.items():
        min_co2 = float('inf')
        min_co2_details = None
        for detail_id, detail_data in details.items():
            if detail_data.get('g of CO2', float('inf')) < min_co2:
                min_co2 = detail_data['g of CO2']
                min_co2_details = detail_data
        if min_co2_details:
            preprocessed_data[website] = {min_co2_details['link']: min_co2_details}
    return preprocessed_data

def convert_carbon_bound(data):
    percentiles = [0, 5, 10, 20, 30, 50, 100]
    tier = ['A+', 'A', 'B', 'C', 'D', 'F']
    percentile_values = [p / 100 for p in percentiles]
    percentile_values = data['CO2'].quantile(percentile_values).tolist()
    carbon_upper_bound = []
    datasets = []

    for i in range(len(percentile_values) - 1):
        lower_bound = percentile_values[i]
        upper_bound = percentile_values[i + 1]
        carbon_upper_bound.append(upper_bound)
        subset = data[(data['CO2'] >= lower_bound) & (data['CO2'] < upper_bound)]
        # datasets.append((f"{tier[i]}: 하위 {percentiles[i]}~{percentiles[i+1]}% 구간의 데이터 ", subset))
        datasets.append((tier[i], subset))
    return datasets

def plot_comparison(datasets, new_data, search, tier):
    all_data = []

    # 정해진 구간별 데이터 분포
    for label, dataset in datasets:
        dataset.columns = [col.upper() for col in dataset.columns]
        mean_values = dataset[['CSS', 'FETCH', 'IMG', 'LINK', 'SCRIPT', 'VIDEO']].mean().reset_index()
        mean_values.columns = ['resource', 'average_usage']
        mean_values['label'] = label
        all_data.append(mean_values)
    
    # 새로 들어오는 데이터 분포
    new_data_upper = {k.upper(): v for k, v in new_data.items()}
    new_mean_values = pd.DataFrame(new_data_upper.items(), columns=['resource', 'average_usage'])
    new_mean_values['label'] = search
    all_data.append(new_mean_values)

    # 모든 데이터를 하나의 데이터프레임으로 결합
    combined_data = pd.concat(all_data, ignore_index=True)

    # 그래프 생성
    fig = px.bar(combined_data, x='resource', y='average_usage', color='label', 
                 barmode='group', title='자원별 평균 사용량 비교', 
                 labels={'average_usage': '평균 사용량', 'resource': '자원', 'label': '데이터셋'})
    fig.for_each_trace(lambda trace: trace.update(visible='legendonly'))
    fig.for_each_trace(lambda trace: trace.update(visible=True) if trace.name == tier or trace.name == search else trace)
    st.plotly_chart(fig)