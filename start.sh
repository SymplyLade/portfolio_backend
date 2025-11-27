
#!/bin/bash
echo "Starting FastAPI..."
uvicorn main:app --reload --host 127.0.0.1 --port 8000
