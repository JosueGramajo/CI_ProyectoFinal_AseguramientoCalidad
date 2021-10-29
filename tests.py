from hello import app
with app.test_client() as c:
	response = c.get('/')
	assert response.data == b'Hola Mundo!, Este es el ambiente de QA'
	assert response.status_code == 200