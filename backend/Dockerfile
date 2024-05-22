# 基於 Python 的官方映像
FROM python:3.10.4

# 設定工作目錄
WORKDIR /app

# 複製依賴文件並安裝依賴
COPY requirements.txt .
RUN pip install setuptools wheel
RUN pip install cmake
RUN pip install --no-cache-dir -r requirements.txt

# 複製後端代碼
COPY . .

# 開放連接埠
EXPOSE 8000

# 啟動 FastAPI 應用
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
