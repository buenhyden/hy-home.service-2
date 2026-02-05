# ==============================================================================
# Dockerfile Multi-Stack Template
#
# 목적 (Purpose):
# - 다양한 Tech Stack에 맞는 Docker 빌드 환경 제공
# - Multi-stage build를 통한 이미지 최적화
#
# 사용법 (Usage):
# - 사용하는 스택의 주석을 해제하고 나머지는 삭제/주석 처리하세요.
# - (Uncomment the stack you use and delete/comment out others.)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Python (FastAPI / Django) - uv 사용 (Recommended)
# ------------------------------------------------------------------------------
# FROM python:3.13-slim-bookworm AS python-base
# ENV PYTHONUNBUFFERED=1 \
#     PYTHONDONTWRITEBYTECODE=1 \
#     PIP_NO_CACHE_DIR=off \
#     UV_SYSTEM_PYTHON=1
#
# WORKDIR /app
#
# # Install uv
# COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
#
# # Install dependencies
# COPY requirements.txt .
# RUN uv pip install --no-cache-dir -r requirements.txt
#
# # Copy code
# COPY . .
#
# # Run
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


# ------------------------------------------------------------------------------
# 2. Node.js (NestJS / Express / Next.js)
# ------------------------------------------------------------------------------
# FROM node:23-alpine AS node-base
# WORKDIR /app
#
# # Install dependencies
# COPY package*.json ./
# RUN npm ci
#
# # Copy code
# COPY . .
#
# # Build (if needed)
# # RUN npm run build
#
# # Run
# CMD ["npm", "run", "start:prod"]


# ------------------------------------------------------------------------------
# 3. Java (Spring Boot) - Eclipse Temurin
# ------------------------------------------------------------------------------
# FROM eclipse-temurin:17-jdk-alpine AS java-build
# WORKDIR /app
# COPY . .
# RUN ./gradlew build -x test
#
# FROM eclipse-temurin:17-jre-alpine
# WORKDIR /app
# COPY --from=java-build /app/build/libs/*.jar app.jar
# CMD ["java", "-jar", "app.jar"]


# ------------------------------------------------------------------------------
# 4. Go (Gin / Fiber)
# ------------------------------------------------------------------------------
# FROM golang:1.21-alpine AS go-build
# WORKDIR /app
# COPY go.mod go.sum ./
# RUN go mod download
# COPY . .
# RUN go build -o main .
#
# FROM alpine:latest
# WORKDIR /app
# COPY --from=go-build /app/main .
# CMD ["./main"]
