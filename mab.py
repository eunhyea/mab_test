import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd
from scipy.stats import beta

class ThompsonSampling:
    def __init__(self, n_arms):
        self.n_arms = n_arms
        self.successes = np.ones(n_arms)
        self.failures = np.ones(n_arms)

    def select_arm(self):
        samples = [np.random.beta(self.successes[i], self.failures[i]) for i in range(self.n_arms)]
        return np.argmax(samples)

    def update(self, arm, reward):
        if reward == 1:
            self.successes[arm] += 1
        else:
            self.failures[arm] += 1

# 초기 설정
@st.cache_resource
def initialize_session():
    return {
        'ts': ThompsonSampling(n_arms=3),
        'total_interactions': 0,
        'arm_clicks': [0, 0, 0],
        'arm_closes': [0, 0, 0],
        'ad_exposures': []
    }

if 'session' not in st.session_state:
    st.session_state.session = initialize_session()

# Streamlit 앱 설정
st.title("최고의 캐릭터 찾기")
st.subheader("- MAB by Thompson Sampling")

# 이미지 파일 경로 설정
image_paths_p = {
    "짱구": "짱구.png",
    "폼폼푸린": "폼폼푸린.png",
    "하츄핑": "하츄핑.png",
}
image_paths_n = {
    "짱구": "삐진짱구.png",
    "폼폼푸린": "우는폼폼푸린.png",
    "하츄핑": "삐진하츄핑.png",
}

# 캐릭터 표시 및 상호작용
selected_arm = st.session_state.session['ts'].select_arm()
ad_names = ["짱구", "폼폼푸린", "하츄핑"]
colors = ["#e15241", "#97c15c", "#4350af"]
colors_dark = ["#a82d26", "#416829", "#1c2379"]

col1, col2 = st.columns(2)

def on_click(is_click):
    st.session_state.session['ad_exposures'].append(selected_arm)
    if is_click:
        st.session_state.session['ts'].update(selected_arm, 1)
        st.session_state.session['arm_clicks'][selected_arm] += 1
        st.session_state.last_action = "클릭"
    else:
        st.session_state.session['ts'].update(selected_arm, 0)
        st.session_state.session['arm_closes'][selected_arm] += 1
        st.session_state.last_action = "닫기"
    st.session_state.session['total_interactions'] += 1
    st.rerun()

with col1:
    st.image(image_paths_p[ad_names[selected_arm]], width=100)
    if st.button("캐릭터 클릭"):
        on_click(True)

with col2:
    st.image(image_paths_n[ad_names[selected_arm]], width=100)
    if st.button("캐릭터 닫기"):
        on_click(False)

# 마지막 액션 표시
if 'last_action' in st.session_state:
    if st.session_state.last_action == "클릭":
        st.success("캐릭터가 클릭되었습니다!")
    else:
        st.info("캐릭터를 클릭하지 않았습니다.")

# 결과 표시
st.write(f"총 상호작용 수: {st.session_state.session['total_interactions']}")
for i, name in enumerate(ad_names):
    st.write(f"{name} - 클릭 수: {st.session_state.session['arm_clicks'][i]}, 닫기 수: {st.session_state.session['arm_closes'][i]}")

# 각 캐릭터의 예상 클릭률 시각화 (Plotly 사용)
x = np.linspace(0, 1, 100)
fig = go.Figure()

for i in range(3):
    y = beta.pdf(x, st.session_state.session['ts'].successes[i], st.session_state.session['ts'].failures[i])
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=f'{ad_names[i]} 분포', line=dict(color=colors[i])))
    
    # 샘플링 결과 추가
    sample = np.random.beta(st.session_state.session['ts'].successes[i], st.session_state.session['ts'].failures[i])
    fig.add_trace(go.Scatter(
        x=[sample], 
        y=[0],  # y값을 0으로 설정하여 x축 위에 표시
        mode='markers',
        name=f'{ad_names[i]} 샘플',
        marker=dict(size=10, color=colors_dark[i], symbol='star')  # 마커를 'x'로 변경
    ))

fig.update_layout(
    title="각 캐릭터의 예상 클릭률 분포와 샘플링 결과",
    xaxis_title="클릭률",
    yaxis_title="확률 밀도",
    legend_title="캐릭터",
    xaxis=dict(range=[0, 1]),  # x축 범위를 0에서 1로 고정
    yaxis=dict(range=[0, None])  # y축의 최소값을 0으로 설정
)

st.plotly_chart(fig)

# 총 상호작용 수에 따른 캐릭터 노출 비율 누적 영역 차트 생성
def create_cumulative_exposure_plot():
    exposures = np.array(st.session_state.session['ad_exposures'])
    
    df = pd.DataFrame({
        'Iteration': range(1, len(exposures) + 1),
        'A_exposures': np.cumsum(exposures == 0),
        'B_exposures': np.cumsum(exposures == 1),
        'C_exposures': np.cumsum(exposures == 2),
    })
    
    df['A_ratio'] = df['A_exposures'] / df['Iteration']
    df['B_ratio'] = df['B_exposures'] / df['Iteration']
    df['C_ratio'] = df['C_exposures'] / df['Iteration']
    
    fig_area = go.Figure()
    
    fig_area.add_trace(go.Scatter(
        x=df['Iteration'], y=df['A_ratio'], mode='lines', name=ad_names[0],
        stackgroup='one', line=dict(width=0.5, color='#e15241')
    ))
    
    fig_area.add_trace(go.Scatter(
        x=df['Iteration'], y=df['B_ratio'], mode='lines', name=ad_names[1],
        stackgroup='one', line=dict(width=0.5, color='#97c15c')
    ))
    
    fig_area.add_trace(go.Scatter(
        x=df['Iteration'], y=df['C_ratio'], mode='lines', name=ad_names[2],
        stackgroup='one', line=dict(width=0.5, color='#4350af')
    ))
    
    fig_area.update_layout(
        title="총 상호작용 수에 따른 캐릭터 노출 비율",
        xaxis_title="총 상호작용 수",
        yaxis_title="노출 비율",
        showlegend=True
    )
    
    return fig_area

# 누적 클릭률과 닫기율 차트 생성
def create_cumulative_rates_plot():
    exposures = np.array(st.session_state.session['ad_exposures'])
    clicks = np.array(st.session_state.session['arm_clicks'])
    closes = np.array(st.session_state.session['arm_closes'])
    
    df = pd.DataFrame({
        'Iteration': range(1, len(exposures) + 1),
        'A_clicks': np.cumsum(exposures == 0) * (clicks[0] / max(1, exposures.tolist().count(0))),
        'B_clicks': np.cumsum(exposures == 1) * (clicks[1] / max(1, exposures.tolist().count(1))),
        'C_clicks': np.cumsum(exposures == 2) * (clicks[2] / max(1, exposures.tolist().count(2))),
        'A_closes': np.cumsum(exposures == 0) * (closes[0] / max(1, exposures.tolist().count(0))),
        'B_closes': np.cumsum(exposures == 1) * (closes[1] / max(1, exposures.tolist().count(1))),
        'C_closes': np.cumsum(exposures == 2) * (closes[2] / max(1, exposures.tolist().count(2)))
    })
    
    fig_rates = go.Figure()
    
    for i, name in enumerate(ad_names):
        fig_rates.add_trace(go.Scatter(
            x=df['Iteration'], 
            y=df[f'{chr(65+i)}_clicks'] / df['Iteration'], 
            mode='lines', 
            name=f'{name} 클릭률',
            line=dict(color=colors[i])
        ))
        fig_rates.add_trace(go.Scatter(
            x=df['Iteration'], 
            y=df[f'{chr(65+i)}_closes'] / df['Iteration'], 
            mode='lines', 
            name=f'{name} 닫기율',
            line=dict(color=colors_dark[i], dash='dash')
        ))
    
    fig_rates.update_layout(
        title="누적 클릭률과 닫기율",
        xaxis_title="총 상호작용 수",
        yaxis_title="비율",
        showlegend=True
    )
    
    return fig_rates


# 누적 영역 차트 표시
st.plotly_chart(create_cumulative_exposure_plot())

# 누적 클릭률과 닫기율 차트 표시
st.plotly_chart(create_cumulative_rates_plot())

