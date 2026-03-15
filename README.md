# AI Log Analyzer

AI-powered debugging assistant that analyzes application logs and suggests root causes and fixes using LLMs.

## Features

- Upload log files
- AI-powered root cause detection
- Suggested fixes for common errors
- FastAPI backend + React frontend

## Tech Stack

- Python
- FastAPI
- React
- OpenAI / Gemini API
- Docker

## Architecture

User → React UI → FastAPI API → LLM → Analysis Result

## Run Backend

cd backend
uvicorn main:app --reload

## Run Frontend

cd frontend
npm start