from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
# Where the database stored
db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'ET.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db = SQLAlchemy(app)
########
with app.app_context():
    db.create_all()
    print("Tables created successfully")

#######

class Todo(db.Model):
    __tablename__ = 'Categories'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    data_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Task {self.id}>'

@app.route('/',methods = ['POST','GET'])

def index():
    if request.method == "POST":
        task_content = request.form['content']
        new_category = Todo(content = task_content)

        try:
            db.session.add(new_category)
            db.session.commit()
            return redirect('/')
        
        except:
            return 'There was an issue adding your category'

    else:
        # Querying our database and ordering all of them
        categories = Todo.query.order_by(Todo.data_created).all()
        return render_template('index.html', tasks = categories)

    

if __name__ == "__main__":
    app.run(debug=True)