from sqlalchemy import Column, Integer, String, Float, ForeignKey, BOOLEAN
from sqlalchemy.orm import relationship

from saleapp import app, db


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    active = Column(BOOLEAN, default=True)
    image = Column(String(200), default='https://res.cloudinary.com/dgeyq5bpg/image/upload/v1729843473/zkac4egeyhm3yikfyxts.jpg')
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        c1 = Category(name="Mobile")
        c2 = Category(name="Tablet")
        c3 = Category(name="Laptop")
        db.session.add_all([c1, c2, c3])

        import json
        with open("data/products.json", encoding="utf-8") as f:
            products = json.load(f)
            for p in products:
                prod = Product(**p)
                db.session.add(prod)

        db.session.commit()