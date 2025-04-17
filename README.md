# 🧭 프로젝트 개요

## 🎯 의도

> 숏폼 콘텐츠의 중독성, 일반인 데이터 수집을 통한 과소비 유도, 편향적이고 자극적인 기사 노출이 심화되는 상황 속에서  
> **균형 잡힌 시각과 태도를 갖고자 하는 사람들에게 필요한 서비스를 제공**합니다.

---

## 🧠 기획

- 정치, 경제, 사회 분야에서 자극적인 뉴스 소비로 인해 발생하는 **편향성**을 보완합니다.
- 유저가 특정 성향의 기사만 소비할 경우, **반대 의견의 기사**를 자동 노출시켜 **균형 있는 시각**을 가질 수 있도록 유도합니다.

---

## ⚖️ 법률적 기준

- **RSS 및 공식 API**를 통한 합법적인 뉴스 데이터만 수집합니다.
- 수익화는 **직접 가공한 요약 및 분석 데이터**만을 기반으로 진행하며, 원본 뉴스 데이터는 광고 등 수익화에 사용하지 않습니다.

---

## 💰 비즈니스 모델 (BM)

- 기본 서비스는 **광고 기반 무료 모델**입니다.
- **일간 뉴스**로는 파악하기 어려운 정치/사회적 흐름 및 소비 성향은  
  **일간/주간/월간 리포트 형태의 구독형 유료 서비스**로 제공합니다.

---

## 🛠️ 개발 구조

### ▪ Frontend

- 초기 버전은 **React 기반 웹**으로 제공
- 향후에는 **Flutter 앱**으로 확장 예정 (웹뷰 포함)

### ▪ Backend

- **Python 서비스 (Collector):**
  - 뉴스사 RSS 수집 및 기사 본문 스크래핑
  - 기사 요약 (LLM API 활용)
  - 정치성향 분석 (NLP)
  
- **Go 서비스 (API/Business Logic):**
  - 사용자 요청 처리 및 유저 편향도 분석
  - 반대 성향 기사 추천 ("Counter" 기능)
  - 사용자 정보 및 열람 기록 관리

### ▪ DevOps

- **AWS EC2**를 활용한 인프라
- **CI/CD:** GitHub Actions + ArgoCD로 자동화

---

## 📣 마케팅 전략

- 정치, 경제, 사회, 환경 이슈에 관심 있는 **의식 있는 타겟 유저층**을 중심으로 광고 집행
- **자연스럽게 균형 잡힌 시각을 가질 수 있음**을 강조:
  - 자주 클릭하는 기사 성향과 반대되는 콘텐츠를 자동으로 추천
- **이메일 마케팅 전략:**
  - 유료 콘텐츠 무상 제공을 미끼로 이메일 수집
  - 이메일 입력 수를 **잠재 유저 인입 수**로 활용

---

