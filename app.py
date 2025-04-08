import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import re

def extract_video_id(url):
    """YouTube URL에서 비디오 ID를 추출합니다."""
    patterns = [
        r'(?:v=|\/)([0-9A-Za-z_-]{11}).*',
        r'(?:be\/)([0-9A-Za-z_-]{11}).*'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def get_transcript(video_id):
    """YouTube 동영상의 자막을 가져옵니다."""
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['ko', 'en'])
        return ' '.join([t['text'] for t in transcript_list])
    except TranscriptsDisabled:
        return None
    except Exception as e:
        return None

def summarize_text(text, sentences_count=5):
    """텍스트를 요약합니다."""
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return ' '.join([str(sentence) for sentence in summary])

# Streamlit UI
st.title('🎥 YouTube 동영상 요약 봇')
st.write('YouTube 동영상 URL을 입력하면 내용을 요약해드립니다.')

url = st.text_input('YouTube URL을 입력하세요:')

if url:
    video_id = extract_video_id(url)
    
    if video_id:
        st.video(f'https://www.youtube.com/watch?v={video_id}')
        
        with st.spinner('자막을 가져오는 중...'):
            transcript = get_transcript(video_id)
        
        if transcript:
            with st.spinner('내용을 요약하는 중...'):
                try:
                    summary = summarize_text(transcript)
                    st.success('요약이 완료되었습니다!')
                    st.write('### 요약 내용')
                    st.write(summary)
                except Exception as e:
                    st.error('요약 중 오류가 발생했습니다. 다시 시도해주세요.')
        else:
            st.error('이 동영상의 자막을 가져올 수 없습니다. 자막이 비활성화되어 있거나 지원되지 않는 형식일 수 있습니다.')