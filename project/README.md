# 배당률 상위 기업 동일 투자금 기준 현금배당 비교

## 폴더 구조
sesac-project1/  
├─ src/ : 수집/정제 스크립트  
│  ├─ paths.py  
│  ├─ io_utils.py  
│  ├─ cleaning.py  
│  ├─ prepare_raw.py  
│  ├─ fetch_price_for_dividend_dates.py  
│  └─ check_results.py  
│  
├─ data/ : 원본 데이터  
│  ├─ dividend_info.csv  
│  ├─ dividend_info.parquet  
│  ├─ stock_price_20260102.csv  
│  └─ stock_price_20260102.parquet  
│  
├─ results/ : 정제된 원천 테이블(공유 산출물)  
│  ├─ dividend_raw.csv  
│  ├─ dividend_raw.parquet  
│  ├─ price_raw.csv  
│  └─ price_raw.parquet  
│
├─ notebooks/ : ipynb 파일들  
│  └─ 00_map_columns.ipynb  
│  
├─ .env (공유/커밋 제외)  
├─ .gitignore  
├─ requirements.txt  
└─ README.md  


## 실행 순서
src/ → 재현/검증용 (선택)  
results/ → 분석 시작점

results/dividend_raw.csv / results/dividend_raw.parquet  
→ 보통주 + 무배당 제외 + 핵심 5컬럼만 남긴 배당 원천 테이블 
results/price_raw.csv / results/price_raw.parquet  
→ isinCd, basDt, clpr만 남긴 시세 원천 테이블(기간 확장 반영)  

배당: scrsItmsKcdNm == "보통주"만  
무배당 제외: stckGenrDvdnAmt > 0 기준으로 제거  
최종 컬럼(배당):  
isinCd, stckIssuCmpyNm, dvdnBasDt, stckGenrDvdnAmt, stckGenrCashDvdnRt  
최종 컬럼(시세):  
isinCd, basDt, clpr  

## 실행 방법(재현 방법)
1. .env 파일 직접 생성 (키 넣기)
DATA_GO_STOCK_SERVICE_KEY=본인키
2. requirements.txt 파일 속 내용 설치
3. 원천 테이블 생성(필터 적용)
python -m src.prepare_raw
4. 결과 검증 리포트
python -m src.check_results
