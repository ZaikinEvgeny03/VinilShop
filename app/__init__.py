from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
import os

# Инициализация Flask-приложения
app = Flask(__name__)

# Конфигурация
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join('app', 'static', 'images', 'vinyls')
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB

# Инициализация расширений
db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

# Регистрация расширений в app
db.init_app(app)
csrf.init_app(app)
login_manager.init_app(app)

# Импорты моделей и blueprint'ов — после инициализации расширений!
from app.models import user, vinyl
from app.routes.main import main as main_blueprint
from app.routes.admin import admin as admin_blueprint
from app.routes.auth import auth as auth_blueprint

# Регистрация blueprint'ов
app.register_blueprint(main_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(auth_blueprint)

# Регистрация user_loader
from app.models.user import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
