@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Retrieve a single Product"""
    app.logger.info("Request for product with id [%s]", product_id)
    product = Product.find(product_id)
    if not product:
        abort(status.HTTP_404_NOT_FOUND, f"Product with id '{product_id}' was not found.")
    app.logger.info("Returning product: %s", product.name)
    return product.serialize(), status.HTTP_200_OK

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update a Product"""
    app.logger.info("Request to update product with id [%s]", product_id)
    check_content_type("application/json")
    product = Product.find(product_id)
    if not product:
        abort(status.HTTP_404_NOT_FOUND, f"Product with id '{product_id}' was not found.")
    data = request.get_json()
    app.logger.info(data)
    product.deserialize(data)
    product.id = product_id
    product.update()
    return make_response(jsonify(product.serialize()), status.HTTP_200_OK)

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a Product"""
    app.logger.info("Request to delete product with id [%s]", product_id)
    product = Product.find(product_id)
    if product:
        product.delete()
    return '', status.HTTP_204_NO_CONTENT

@app.route('/products', methods=['GET'])
def list_products():
    """Returns a list of Products"""
    app.logger.info("Request to list Products...")
    products = []
    name = request.args.get("name")
    category = request.args.get("category")
    available = request.args.get("available")
    if name:
        app.logger.info("Find by name: %s", name)
        products = Product.find_by_name(name)
    elif category:
        app.logger.info("Find by category: %s", category)
        category_value = getattr(Category, category.upper(), None)
        products = Product.find_by_category(category_value)
    elif available:
        app.logger.info("Find by availability: %s", available)
        available_value = available.lower() in ["true", "yes", "1"]
        products = Product.find_by_availability(available_value)
    else:
        app.logger.info("Find all")
        products = Product.all()
    results = [product.serialize() for product in products]
    app.logger.info("[%s] Products returned", len(results))
    return jsonify(results), status.HTTP_200_OK