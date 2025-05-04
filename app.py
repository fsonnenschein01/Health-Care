from flask import Flask, render_template, request

app = Flask(__name__)

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# Каталог товаров
@app.route('/catalog')
def catalog():
    return render_template('catalog.html')

# Карточка товара
@app.route('/product/<int:product_id>')
def product(product_id):
    return render_template('product.html', product_id=product_id)

# Корзина
@app.route('/cart')
def cart():
    return render_template('cart.html')

# Оформление заказа
@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

# Личный кабинет
@app.route('/account')
def account():
    return render_template('account.html')

# Онлайн-консультант
@app.route('/consultant')
def consultant():
    return render_template('consultant.html')

# Поиск товаров
@app.route('/search')
def search():
    query = request.args.get('query', '')
    # Здесь будет логика поиска с использованием регулярных выражений
    return render_template('search_results.html', query=query)

if __name__ == '__main__':
    app.run(debug=True)
