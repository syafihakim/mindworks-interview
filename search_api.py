import graphene
import json
from schema import *
from graphene.types.objecttype import ObjectType

schema = graphene.Schema(query=Query)

def startSearching(postId, id, email, name, body) :
    query = buildCommentQuery(postId, id, email, name, body)
    result = schema.execute(query)
    #print(result)
    print(query)
    return result.data

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

    # fields = f"query{{\nlistOfComments (postId: \"{postId}\"){{"
    # if(postId != "") : fields += "\npostId"
    # if(id != "") : id += "\nid"
    # if(name != "") : name += "\nname"
    # if(email != "") : email += "\nemail"
    # if(body != "") : body += "\nbody"
    # fields += "\n}\n}"
    return fields
