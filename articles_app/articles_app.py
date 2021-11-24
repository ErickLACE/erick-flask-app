from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:cbi2132015379@localhost/articles'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
ma = Marshmallow(app)

class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70))
    body = db.Column(db.String(100))

    def __init__(self, title, body):
        self.title = title
        self.body = body


db.create_all()

class ArticleSechema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'body')

article_schema = ArticleSechema()
articles_schema = ArticleSechema(many=True)

# Create endpoints

@app.route('/articles', methods=['GET'])
def get_Articles():
    all_articles = Articles.query.all()
    latest_10 = all_articles[-10:][::-1]
    result = articles_schema.dump(latest_10)
    return jsonify(result)



@app.route('/articles', methods=['POST'])
def create_article():
    
    title = request.json['title'],
    body = request.json['body']

    new_article = Articles(title, body)
    db.session.add(new_article)
    db.session.commit()

    return article_schema.jsonify(new_article)


@app.route('/articles/<id>', methods=['GET'])
def get_article(id):
    article = Articles.query.get(id)
    return article_schema.jsonify(article)



@app.route('/articles/<id>', methods=['PUT'])
def update_article(id):

    article = Articles.query.get(id)

    title = request.json['title'],
    body = request.json['body']

    article.title = title
    article.body = body

    db.session.commit()

    return article_schema.jsonify(article)


@app.route('/articles/<id>', methods=['DELETE'])
def delete_article(id):
    article = Articles.query.get(id)
    db.session.delete(article)
    db.session.commit

    return article_schema.jsonify(article)


if __name__ == '__main__':
    app.run(debug=True, port = 7000)