import streamlit as st
import os

st.title('간단한 메모장')

# 메모 입력 영역
memo = st.text_area('메모 입력', height=200)
save_button = st.button('저장')

# 저장 버튼 클릭 시 동작
if save_button:
    # 기존 메모 읽기
    if os.path.exists('memos.txt'):
        with open('memos.txt', 'r', encoding='UTF-8') as file:
            saved_memos = file.readlines()
    else:
        saved_memos = []

    # 새로운 메모 추가
    saved_memos.append(memo.strip() + '\n')

    # 업데이트된 메모 저장
    with open('memos.txt', 'w', encoding='UTF-8') as file:
        file.writelines(saved_memos)
    
    st.success('메모가 저장되었습니다!')

# 저장된 메모 목록 표시
st.subheader('저장된 메모 목록')
try:
    with open('memos.txt', 'r', encoding='UTF-8') as file:
        saved_memos = file.readlines()
        if saved_memos:
            for idx, m in enumerate(saved_memos, 1):
                st.write(f"{idx}. {m.strip()}")
        else:
            st.info('저장된 메모가 없습니다.')
except FileNotFoundError:
    st.info('저장된 메모가 없습니다.')
