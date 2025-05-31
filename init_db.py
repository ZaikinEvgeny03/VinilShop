from app import app, db
from app import Artist, Genre, Vinyl, User, Order, OrderItem

with app.app_context():
    db.drop_all()
    db.create_all()

    # Примеры жанров
    rock = Genre(name="Rock")
    electronic = Genre(name="Electronic")
    jazz = Genre(name="Jazz")

    # Примеры исполнителей
    floyd = Artist(name="Pink Floyd", country="UK", description="Легендарная прог-рок группа.")
    daft = Artist(name="Daft Punk", country="France", description="Французский электронный дуэт.")

    # Примеры винилов
    v1 = Vinyl(
        title="The Dark Side of the Moon",
        artist_id=1,
        genre_id=1,
        year=1973,
        price=1499.0,
        cover_image="darkside.jpg",
        onSale=1
    )

    v2 = Vinyl(
        title="Random Access Memories",
        artist_id=2,
        genre_id=2,
        year=2013,
        price=1899.0,
        cover_image="ram.jpg",
        onSale=0
    )

    db.session.add_all([rock, electronic, jazz, floyd, daft, v1, v2])
    db.session.commit()

    print("✅ База данных создана и заполнена.")
