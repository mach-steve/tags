from flask import request, redirect
from datetime import datetime
from app import app
from tag import Tag

delete_js = '''
<script type="text/javascript" src="static/js/lib/jquery-3.5.1.js"></script>
<script type="text/javascript">
$('.delete_link').on('click', function(e) {
  var url = "http://localhost:5000" + $(this).attr('href');
  var xhr = new XMLHttpRequest();
  xhr.open("DELETE", url, true);
  xhr.send(null);
  window.location.href='/';  // Redirect
  return false;
});
</script>
'''

@app.route('/', methods=['GET'])
def show_tags():
    tags = Tag.select()
    tags_html = '\n'.join(list(map(lambda x: "<a class=\"delete_link\" href=\"/tags/%s\">%s</a><br>" % (x.name, x.name), tags)))
    form_html = "<form action=\"/tags\" method=\"POST\"><label>Enter a tag: </label><input name=\"tag-name\"></form>"
    #embed()
    return "<h1>The Ultimate Tag Manager</h1><h1>Hello World!</h1><img src=\"%s\" style=\"width:300px\"><div>%s</div><div>%s</div>%s" % (app.config['config']['awesome_image'],tags_html, form_html,delete_js)

@app.route('/tags', methods=['POST'])
def add_tag():
    Tag.get_or_create(
      name=request.form['tag-name'],
      defaults={'created_at': datetime.now(), 'updated_at': datetime.now()})

    return redirect('/')

@app.route('/tags/<tag>', methods=['DELETE'])
def remove_tag(tag):
    tag_to_remove = Tag.get(Tag.name == tag).delete_instance()

    return '', 204 # No need to return any content, since Javascript will redirect anyway
