import streamlit as st

def app():
    # st.title()
    


# HTML과 CSS를 사용하여 풀스크린 유튜브 동영상 설정
    youtube_html = '''
    <style>
    .video-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1; /* 배경으로 보내기 위해 음수 인덱스 사용 */
        overflow: hidden;
    }

    iframe {
        width: 100vw;
        height: 100vh;
        border: none;
    }
    </style>

    <div class="video-container">
        <iframe src="https://www.youtube.com/embed/VIDEO_ID?autoplay=1&mute=1&loop=1&playlist=VIDEO_ID" 
                frameborder="0" 
                allow="autoplay; fullscreen">
        </iframe>
    </div>
    '''

# sv2INkTl2JM
    # 동영상 ID를 실제 동영상 ID로 변경
    youtube_html = youtube_html.replace("VIDEO_ID", "whO-K1nU-H4")  # 실제 동영상 ID로 대체

    # HTML을 사용하여 CSS 및 비디오 추가
    st.markdown(youtube_html, unsafe_allow_html=True)

    # 애플리케이션 내용
    # st.title("풀스크린 유튜브 동영상이 있는 Streamlit 앱")
    # st.write("이 애플리케이션은 풀스크린 유튜브 동영상을 배경으로 사용합니다.")

      


