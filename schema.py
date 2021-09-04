import graphene
import json
import urllib
from graphene.types.objecttype import ObjectType

link = "https://jsonplaceholder.typicode.com/comments"
f = urllib.request.urlopen(link)
myfile = f.read().decode()
COMMENTS = json.loads(myfile)

class Comment(ObjectType):
    postId = graphene.Int()
    id = graphene.Int()
    name = graphene.String()
    email = graphene.String()
    body = graphene.String()

class Query(ObjectType):
    listOfComments = graphene.List(
        Comment, 
        postId=graphene.Int(),
        id = graphene.Int(),
        name = graphene.String(),
        email = graphene.String(),
        body = graphene.String())

    def resolve_listOfComments(root, info, postId=None, id=None, name=None, email=None, body=None):
        filteredComments = []
        for comment in COMMENTS:
            append = True
            if(postId and postId != comment["postId"]):
                append = False
            if(id and id != comment["id"]):
                append = False
            if(name and name not in comment["name"]):
                append = False
            if(email and email not in comment["email"]):
                append = False
            if(body != None and body not in comment["body"]):
                append = False
            if(append == True):
                filteredComments.append(comment)
        return filteredComments