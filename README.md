# 🎥 Video Analysis Worker

**Kafka 기반 비디오 분석 및 요약 서비스**

이 서비스는 Kafka 메시지를 소비하여 비디오 URL을 수신하고, 비디오 프레임 추출, VLM(Vision Language Model)을 이용한 장면 설명, 그리고 LLM을 이용한 최종 요약을 수행하는 백그라운드 워커입니다.
추가적으로 요약된 내용을 바탕으로 AI 썸네일과 음성 브리핑(TTS)을 생성하여 제공합니다.

---

## ✨ 주요 기능

- **📨 Kafka Consumer**: `video.analysis.request` 토픽을 구독하여 분석 요청을 비동기로 처리합니다.
- **🎞️ 비디오 처리**: `yt-dlp`와 `OpenCV`를 사용하여 YouTube 및 기타 비디오 소스에서 키프레임을 추출합니다.
- **👁️ AI 비전 분석**: `Ollama` (minicpm-v:8b)를 사용하여 추출된 프레임의 내용을 텍스트로 설명합니다.
- **📝 AI 요약**: `Ollama` (exaone3.5)를 사용하여 장면 설명들을 종합하여 비디오 내용을 요약합니다.
- **🎨 AI 썸네일 생성**: 요약 내용을 바탕으로 프롬프트를 생성하고, `Pollinations.ai` (Flux/Turbo 모델)를 통해 고품질 썸네일 이미지를 생성합니다.
- **🗣️ AI 음성 브리핑**: `edge-tts`를 사용하여 요약된 텍스트를 자연스러운 한국어 음성(MP3)으로 변환합니다.
- **💾 스토리지 통합**: 생성된 썸네일과 오디오 파일을 MinIO(S3 호환 스토리지)에 자동으로 업로드합니다.
- **🔔 알림 시스템**: 분석 완료 시 Kafka를 통해 알림 이벤트를 발행합니다.
- **📊 관측성(Observability)**: `OpenTelemetry`와 `Loki`를 연동하여 분산 트레이싱 및 로그 모니터링을 지원합니다.

---

## 🛠️ 기술 스택

- **Language**: Python 3.12+
- **Framework**: Asyncio, AIOKafka
- **Video Processing**: OpenCV, yt-dlp
- **AI/ML Integration**: Ollama (MiniCPM-V, Exaone 3.5), Pollinations.ai
- **TTS**: edge-tts
- **Database**: PostgreSQL (SQLAlchemy)
- **Storage**: MinIO (boto3)
- **Observability**: OpenTelemetry, Loki
- **Containerization**: Docker, Docker Compose

---

## 📋 필수 요구 사항

이 서비스를 실행하기 위해서는 다음 인프라가 필요합니다:

- **Kafka**: 메시지 브로커
- **PostgreSQL**: 데이터베이스
- **MinIO**: 객체 스토리지 (썸네일/오디오 저장용)
- **Ollama**: AI 모델 서빙 (minicpm-v:8b, exaone3.5 모델 필요)
- **Loki & Prometheus**: 로그 및 메트릭 수집 (선택 사항)

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
- `MINIO_ENDPOINT`: MinIO 서버 주소
- `MINIO_ACCESS_KEY`: MinIO 액세스 키
- `MINIO_SECRET_KEY`: MinIO 시크릿 키
- `MINIO_BUCKET_NAME`: 저장소 버킷 이름
- `LOKI_URL`: Loki 로그 수집 주소

### 2. 로컬 실행

uv를 사용하여 의존성을 설치하고 워커를 실행합니다.

```bash
# 의존성 설치
uv sync

# 워커 실행
uv run python src/main.py
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
uv run pytest

# 커버리지 확인
uv run pytest --cov=src
```

---

## 📂 프로젝트 구조

```
.
├── src/
│   ├── core/               # 설정, 로거, DB, 스토리지, 메시지 브로커 등 핵심 모듈
│   ├── models/             # DB 모델 정의
│   ├── services/           # 비즈니스 로직 (비디오 분석, AI 호출, TTS, 썸네일)
│   └── main.py             # 워커 진입점 (Kafka Consumer)
├── tests/                  # 단위 및 통합 테스트
├── Dockerfile              # Docker 이미지 정의
├── docker-compose.yml      # Docker Compose 구성
└── pyproject.toml          # Poetry 및 의존성 설정
```
