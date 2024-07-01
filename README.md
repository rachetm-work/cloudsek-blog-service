# cloudsek-blog-service

CloudSEK Assignment

**Author:** Rachet M

### For deployment on docker -

- Navigate to `/deployment/docker/` directory from project root
- Run `bash deploy.sh`

### NOTE: I have not worked with Kubernetes, so I have not tested deployment on it.

### cURL commands -

- Insertion of blog entries

```
curl -X POST "http://localhost:8000/api/v1/blog/submit" -H "Content-Type: application/json" -d '{"title": "My First Blog", "content": "This is the content of my first blog.", "user_id": "1"}'

curl -X POST "http://localhost:8000/api/v1/blog/submit" -H "Content-Type: application/json" -d '{"title": "My Second Blog", "content": "This is the content of my second blog.", "user_id": "1"}'
```

- Search for blog entries

```
curl -X GET "http://localhost:8000/api/v1/blog/search?search_term=first"

curl -X GET "http://localhost:8000/api/v1/blog/search?search_term=content"
```
