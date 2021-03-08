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
    return "<h1>The Ultimate Tag Manager</h1><h1>Hello World!</h1><img src=\"%s\" style=\"width:300px\"><div>%s</div><div>%s</div>" % (app.config['config']['awesome_image'],form_html, tags_html)

@app.route('/tags', methods=['POST'])
def add_tag():
    Tag.get_or_create(
      name=request.form['tag-name'],
      defaults={'created_at': datetime.now(), 'updated_at': datetime.now()})

    return redirect('/')
