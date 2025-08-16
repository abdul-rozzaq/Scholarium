HOST := 0.0.0.0
PORT := 8000

run:
	python src/manage.py runserver $(HOST):$(PORT)
