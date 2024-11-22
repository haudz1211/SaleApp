from flask import Flask, render_template, request
import dao

from saleapp import app


@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("category_id")
    page = request.args.get("page")
    products = dao.load_products(q, cate_id, page)
    return render_template("index.html", products=products)


@app.route("/products/<int:id>")
def product_details(id):
    product = dao.load_product_by_id(id)
    print(product)
    return render_template("product-details.html", product= product)


@app.context_processor
def common_attributes():
    return {
        "categories": dao.load_categories()
    }


@app.route("/login")
def login_my_user():
    return render_template("login.html")


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)

