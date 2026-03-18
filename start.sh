#!/bin/bash
set -e
echo "Starting AI-Powered Mental Health Chatbot..."
uvicorn app:app --host 0.0.0.0 --port 9112 --workers 1
