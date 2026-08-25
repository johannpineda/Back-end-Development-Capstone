# Back-End-Development-Songs
IBM capstone Songs microservice using Flask + MongoDB.

```bash
docker run -d --name mongo -p 27017:27017 mongo:7
pip install -r requirements.txt
python seed.py
python app.py
curl http://localhost:5000/health
curl http://localhost:5000/song
```
