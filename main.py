from flask import Flask, request, redirect, render_template,url_for,flash
import random
import string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key='test'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/'your_path'/test.db'
db = SQLAlchemy(app)
app.app_context().push()

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(50), nullable=False)
    desc=db.Column(db.String(200), nullable=False)
    short=db.Column(db.String(50), nullable=False)
    long=db.Column(db.String(800), nullable=False)
    def __init__(self,title,desc,short,long):
        self.title=title
        self.desc=desc
        self.short=short
        self.long=long

class shortner():
    def __init__(self):
        self.charas = string.ascii_letters + string.digits
    def shorten(self):
        while True:
            short_code=self.generate_short_code()
            if not self.shorten_exist(short_code):
                return short_code
    def shorten_exist(self,short_code):
        search=URL.query.filter(URL.short==short_code).all()
        return search

    def generate_short_code(self, length=6):
        return ''.join(random.choice(self.charas) for _ in range(length))
    
@app.route('/')
def index():
    """user = URL(title="video2",desc='something very long2hdhfjkdshakfhakdhfakhkjfhaskdhdfakhdsakhfadsk',short="link short2", long='link long2')
    db.session.add(user)
    db.session.commit()"""
    links = URL.query.all()
    return render_template("index.html",links=links)

@app.route('/insert',methods=['POST'])
def insert():
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        longLink=request.form['longLink']
        shortLink=shortner().shorten()

        url=URL(title,desc,shortLink,longLink)
        db.session.add(url)
        db.session.commit()

        flash("Link successfully created")

        return redirect(url_for("index"))
    
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    link = URL.query.get_or_404(id)
    
    db.session.delete(link)
    db.session.commit()
    
    flash("Link successfully deleted")
    
    return redirect(url_for("index"))

@app.route('/update/<int:id>',methods=['GET', 'POST'])
def update(id):
    link = URL.query.get_or_404(id)
    
    if request.method == 'POST':
        link.title = request.form['title']
        link.desc = request.form['desc']
        link.long = request.form['longLink']
        
        db.session.commit()
        flash("Link successfully updated")
        
        return redirect(url_for("index"))
    return render_template("update.html", link=link)


@app.route('/<short_code>')
def redirect_to_long(short_code):
    url = URL.query.filter_by(short=short_code).first()
    if url:
        return redirect(url.long)
    else:
        return f'Short Link does not exist or you forgot to add the http:// or https://'
    
@app.route('/display')
def display_links():
    links = URL.query.all()
    for link in links:
        print(f"Title: {link.title}")
        print(f"Description: {link.desc}")
        print(f"Short Link: {link.short}")
        print(f"Long Link: {link.long}")
        print("----------------------")
    return "Data printed in the console"
if __name__ == '__main__':
    #db.create_all()
    app.run(debug=True)
