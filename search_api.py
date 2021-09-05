import graphene
import json
from schema import *
from graphene.types.objecttype import ObjectType

schema = graphene.Schema(query=Query)

# Purpose : Execute the query built from buildCommentQuery()
# Return : The function returns a list of filtered comments - can be any fields
def startSearching(postId="", id="", email="", name="", body="") :
    query = buildCommentQuery(postId, id, email, name, body)
    result = schema.execute(query)
    return result.data

# Purpose : Search comment with ANY match from ANY fields
# Return : Returns 
def buildCommentQuery(postId, id, email, name, body) :
    f_1 =  (f"postId : {postId}") if (postId != "") else ("")
    f_2 =  (f"id : {id}") if (id != "") else ("")
    f_3 =  (f"email : \"{email}\"") if (email != "") else ("")
    f_4 =  (f"name : \"{name}\"") if (name != "") else ("")
    f_5 =  (f"body : \"{body}\"") if (body != "") else ("")
    fields = (f'''
    {{
        listOfComments ({f_1}, {f_2}, {f_3}, {f_4}, {f_5}) {{
            postId
            id
            email
            name
            body   
        }}
    }}''')
    return fields
