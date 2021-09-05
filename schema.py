import graphene
import json
import urllib
from graphene.types.objecttype import ObjectType

# Fetching from remote API endpoint
link = "https://jsonplaceholder.typicode.com/comments"
f = urllib.request.urlopen(link)
myfile = f.read().decode()
COMMENTS = json.loads(myfile)

# Fetching from remote API endpoint
link = "https://jsonplaceholder.typicode.com/posts"
f = urllib.request.urlopen(link)
myfile = f.read().decode()
POSTS = json.loads(myfile)
class Comment(ObjectType):
    postId = graphene.Int()
    id = graphene.Int()
    name = graphene.String()
    email = graphene.String()
    body = graphene.String()

class Post(ObjectType):
    id = graphene.Int()
    title = graphene.String()

class SinglePost(ObjectType):
    title = graphene.String()
    userId=graphene.Int()
    id=graphene.Int() 
    title=graphene.String()
    body=graphene.String()

class Query(ObjectType):

    simplePostList = graphene.List(Post, currentPage=graphene.Int())
    singlePost = graphene.Field(SinglePost, id=graphene.Int())
    listOfComments = graphene.List(Comment, postId=graphene.Int(), id = graphene.Int(), name = graphene.String(), email = graphene.String(), body = graphene.String())

    # Purpose : Fetches only related post based on postId
    # Return : A single Post from API endpoint
    def resolve_singlePost(root, info, id) :
        link = f"https://jsonplaceholder.typicode.com/posts/{id}"
        f = urllib.request.urlopen(link)
        myfile = f.read().decode()
        POST = json.loads(myfile)
        print(POST)
        return POST

    # Purpose : Keeping only the comment that are relevant (union-based searching)
    # Filter can be from any fields
    def resolve_listOfComments(root, info, postId=None, id=None, name=None, email=None, body=None):
        filteredComments = []
        for comment in COMMENTS:
            append = False
            if(postId and postId == comment["postId"]):
                if(id == None and name == None and email == None and body == None):
                    append = True
                if(id and id == comment["id"]):
                    append = True
                if(name and name in comment["name"]):
                    append = True
                if(email and email in comment["email"]):
                    append = True
                if(body != None and body in comment["body"]):
                    append = True
            if(append == True):
                filteredComments.append(comment)
        return filteredComments

    # Purpose : Paginates all posts by 10 posts per page
    # Return : List of posts on current item only
    def resolve_simplePostList(root, info, currentPage=1):
        simplePostList = POSTS[(currentPage-1)*10:10*currentPage]
        return simplePostList

