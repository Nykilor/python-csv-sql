start-db:
	docker compose up -d

run:
	streamlit run ./main.py

freeze:
	pip3 freeze > requirements.txt