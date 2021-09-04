import graphene
import json
from datetime import datetime
from graphene.types.objecttype import ObjectType

COMMENTS = json.load(open('comments.json', ))

# =================== Objects ===================
class Comment(ObjectType):
    postId = graphene.ID()
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()
    body = graphene.String()

# =================== Query Templates ===================

class Query(ObjectType):
    array = graphene.List(Comment)

    def resolve_array(root, info):
        return COMMENTS

# =================== Graphql Query ===================
query_graphql = '''
query myquery{
    array {
        name
        id
    }
}
'''

# print(schema)
schema = graphene.Schema(query=Query)
result = schema.execute(query_graphql)
print(json.dumps(result.data, indent=3))
