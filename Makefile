all:
	FLASK_APP=supabase_raw FLASK_DEBUG=1 flask run

deploy:
	fly deploy

