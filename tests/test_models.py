def test_read_a_product(self):
    """It should Read a Product"""
    product = ProductFactory()
    product.id = None
    product.create()
    self.assertIsNotNone(product.id)
    found_product = Product.find(product.id)
    self.assertEqual(found_product.id, product.id)
    self.assertEqual(found_product.name, product.name)
    self.assertEqual(found_product.description, product.description)
    self.assertEqual(found_product.price, product.price)

def test_update_a_product(self):
    """It should Update a Product"""
    product = ProductFactory()
    product.id = None
    product.create()
    product.description = "testing"
    original_id = product.id
    product.update()
    self.assertEqual(product.id, original_id)
    self.assertEqual(product.description, "testing")
    products = Product.all()
    self.assertEqual(len(products), 1)
    self.assertEqual(products[0].id, original_id)
    self.assertEqual(products[0].description, "testing")

def test_delete_a_product(self):
    """It should Delete a Product"""
    product = ProductFactory()
    product.id = None
    product.create()
    self.assertIsNotNone(product.id)
    product.delete()
    products = Product.all()
    self.assertEqual(len(products), 0)

def test_list_products(self):
    """It should List Products"""
    products = [ProductFactory() for _ in range(10)]
    for product in products:
        product.id = None
        product.create()
    all_products = Product.all()
    self.assertEqual(len(all_products), 10)
    for product in all_products:
        self.assertIsNotNone(product.id)
        self.assertIsNotNone(product.name)
        self.assertIsNotNone(product.description)
        self.assertIsNotNone(product.price)

def test_find_by_name(self):
    """It should Find a Product by Name"""
    product = ProductFactory()
    product.id = None
    product.create()
    self.assertIsNotNone(product.id)
    found_product = Product.find_by_name(product.name)
    self.assertIsNotNone(found_product)
    self.assertEqual(found_product.id, product.id)
    self.assertEqual(found_product.name, product.name)
    self.assertEqual(found_product.description, product.description)
    self.assertEqual(found_product.price, product.price)

def test_find_by_category(self):
    """It should Find a Product by Category"""
    product = ProductFactory()
    product.id = None
    product.create()
    self.assertIsNotNone(product.id)
    found_products = Product.find_by_category(product.category)
    self.assertEqual(len(found_products), 1)
    found_product = found_products[0]
    self.assertIsNotNone(found_product)
    self.assertEqual(found_product.id, product.id)
    self.assertEqual(found_product.name, product.name)
    self.assertEqual(found_product.description, product.description)
    self.assertEqual(found_product.price, product.price)

def test_find_by_available(self):
    """It should Find a Product by Availability"""
    product = ProductFactory()
    product.id = None
    product.create()
    self.assertIsNotNone(product.id)
    found_products = Product.find_by_available(product.available)
    self.assertEqual(len(found_products), 1)
    found_product = found_products[0]
    self.assertIsNotNone(found_product)
    self.assertEqual(found_product.id, product.id)
    self.assertEqual(found_product.name, product.name)
    self.assertEqual(found_product.description, product.description)
    self.assertEqual(found_product.price, product.price)