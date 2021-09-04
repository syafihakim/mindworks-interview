from flask import Flask, render_template, request
import schema
import search_api
app = Flask(__name__)  

@app.route('/')  
def index():  
    filteredComments = []
    return render_template('index.html', filteredComments = filteredComments)
  
@app.route('/', methods=['POST'])
def my_form_post():
    postId = request.form['postId']
    id = request.form['id']
    email = request.form['email']
    name = request.form['name']
    body = request.form['body']
    filteredComments = search_api.startSearching(postId, id, email, name, body)
    return render_template('index.html', filteredComments = filteredComments)

if __name__ =="__main__":  
    app.run(debug = True)  