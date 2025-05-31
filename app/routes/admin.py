from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import generate_csrf
from app import db
from app.models.vinyl import Vinyl
import os
from werkzeug.utils import secure_filename

admin = Blueprint('admin', __name__)

@admin.route('/admin/add', methods=['GET', 'POST'])
def add_vinyl():
    if request.method == 'POST':
        title = request.form['title']
        artist_id = request.form['artist_id']
        genre_id = request.form['genre_id']
        year = request.form['year']
        price = request.form['price']
        on_sale = request.form.get('onSale') == 'on'

        # Работа с изображением
        image = request.files['cover']
        filename = secure_filename(image.filename)
        image_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'static', 'images', 'vinyls', filename)
        image.save(image_path)

        new_vinyl = Vinyl(
            title=title,
            artist_id=artist_id,
            genre_id=genre_id,
            year=year,
            price=price,
            cover_image=filename,
            onSale=1 if on_sale else 0
        )

        db.session.add(new_vinyl)
        db.session.commit()
        flash('Винил успешно добавлен!', 'success')
        return redirect(url_for('main.index'))

    return render_template('admin_add.html', csrf_token=generate_csrf())
