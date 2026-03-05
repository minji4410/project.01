import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="돌봄 근로자 건강 가이드", 
    page_icon="🦾", 
    layout="centered"
)

# 2. 메인 제목 및 소개
st.title("🦾 돌봄 근로자 근골격계 질환 예방")
st.write("돌봄 현장에서의 건강한 노동을 위해, 근골격계 질환 예방 정보를 제공합니다.")

# 3. 탭 구성
tab1, tab2, tab3 = st.tabs(["📌 자가진단", "📺 스트레칭 영상", "📝 예방 수칙"])

with tab1:
    st.header("🔍 나의 관절 건강은?")
    st.write("최근 일주일 동안 아래와 같은 통증을 느낀 적이 있나요?")
    
    q1 = st.checkbox("허리를 숙이거나 물건을 들 때 통증이 있다.")
    q2 = st.checkbox("손목이나 손가락 마디가 붓거나 쑤신다.")
    q3 = st.checkbox("어깨를 위로 올릴 때 걸리는 느낌이 든다.")
    q4 = st.checkbox("잠을 잘 때 목이나 어깨가 아파서 깬다.")
    
    if st.button("진단 결과 보기"):
        score = q1 + q2 + q3 + q4
        if score >= 3:
            st.error("🚨 **위험:** 통증이 심각합니다. 즉시 전문가와 상담하고 휴식을 취하세요!")
        elif score >= 1:
            st.warning("⚠️ **주의:** 근골격계 질환 초기 증상일 수 있습니다. 아래 스트레칭을 매일 따라하세요.")
        else:
            st.success("✅ **정상:** 아주 건강하시네요! 예방을 위해 꾸준히 관리해 주세요.")

with tab2:
    st.header("📺 현장에서 따라하는 3분 스트레칭")
    st.info("대상자를 돌보기 전후로 아래 영상을 보며 몸을 풀어주세요.")
    
    # 돌봄 노동자 근골격계 예방 관련 유튜브 영상 (예시 링크)
    st.video("https://www.youtube.com/watch?v=kYvMvE6VpI4")
    st.caption("출처: 안전보건공단 - 돌봄 종사자를 위한 근골격계 질환 예방")

with tab3:
    st.header("📝 올바른 작업 자세 3계명")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("✅ 할 것 (DO)")
        st.write("- 대상자와 최대한 몸을 가깝게 밀착하기")
        st.write("- 무릎을 굽히고 다리 힘으로 들어올리기")
        st.write("- 작업 중간중간 짧게 자주 휴식하기")
        
    with col2:
        st.subheader("❌ 하지 말 것 (DON'T)")
        st.write("- 허리만 숙여서 대상자 이동시키기")
        st.write("- 몸을 갑자기 비틀거나 회전하기")
        st.write("- 혼자서 무리하게 무거운 물건 들기")

# 4. 푸터 (조 정보)
st.divider()
st.write("👨‍👩‍👧‍👦 **제작: 00대학교 00과 조별과제**")
st.write("출처: 안전보건공단 및 근로복지공단 건강 가이드라인")
