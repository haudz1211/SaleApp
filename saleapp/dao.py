from saleapp import app
from models import *


def load_categories():
    return Category.query.all()


def load_products(q=None, cate_id=None, page = None):
    query = Product.query
    if q:
        query = query.filter(Product.name.contains(q))

    if cate_id:
        query = query.filter(Product.category_id.__eq__(int(cate_id)))

    if page:
        page_size = app.config["PAGE_SIZE"]
        start = (       int(page - 1)) * page_size
        query = query.slice(start, start+page_size)

    return query


def load_product_by_id(id):
    return Product.query.get(id)


if __name__ == "__main__":
    print(load_products())
