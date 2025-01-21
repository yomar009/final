def test_get_product(client):
    """It should Get a Product by ID"""
    product = ProductFactory()
    product.id = None
    product.create()
    response = client.get(f'/products/{product.id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == product.id
    assert data['name'] == product.name
    assert data['description'] == product.description
    assert data['price'] == product.price

def test_update_product(client):
    """It should Update a Product by ID"""
    product = ProductFactory()
    product.id = None
    product.create()
    new_data = create_fake_product()
    response = client.put(f'/products/{product.id}', json=new_data)
    assert response.status_code == 200
    updated_product = Product.find_by_id(product.id)
    assert updated_product.name == new_data['name']
    assert updated_product.description == new_data['description']
    assert updated_product.price == new_data['price']

def test_delete_product(client):
    """It should Delete a Product by ID"""
    product = ProductFactory()
    product.id = None
    product.create()
    response = client.delete(f'/products/{product.id}')
    assert response.status_code == 204
    assert Product.find_by_id(product.id) is None

def test_get_products(client):
    """It should List all Products"""
    products = [ProductFactory() for _ in range(10)]
    for product in products:
        product.id = None
        product.create()
    response = client.get('/products')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 10
    for product, product_data in zip(products, data):
        assert product_data['id'] == product.id
        assert product_data['name'] == product.name
        assert product_data['description'] == product.description
        assert product_data['price'] == product.price

def test_query_by_name(client):
    """It should List Products by Name"""
    products = [ProductFactory() for _ in range(10)]
    for product in products:
        product.id = None
        product.create()
    response = client.get('/products?name=Hat')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['name'] == 'Hat'

def test_query_by_category(client):
    """It should List Products by Category"""
    products = [ProductFactory() for _ in range(10)]
    for product in products:
        product.id = None
        product.create()
    response = client.get('/products?category=Electronics')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 3
    for product_data in data:
        assert product_data['category'] == 'Electronics'

def test_query_by_availability(client):
    """It should List Products by Availability"""
    products = [ProductFactory() for _ in range(10)]
    for product in products:
        product.id = None
        product.create()
    response = client.get('/products?availability=true')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 5
    for product_data in data:
        assert product_data['availability'] == True