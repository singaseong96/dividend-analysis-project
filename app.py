import streamlit as st
import pandas as pd
import plotly.express as px

# 0. 기본 설정
st.set_page_config(page_title="배당 효율 분석기", layout="wide")

# 다크/라이트 모드 자동 대응 CSS
st.markdown("""
    <style>
    /* 1. 지표(Metric) 박스 설정: 배경은 반투명하게, 글자는 테마에 따라 자동변경 */
    div[data-testid="stMetric"] {
        background-color: rgba(128, 128, 128, 0.1) !important;
        border: 1px solid rgba(128, 128, 128, 0.2) !important;
        padding: 20px !important;
        border-radius: 12px !important;
    }
    
    /* 2. 메트릭 레이블(소제목) 색상 */
    div[data-testid="stMetricLabel"] > div {
        color: var(--text-color) !important;
        opacity: 0.8;
    }

    /* 3. 메트릭 수치 색상: 가독성을 위해 포인트 컬러 사용 */
    div[data-testid="stMetricValue"] > div {
        color: #0080FF !important; /* 다크/라이트 모두 잘 보이는 파란색 */
    }

    /* 4. 차트 주변 여백 조정 */
    .block-container {
        padding-top: 2rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. 데이터 로드
@st.cache_data
def load_local_data():
    df = pd.read_csv('./results/final_dataset_efficiency_rank.csv')
    return df

try:
    df = load_local_data()
    
    # 2. 사이드바
    with st.sidebar:
        st.header("⚙️ 분석 설정")
        investment = st.number_input("투자 원금 (원)", value=10000000, step=1000000)
        tax_apply = st.checkbox("배당소득세(15.4%) 공제", value=True)
        top_n = st.slider("상위 종목 개수", 5, 20, 10)

    # 3. 계산 로직
    df['실제매수수량'] = investment // df['종가']
    df['실제수령액'] = df['실제매수수량'] * df['1주당배당금']
    if tax_apply:
        df['실제수령액'] = df['실제수령액'] * (1 - 0.154)
    df['실제수익률'] = (df['실제수령액'] / investment) * 100

    # 4. 메인 화면
    st.title("💰 주린이 배당금 체감 분석기")
    
    # 상단 요약 카드 (다크모드 대응)
    top_1 = df.sort_values('실제수령액', ascending=False).iloc[0]
    m1, m2, m3 = st.columns(3)
    m1.metric("수령액 1위", top_1['기업명'])
    m2.metric("실제 수령액", f"{top_1['실제수령액']:,.0f}원")
    m3.metric("실제 수익률", f"{top_1['실제수익률']:.2f}%")

    st.divider()

    # 5. 시각화 (Plotly는 템플릿 설정을 통해 자동 대응)
    col1, col2 = st.columns(2)
    
    # 시스템 테마에 맞춰 Plotly 테마 자동 선택
    # streamlit의 현재 테마 정보를 가져올 수 없으므로, 투명 배경을 활용합니다.
    
    with col1:
        st.subheader(f"📊 TOP {top_n} 실제 배당금 순위")
        fig_bar = px.bar(df.sort_values('실제수령액', ascending=False).head(top_n),
                        x='기업명', y='실제수령액',
                        text_auto=',.0f',
                        color='실제수령액', 
                        color_continuous_scale='Blues')
        
        # 그래프 글자색을 시스템 테마에 맡기기 위해 배경 투명화
        fig_bar.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(size=12) # 글자색을 명시하지 않으면 시스템 테마를 따릅니다.
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    with col2:
        st.subheader("🧐 배당률 vs 실제 수익률")
        fig_scatter = px.scatter(df.head(50), 
                                x='투자금대비배당률(%)', y='실제수익률',
                                size='실제수령액', hover_name='기업명',
                                color='실제수령액', 
                                color_continuous_scale='Viridis')
        
        fig_scatter.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

    # 6. 테이블
    st.subheader("📋 상세 데이터")
    st.dataframe(df[['기업명', '종가', '1주당배당금', '실제매수수량', '실제수령액', '실제수익률']]
                 .sort_values('실제수령액', ascending=False), use_container_width=True)

except Exception as e:
    st.error(f"데이터 로드 오류: {e}")