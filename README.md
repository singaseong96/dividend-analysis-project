# 💰 주린이를 위한 실질 배당 수령액 분석 시뮬레이터
> **배당률의 함정에서 벗어나, 내 투자금으로 실제로 받을 수 있는 현금을 확인하세요!**

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=Pandas&logoColor=white)

---

## 🔍 프로젝트 개요
일반 투자자들은 배당주를 선택할 때 **표면적인 배당률**을 주요 기준으로 삼습니다. 하지만 주가 수준에 따라 실제로 살 수 있는 주식 수가 달라지며, 이는 **실제 수령 배당금**의 차이로 이어집니다. 본 프로젝트는 동일 금액 투자 시 기업별 실제 현금 배당액을 비교 분석하여 주린이들에게 현실적인 가이드를 제공합니다.

### ❓ 핵심 질문 (Problem Definition)
1. **배당률 상위 기업**에 동일 금액을 투자했을 때, 실제 총 배당금은 얼마나 차이 나는가?
2. **배당률**과 **실제 배당 효율**은 항상 비례하는가?
3. 배당률이 낮더라도 **주가가 낮은 기업**이 더 높은 실질 배당 효율을 보이는 경우가 있는가?

---

## ✨ 주요 기능
- **실시간 시뮬레이션**: 사용자가 직접 투자 원금을 설정 (기본 1,000만 원)
- **세금 계산기**: 배당소득세(15.4%) 공제 전/후 금액 선택 기능
- **다크 모드 지원**: 사용자 환경에 최적화된 시각화 대시보드
- **TOP 랭킹 분석**: 실제 수령액 기준 상위 기업 리스트업 및 산점도 분석

---

## 📊 사용 데이터 및 분석 방법론
- **데이터 소스**: 금융위원회 주식배당정보 및 주식시세정보 API (KRX 기준)
- **분석 로직**:
  - `매수 가능 주식 수` = $Investment / Stock\ Price$ (정수 매수 가정)
  - `총 현금 배당금` = $Shares \times Dividend\ per\ Share$
  - `실제 배당 수익률` = $Total\ Dividend / Investment \times 100$

---

## 🚀 실행 방법 (Local)

1. 저장소 클론
   ```bash
   git clone [https://github.com/singaseong96/dividend-analysis-project.git](https://github.com/singaseong96/dividend-analysis-project.git)