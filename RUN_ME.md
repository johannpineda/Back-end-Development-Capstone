# Run the complete capstone

## Local services
```bash
docker compose up --build -d
```
Seed MongoDB:
```bash
docker compose exec songs python seed.py
```
Open `http://localhost:8000`.

## Pictures evidence
```bash
cd Back-End-Development-Pictures
pytest -k 'test_health or test_count' -v
pytest -v
```

## Songs evidence
```bash
curl --request GET --url http://localhost:5002/health
curl --request GET --url http://localhost:5002/song
```
Get a song `_id` from the previous output and use it below:
```bash
curl --request GET --url http://localhost:5002/song/<ID>
curl --request PUT --url http://localhost:5002/song/<ID> --header 'Content-Type: application/json' --data '{"title":"Updated Song","artist":"The Example Band"}'
curl --request DELETE --url http://localhost:5002/song/<ID>
```

## Django migration evidence
```bash
cd Back-end-Development-Capstone
python manage.py migrate
```

Deployment commands must be run against your authenticated IBM Cloud/OpenShift/Kubernetes accounts because those outputs contain real resource names/routes.
