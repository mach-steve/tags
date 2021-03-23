from flask import request, redirect, render_template, g
from datetime import datetime
from app import app, cfg
from tag import Tag

@app.route('/', methods=['GET'])
def show_tags():
    tags = Tag.select()
    tags_html = '\n'.join(list(map(lambda x: "<a href=\"/tags/%s\">%s</a><br>" % (x.name, x.name), tags)))
    form_html = "<form action=\"/tags\" method=\"POST\"><label>Enter a tag: </label><input name=\"tag-name\"></form>"
    #embed()
    return "<div><h1>The Ultimate Tag Manager</h1><h1>Tags</h1><a href='/about/'>ABOUT</a></div><img src=\"%s\" style=\"width:300px\"><div>%s</div><div>%s</div>" % (cfg['awesome_image'],tags_html, form_html)

@app.route('/tags', methods=['POST'])
def add_tag():
    Tag.get_or_create(
      name=request.form['tag-name'],
      defaults={'created_at': datetime.now(), 'updated_at': datetime.now()})

    return redirect('/')

@app.route('/about/', methods=['GET'])
def about_page():
    return "<nav style='background-color: brown; width: 100%'> <a href='/'>GO HOME</a> </nav>  <div> <h1> This is a page to manage tags </h1> </div>"

# GET is not the recommended way to implement DELETE, but oh well...
@app.route('/tags/<tag>', methods=['GET'])
def remove_tag(tag):
    tag_to_remove = Tag.get(Tag.name == tag).delete_instance()

    return redirect('/')
