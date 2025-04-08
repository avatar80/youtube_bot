# YouTube 동영상 요약 봇

YouTube 동영상의 자막을 추출하여 내용을 요약해주는 Streamlit 애플리케이션입니다.

## 주요 기능

- YouTube URL 입력으로 간편한 사용
- 자동 자막 추출 (한국어/영어 지원)
- LSA(Latent Semantic Analysis) 기반 텍스트 요약
- Streamlit 기반의 직관적인 웹 인터페이스

## 설치 방법

1. 저장소를 클론합니다:
```bash
git clone https://github.com/avatar80/youtube_bot.git
cd youtube_bot
```

2. 필요한 패키지를 설치합니다:
```bash
pip install -r requirements.txt
```

3. NLTK 데이터를 다운로드합니다:
```python
python -c "import nltk; nltk.download('punkt')"
```

## 실행 방법

다음 명령어로 애플리케이션을 실행합니다:
```bash
streamlit run app.py
```

## 사용 방법

1. 브라우저에서 애플리케이션이 실행됩니다
2. YouTube 동영상 URL을 입력창에 붙여넣기 합니다
3. 자동으로 자막을 추출하고 내용을 요약합니다
4. 요약된 내용을 확인합니다

## 주의사항

- 자막이 비활성화된 동영상은 요약할 수 없습니다
- 한국어와 영어 자막만 지원됩니다
- 텍스트 요약은 LSA 알고리즘을 사용하며, 기본적으로 5개의 문장으로 요약됩니다