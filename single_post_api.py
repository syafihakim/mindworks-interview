import graphene
import json
from schema import *
from graphene.types.objecttype import ObjectType

schema = graphene.Schema(query=Query)

# Purpose : Execute the query built from buildSinglePostQuery()
# Return : The function returns a single post
def getSinglePost(id) :
    query = buildSinglePostQuery(id)
    result = schema.execute(query)
    #print(result.data)
    return result.data

# Purpose : The query is used to display relevant post information
# Return : only 3 useful items for our use case
def buildSinglePostQuery(id) :
    fields = (f'''
    {{
        singlePost (id : {id}){{
            title
            body
            id
        }}
    }}''')
    return fields
