# EL-RFA-Predict
The system to predict prognosis of hcc patient recieving RFA

# How to run?
- url setting: 
    - `frontend/src/boot/axios.js`
    - `axios.create({ baseURL: 'YOUR_URL/api' })`
- use docker compose
    - `docker compose up -d`
- port: 8080

# Need to fix
- YOUR_URL as docker compose environment variable

# Structure
## Services
- backend
    - as RESTful API
    - run model inference
    - case and batch mode
    - python, fastapi
- frontend
    - as GUI(website)
    - upload form
    - upload excel
    - display case result
    - download batch result
    - nodejs, vue3, quasar2
- proxy
    - as router
    - `YOUR_URL` to frontend
    - `YOUR_URL/api` to backend
    - nginx
## Docker
- frontend, backend: using `Dockerfile` to build docker images
- `docker-compose-yml` integrates all services

# How to write git commit?
[IT邦幫忙: Git Commit Message 這樣寫會更好，替專案引入規範與範例](https://ithelp.ithome.com.tw/articles/10228738)