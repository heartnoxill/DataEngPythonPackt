from elasticsearch import Elasticsearch
from faker import Faker

fake=Faker()
# es = Elasticsearch('127.0.0.1') #or pi {127.0.0.1}
# es = Elasticsearch("http://localhost:9200")
es = Elasticsearch(
    "http://localhost:9200",
    basic_auth=("elastic", "JNYfTy*sULK5IoberpYe"),
)

doc={"name": fake.name(),"street": fake.street_address(), "city": fake.city(),"zip":fake.zipcode()}

res=es.index(index="users",document=doc,request_timeout=30)
print(res)

# doc={"query":{"match":{"_id":"pDYlOHEBxMEH3Xr-2QPk"}}}
# res=es.search(index="users",body=doc,size=10)
# print(res)