from flask import request, redirect
from datetime import datetime
from app import app
from tag import Tag

@app.route('/', methods=['GET'])
def show_tags():
    tags = Tag.select()
    tags_html = '\n'.join(list(map(lambda x: x.name + "<br>", tags)))
    form_html = "<form action=\"/tags\" method=\"POST\"><label>Enter a tag: </label><input name=\"tag-name\"></form>"
    #embed()
    return "<h1>The Ultimate Tag Manager</h1><a href=\"/\">Home</a> <a href=\"/about\">About</a><h1>Hello World!</h1><img src=\"%s\" style=\"width:300px\"><div>%s</div><div>%s</div>" % (app.config['config']['awesome_image'],tags_html, form_html)

@app.route('/about', methods=['GET'])
def about():
    return '<h1>The Ultimate Tag Manager</h1><a href=\"/\">Home</a> <a href=\"/about\">About</a><h1>A Uniquely World-Changing Super-Proprietary Way of Managing Tags</h1><p>This is the only website ever designed that has at least one of the properties common to every other website ever designed.</p><p>A highly respected source has said, "I\'d rather use this site than use one of the best sites in the world!"'

@app.route('/tags', methods=['POST'])
def add_tag():
    Tag.get_or_create(
      name=request.form['tag-name'],
      defaults={'created_at': datetime.now(), 'updated_at': datetime.now()})

    return redirect('/')
