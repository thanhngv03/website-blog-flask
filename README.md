# website-blog-flask

#chạy ứng dụng web:
flask --app run:create_app run
flask --app run:create_app --debug run(che do debug)
#chay moi truong ao
venv\Scripts\activate

#Tao db 
flask --app run:create_app shell
>>> from app import db 
>>> db.drop_all()
>>> db.create_all()
>>> exit()

#upgrade db
flask --app run:create_app db upgrade 