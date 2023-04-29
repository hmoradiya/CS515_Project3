from flask import Flask
from app.extensions import db
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize Flask extensions here
    db.init_app(app)
    
    # Register blueprints here
    from app.posts import bp as posts_bp
    from app.users import bp as users_bp
    app.register_blueprint(posts_bp, url_prefix='/post')
    app.register_blueprint(users_bp, url_prefix='/user')

    return app