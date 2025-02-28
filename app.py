from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client.get_default_database()
collection = db.sales

# 主页 - 显示所有商品
@app.route('/')
def home():
    products = list(collection.find())
    return render_template('home.html', products=products)

# 添加新商品
@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        item = request.form['item']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])

        # 插入到 MongoDB
        collection.insert_one({
            'item': item,
            'price': price,
            'quantity': quantity
        })
        flash('Product added successfully!')
        return redirect(url_for('home'))
    return render_template('add.html')

# 编辑商品
@app.route('/edit/<product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    from bson.objectid import ObjectId  # 导入 ObjectId 以正确查找 MongoDB ID
    product = collection.find_one({'_id': ObjectId(product_id)})
    if request.method == 'POST':
        item = request.form['item']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])

        # 更新 MongoDB
        collection.update_one({'_id': ObjectId(product_id)}, {'$set': {
            'item': item,
            'price': price,
            'quantity': quantity
        }})
        flash('Product updated successfully!')
        return redirect(url_for('home'))
    return render_template('edit.html', product=product)

# 删除商品
@app.route('/delete/<product_id>')
def delete_product(product_id):
    from bson.objectid import ObjectId
    collection.delete_one({'_id': ObjectId(product_id)})
    flash('Product deleted successfully!')
    return redirect(url_for('home'))

# 搜索商品
@app.route('/search', methods=['GET', 'POST'])
def search_product():
    if request.method == 'POST':
        query = request.form['query']
        products = list(collection.find({'item': {'$regex': query, '$options': 'i'}}))
        return render_template('home.html', products=products)
    return redirect(url_for('home'))

@app.route('/item/<product_id>')
def item_detail(product_id):
    from bson.objectid import ObjectId
    item = collection.find_one({"_id": ObjectId(product_id)})
    
    if item:
        return render_template('item_detail.html', item=item)
    else:
        return "Item not found", 404



if __name__ == '__main__':
    app.run(debug=True)  # ✅ 开启调试模式，便于开发时发现错误
