SELECT products.id AS product_id, 
       products.name AS product_name
FROM products
INNER JOIN categories
ON products.id_categories = categories.id
WHERE categories.name LIKE 'super%';