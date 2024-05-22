# 基於 Node 的官方映像
FROM node:18

# 設定工作目錄
WORKDIR /app

# 複製 package.json 並安裝依賴
COPY package*.json ./
RUN yarn global add @quasar/cli

# 複製剩餘的前端代碼
COPY . .

# 構建應用
RUN yarn install
RUN quasar build

# 開放連接埠
EXPOSE 9000

# 啟動服務器
CMD ["quasar", "serve", "-p", "9000", "dist/spa"]
