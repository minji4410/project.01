import streamlit as st

# 사이트 기본 설정 (제목, 아이콘)
st.set_page_config(page_title="건강 정보 가이드", page_icon="🏥")

# 메인 화면 문구
st.title("🏥 모두를 위한 건강 상식")
st.subheader("바쁜 일상 속, 1분만 투자하세요!")

# 메뉴 구성
category = st.selectbox("관심 있는 주제를 선택하세요", ["거북목 예방", "올바른 영양제 섭취", "간단 스트레칭"])

if category == "거북목 예방":
    st.write("### 🐢 거북목 탈출법")
    st.info("모니터를 눈높이로 올리는 것만으로도 목의 부담이 5kg 줄어듭니다.")
    st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=500") # 예시 이미지

elif category == "올바른 영양제 섭취":
    st.write("### 💊 비타민, 언제 먹나요?")
    st.write("- 종합비타민: 식사 직후 (흡수율 UP)")
    st.write("- 유산균: 아침 공복 (생존율 UP)")

else:
    st.write("### 🧘 1분 스트레칭")
    st.success("지금 바로 기지개를 한 번 켜보세요!")

# 하단 정보
st.divider()
st.caption("제작: 00대학교 00과 0조 | 출처: 보건복지부")