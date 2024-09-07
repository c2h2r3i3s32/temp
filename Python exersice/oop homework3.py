class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.products = []
        self.reviews = []

    def sell_product(self, name, description, price):
        product = Product(name, description, self, price)
        self.products.append(product)
        return product

    def buy_product(self, product):
        product.available = False

    def write_review(self, description, product):
        review = Review(description, self, product)
        self.reviews.append(review)
        product.reviews.append(review)
        return review

    def __repr__(self):
        return f"User({self.id}, {self.name})"

class Product:
    def __init__(self, name, description, seller, price):
        self.name = name
        self.description = description
        self.seller = seller
        self.reviews = []
        self.price = price
        self.available = True

    def __repr__(self):
        return f"Product({self.name}, {self.description}, {self.price}, Available: {self.available})"

class Review:
    def __init__(self, description, user, product):
        self.description = description
        self.user = user
        self.product = product

    def __repr__(self):
        return f"Review({self.description}, {self.user.name}, {self.product.name})"

brianna = User(1, 'Brianna')
mary = User(2, 'Mary')

keyboard = brianna.sell_product('Keyboard', 'A nice mechanical keyboard', 100)
print(keyboard.available)  # => True
mary.buy_product(keyboard)w
print(keyboard.available)  # => False
review = mary.write_review('This is the best keyboard ever!', keyboard)
print(review in mary.reviews)  # => True
print(review in keyboard.reviews)  # => True




