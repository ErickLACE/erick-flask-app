from flask import Flask, render_template, request, redirect, url_for
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) #name spaces
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/ericksg631/Desktop/flask/erick-flask-app/ejercicios/articles/articles.db'
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(200))


@app.route('/')
def home():
    article = Article.query.all()
    return render_template('articles.html', article = article)



@app.route('/create-articles', methods =['POST'])
def create():
    
    article = Article(title=request.form['title'], body=request.form['body'])
    db.session.add(article)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/delete-articles/<id>')
def delete(id):
    article = Article.query.filter_by(id = int(id)).delete()
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, port=7000, host='0.0.0.0' ) #   errors