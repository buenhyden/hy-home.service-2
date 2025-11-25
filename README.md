# 🎥 Video Analysis Worker

**Kafka 기반 비디오 분석 및 요약 서비스**

이 서비스는 Kafka 메시지를 소비하여 비디오 URL을 수신하고, 비디오 프레임 추출, VLM(Vision Language Model)을 이용한 장면 설명, 그리고 LLM을 이용한 최종 요약을 수행하는 백그라운드 워커입니다.

---

## ✨ 주요 기능

- **📨 Kafka Consumer**: `video.analysis.request` 토픽을 구독하여 분석 요청을 비동기로 처리합니다.
- **🎞️ 비디오 처리**: `yt-dlp`와 `OpenCV`를 사용하여 YouTube 및 기타 비디오 소스에서 키프레임을 추출합니다.
- **👁️ AI 비전 분석**: `Ollama` (minicpm-v:8b)를 사용하여 추출된 프레임의 내용을 텍스트로 설명합니다.
- **📝 AI 요약**: `Ollama` (exaone3.5)를 사용하여 장면 설명들을 종합하여 비디오 내용을 요약합니다.
- **💾 상태 관리**: 분석 진행 상황(processing, completed, failed)과 결과를 데이터베이스에 저장합니다.

---

## 🛠️ 기술 스택

- **Language**: Python 3.12+
- **Framework**: Asyncio, AIOKafka
- **Video Processing**: OpenCV, yt-dlp
- **AI/ML Integration**: Ollama (MiniCPM-V, Exaone 3.5)
- **Database**: PostgreSQL (SQLAlchemy)
- **Containerization**: Docker, Docker Compose

---

## 📋 필수 요구 사항

이 서비스를 실행하기 위해서는 다음 인프라가 필요합니다:

- **Kafka**: 메시지 브로커
- **PostgreSQL**: 데이터베이스
- **Ollama**: AI 모델 서빙 (minicpm-v:8b, exaone3.5 모델 필요)

---

## 🚀 설치 및 실행

### 1. 환경 변수 설정

`.env.example` 파일을 복사하여 `.env` 파일을 생성하고 설정을 입력합니다.

```bash
cp .env.example .env
```

**주요 환경 변수:**

- `KAFKA_BROKERS`: Kafka 브로커 주소 (예: `localhost:9092`)
- `KAFKA_TOPIC_ANALYSIS`: 분석 요청 토픽 (기본값: `video.analysis.request`)
- `OLLAMA_URL`: Ollama 서버 주소 (예: `http://localhost:11434`)
- `DATABASE_URL`: PostgreSQL 연결 문자열

### 2. 로컬 실행

Poetry를 사용하여 의존성을 설치하고 워커를 실행합니다.

```bash
# 의존성 설치
poetry install

# 워커 실행
poetry run python src/main.py
```

### 3. Docker 실행

```bash
docker-compose up --build
```

---

## 🧪 테스트

단위 테스트를 실행하여 로직을 검증할 수 있습니다.

```bash
# 테스트 실행
pytest

# 커버리지 확인
pytest --cov=src
```

---

## 📂 프로젝트 구조

```
.
├── src/
│   ├── core/               # 설정, 로거, DB 연결 등 핵심 모듈
│   ├── models/             # DB 모델 정의
│   ├── services/           # 비즈니스 로직 (비디오 분석, AI 호출)
│   └── main.py             # 워커 진입점 (Kafka Consumer)
├── tests/                  # 단위 및 통합 테스트
├── Dockerfile              # Docker 이미지 정의
├── docker-compose.yml      # Docker Compose 구성
└── pyproject.toml          # Poetry 및 의존성 설정
```
