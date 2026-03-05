import streamlit as st

# 1. 페이지 설정 및 접근성 스타일
st.set_page_config(page_title="돌봄 건강 지킴이", page_icon="🦾", layout="wide")

st.markdown("""
    <style>
    .main-title { font-size: 32px !important; color: #2E7D32; font-weight: bold; }
    .section-header { font-size: 26px !important; color: #1565C0; font-weight: bold; border-bottom: 2px solid #1565C0; padding-bottom: 5px; margin-top: 30px; }
    .tip-box { background-color: #F1F8E9; padding: 15px; border-radius: 10px; border-left: 5px solid #4CAF50; }
    .care-box { background-color: #E3F2FD; padding: 15px; border-radius: 10px; border-left: 5px solid #2196F3; }
    </style>
    """, unsafe_allow_html=True)

# 2. 메인 제목
st.markdown('<p class="main-title">🦾 돌봄 노동자·보호자 근골격계 예방 사이트</p>', unsafe_allow_html=True)
st.info("💡 아래 메뉴에서 궁금한 항목을 선택하거나 화면을 아래로 내려보세요.")
choice = st.radio("바로가기", ["전체 보기", "🛡️ 돌봄 시 예방 수칙", "🦒 목·어깨", "🧍 허리", "👐 손목", "🦶 다리·발목"], horizontal=True)

st.divider()
# --- 섹션 0: 자가진단 (추가된 부분) ---
if choice == "전체 보기" or choice == "📊 자가진단":
    st.markdown('<p class="section-header">📊 근골격계 통증 자가진단</p>', unsafe_allow_html=True)
    st.write("현재 본인의 몸 상태를 체크해보세요. (최근 1주일 기준)")
    
    with st.container():
        st.markdown('<div class="diag-box">', unsafe_allow_html=True)
        c1 = st.checkbox("물건을 들거나 대상자를 옮길 때 허리에 통증이 있다.")
        c2 = st.checkbox("자고 일어났을 때 목이나 어깨가 뻣뻣하고 움직이기 힘들다.")
        c3 = st.checkbox("손목이나 손가락 마디가 붓거나 찌릿한 느낌이 있다.")
        c4 = st.checkbox("운전이나 보행 시 발목 혹은 종아리에 쥐가 자주 난다.")
        c5 = st.checkbox("통증 때문에 밤에 잠을 설친 적이 있다.")
        
        if st.button("진단 결과 확인하기"):
            score = c1 + c2 + c3 + c4 + c5
            if score >= 4:
                st.error("🚨 **위험:** 신체 부담이 매우 높습니다. 즉시 전문가와 상담하고 휴식을 취하세요!")
            elif score >= 1:
                st.warning("⚠️ **주의:** 근골격계 질환 초기 증상입니다. 아래의 부위별 스트레칭을 매일 실천하세요.")
            else:
                st.success("✅ **양호:** 현재 건강한 상태입니다. 예방 수칙을 지켜 건강을 유지하세요!")
        st.markdown('</div>', unsafe_allow_html=True)
        
# --- 섹션 1: 돌봄 대상자 케어 시 예방 수칙 (추가된 부분) ---
if choice == "전체 보기" or choice == "🛡️ 돌봄 시 예방 수칙":
    st.markdown('<p class="section-header">🛡️ 돌봄 대상자 케어 시 부상 예방 수칙</p>', unsafe_allow_html=True)
    st.write("대상자를 이동시키거나 자세를 바꿀 때 아래 수칙을 반드시 지켜주세요.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown('<div class="care-box"><b>✅ 안전한 이동 돕기 (DO)</b><br>'
                    '- 대상자와 최대한 몸을 밀착하여 무게 중심 낮추기<br>'
                    '- 허리가 아닌 무릎을 굽히고 다리 힘으로 들어올리기<br>'
                    '- 이동 전 대상자에게 동작을 미리 알리고 협조 구하기</div>', unsafe_allow_html=True)
    with col_b:
        st.markdown('<div class="care-box" style="border-left-color: #F44336;"><b>❌ 위험한 자세 (DON\'T)</b><br>'
                    '- 무릎을 편 채 허리만 숙여서 힘쓰기<br>'
                    '- 대상자를 잡고 갑자기 몸을 비틀거나 회전하기<br>'
                    '- 혼자서 무리하게 무거운 대상을 이동시키기</div>', unsafe_allow_html=True)

# --- 섹션 2: 목·어깨 ---
if choice == "전체 보기" or choice == "🦒 목·어깨":
    st.markdown('<p class="section-header">🦒 섹션 1. 목과 어깨 통증</p>', unsafe_allow_html=True)
    
    # 세 개의 칸을 만듭니다 (영상1, 영상2, 팁박스)
    col1, col2, col3 = st.columns([1, 1, 1]) 
    
    with col1:
        st.subheader("📺 스트레칭 1")
        st.video("https://youtube.com/watch?v=ltjTJj1jv4A?si=f6tuQ7Vbhkulwun4")
        st.write("어깨와 승모근이 아플때 앉아서 하기 좋습니다.")

    with col2:
        st.subheader("📺 스트레칭 2")
        st.video("https://youtube.com/watch?v=sFMjbukgq4s?si=PDyfgsuPkYU371wF") 
        st.write("목이 뻐근할 때 하기 좋습니다.")

    with col3:
        st.markdown('<div class="tip-box"><b>🏥 일상 팁</b><br>- 스마트폰 사용 시 눈높이 맞추기<br>- 수시로 기지개 켜기</div>', unsafe_allow_html=True)
        
# --- 섹션 3: 허리 ---
if choice == "전체 보기" or choice == "🧍 허리":
    st.markdown('<p class="section-header">🧍 섹션 2. 허리 통증</p>', unsafe_allow_html=True)
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.video("https://youtube.com/watch?v=33C8ujK5drw?si=ZyQtTkQpU1_Ut6lU")
    with col2:
        st.markdown('<div class="tip-box"><b>🏥 일상 팁</b><br>- 오래 서 있을 때 발판에 발 교대로 올리기<br>- 틈틈이 허리 젖히기 운동</div>', unsafe_allow_html=True)

# --- 섹션 4: 손목 ---
if choice == "전체 보기" or choice == "👐 손목":
    st.markdown('<p class="section-header">👐 섹션 3. 손목 통증</p>', unsafe_allow_html=True)
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.video("https://youtube.com/watch?v=waEegh-wIVU?si=ctCRkwjO2JKagVl6")
    with col2:
        st.markdown('<div class="tip-box"><b>🏥 일상 팁</b><br>- 손바닥을 벽에 대고 스트레칭 하기<br>- 무거운 조리도구 양손 사용하기</div>', unsafe_allow_html=True)

# --- 섹션 5: 다리·발목 ---
if choice == "전체 보기" or choice == "🦶 다리·발목":
    st.markdown('<p class="section-header">🦶 섹션 4. 다리와 발목 (운전 포함)</p>', unsafe_allow_html=True)
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.video("https://youtube.com/watch?v=GrWC9JgnAEE?si=fUXjzWGPShlirA6_")
    with col2:
        st.markdown('<div class="tip-box"><b>🏥 일상 팁</b><br>- 1시간 운전 후 꼭 내려서 걷기<br>- 발목 돌리기와 까치발 운동</div>', unsafe_allow_html=True)

# 4. 푸터
st.write("---")
st.caption("제작: 00대학교 물리치료학과 조별과제 (조장: 김민지)")
st.caption("자료 출처: 안전보건공단 및 근로복지공단 건강 가이드라인")


