import sqlite3 as sqlite
from flask import Flask, render_template, request, url_for, flash, redirect

#function to create database connection and return it
def get_db_connection():
    db_connection = sqlite.connect('database.db')
    db_connection.row_factory = sqlite.Row
    return db_connection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'stephansnewblogireallyhopethishitworks'
#main blog page
@app.route("/")
def index():
    #open a db connection called blog_db_connection
    blog_db_connection = get_db_connection()
    #sql query to select all posts from the db
    posts = blog_db_connection.execute('SELECT * FROM posts').fetchall()
    #close the db connection, return the posts as outline in the index.html file
    blog_db_connection.close()
    return render_template('index.html', posts=posts )

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required')
        else:
            blog_db_connection = get_db_connection()
            blog_db_connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                (title, content))
            blog_db_connection.commit()
            blog_db_connection.close()
            return redirect(url_for('index'))

    return render_template('create.html')

"""
#all of the html testing behind this url
@app.route("/blog_testing")
def blog_testing():
    blog_db_connection = get_db_connection()
    posts = blog_db_connection.execute('SELECT * FROM posts').fetchall()
    blog_db_connection.close()
    return render_template('index.html', posts=posts )
"""
