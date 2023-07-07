from flask import Flask, jsonify, request
from pymongo import MongoClient

# Flask uygulamasını oluşturma
app = Flask(__name__)

# MongoDB'ye bağlan
client = MongoClient('mongodb://localhost:27017')
db = client['flaskmongodb']
collection = db['Users']


# Veritabanı ve koleksiyon seçimi
db = client.flaskmongodb
collection = db.Users

# Endpoint - Users Collection'a kullanıcı ekleme
@app.route('/adduser', methods=['POST'])
def add_user():
    user = request.get_json()
    collection.insert_one(user)
    return jsonify({"message": "Kullanıcı başarıyla eklendi."})

# Endpoint - Users Collectionında yaşı 25'ten büyük olanları getirme
@app.route('/25', methods=['GET'])
def get_users_above_25():
    users = list(collection.find({"Age": {"$gt": 25}}))
    return jsonify(users)

# Endpoint - Users Collectionındaki tüm kullanıcıları getirme
@app.route('/', methods=['GET'])
def get_all_users():
    users = list(collection.find())
    return jsonify(users)

# Endpoint - Users Collectionındaki verilen id'ye sahip kullanıcıyı silme
@app.route('/deleteuser', methods=['POST', 'DELETE'])
def delete_user():
    user_id = request.args.get('id')
    collection.delete_one({"_id": ObjectId(user_id)})
    return jsonify({"message": "Kullanıcı başarıyla silindi."})

# Flask uygulamasını çalıştırma
if __name__ == '__main__':
    app.run()
