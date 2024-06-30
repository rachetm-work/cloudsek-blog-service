# cloudsek-blog-service

CloudSEK Assignment

### cURL commands -

- Insertion

```
curl -X POST "http://localhost:8000/api/v1/blog/submit" -H "Content-Type: application/json" -d '{"title": "My First Blog", "content": "This is the content of my first blog.", "user_id": "1"}'

curl -X POST "http://localhost:8000/api/v1/blog/submit" -H "Content-Type: application/json" -d '{"title": "My Second Blog", "content": "This is the content of my second blog.", "user_id": "1"}'
```

- Search

```
curl -X GET "http://localhost:8000/api/v1/blog/search?search_term=first"
```
