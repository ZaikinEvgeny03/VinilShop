from app import app, db
from app.models.user import User
from werkzeug.security import generate_password_hash

with app.app_context():
    username = 'admin'
    password = 'admin123'
    hashed_password = generate_password_hash(password)

    if User.query.filter_by(username=username).first():
        print('Пользователь уже существует.')
    else:
        new_admin = User(username=username, password_hash=hashed_password)
        db.session.add(new_admin)
        db.session.commit()
        print('Админ успешно создан.')
