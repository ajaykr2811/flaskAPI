from ariadne import QueryType, MutationType

query = QueryType()
mutation = MutationType()

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

@mutation.field("updateEmail")
def resolver_updateEmail(_,info,name, email):
    db = info.context['db']
    update = db.update_one(
        {"name":name},
        {"$set":{"email":email}}
    )
    if update.matched_count == 0:
        #raise GraphQLError(f"User '{name}' not found!")
        return {
            "success": False,
            "message": f"User {name} is not found !"
        }
    return {
        "success": True,
        "message": f"email {email} is updated for {name}"
    }
    