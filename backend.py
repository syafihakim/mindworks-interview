'''
This python file communicates with the website's front end using FLASK,
contents for various pages are generated dynamically and automatically through this page
'''

from flask import Flask, render_template, request
import schema
import math
import search_api
import pagination_api
import single_post_api
app = Flask(__name__)  
totalPages = math.floor(len(pagination_api.POSTS)/10)

# This function is called if we are first time visiting the website
@app.route('/')  
def index():  
    postsOnCurrPage = pagination_api.paginate(1)
    return render_template('posts.html', postsOnCurrPage = postsOnCurrPage, totalPages = totalPages)

# This function is called if when we clicked the pagination buttons
@app.route('/<page_num>', methods=['POST', 'GET'])
def page(page_num):  
    postsOnCurrPage = pagination_api.paginate(page_num)
    return render_template('posts.html', postsOnCurrPage = postsOnCurrPage, totalPages = totalPages)

# This function is when any post is clicked
@app.route('/post/<post_id>', methods=['POST', 'GET'])
def single_post_page(post_id):  
    singlePost = single_post_api.getSinglePost(post_id)["singlePost"]
    print(singlePost)

    if request.method == 'POST':
        postId = request.form['postId']
        id = request.form['id']
        email = request.form['email']
        name = request.form['name']
        body = request.form['body']
        comments = search_api.startSearching(post_id, id, email, name, body)
    else:
        comments = search_api.startSearching(post_id)
    return render_template('post.html', currPost = singlePost, comments=comments)

if __name__ =="__main__":  
    app.run(debug = True)  