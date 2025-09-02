# flask-backend/endpoint_test.md


curl http://127.0.0.1:5000/helloworld

curl http://127.0.0.1:5000/

curl -X POST http://127.0.0.1:5000/todo/ \
  -H "Content-Type: application/json" \
  -d '{"title": "New task from curl"}'

curl http://127.0.0.1:5000/todo/

curl http://127.0.0.1:5000/todo/1

curl -X PUT http://127.0.0.1:5000/todo/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated task title"}'

curl -X DELETE http://127.0.0.1:5000/todo/1
