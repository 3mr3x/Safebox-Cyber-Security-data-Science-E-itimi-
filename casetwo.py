from pymongo import MongoClient



client = MongoClient('mongodb://localhost:27017')
db = client['flaskmongodb']
collection = db['Users']


result=collection.find()
for i in result:
    print(i)




#İsmi Ahmet olanları getir
result1=collection.find({"Name":"Ahmet"})
for i in result1:
    print(i)


#Users collectionında yaşı 20'den fazla olanları getiren sorgu
result2=collection.find(
    {
        "Age":{
            "$gt":20
        }
    }
)
for i in result2:
    print(i)



#Users collectionında yaşı 25'den fazla olanların description'ı 0 olacak.
result3=collection.update_many(
     {'Age':{"$gt":25}},
     {'$set':{'Description':0}}
)


#Users collectionında yaşı 45-48 yaş aralığında olan kişileri silen sorgu
result4=collection.delete_many(
    {
        "Age":{"$gte":45,"$lte":48}
    }
)
