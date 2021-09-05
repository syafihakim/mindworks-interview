import graphene
import json
from schema import *
from graphene.types.objecttype import ObjectType

schema = graphene.Schema(query=Query)

# Purpose : Execute the query built from buildPageQuery()
# Return : The function returns the list of posts on current page - default page is 1
def paginate(currentPage=1) :
    query = buildPageQuery(currentPage)
    result = schema.execute(query)
    return result.data

# Purpose : The query is used to GET relevant post information for pagination
# Return : Return the info of Posts that are in current page only
def buildPageQuery(currentPage=1) :
    f_1 =  (f"currentPage : {currentPage}")
    fields = (f'''
    {{
        simplePostList ({f_1}) {{
            id
            title
        }}
    }}''')
    return fields
