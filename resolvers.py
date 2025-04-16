from ariadne import QueryType

query = QueryType()

@query.field("hello")
def resolver_hello(_,info):
    return "Hello from the resolver file"

# allUsers resolver for MongoDB
@query.field("allUsers")
def resolve_all_users(_, info):
    db = info.context["db"]
    users = list(db.find({}, {"_id": 0}))  # skip _id from response
    return users

@query.field("getUserByName")
def resolver_getUserByName(_,info,name):
    db = info.context['db']
    user = db.find_one({"name": name},{"_id":0})
    print(user)
    if not user:
        return None
    return user