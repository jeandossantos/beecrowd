SELECT products.name AS product_name, 
       providers.name AS provider_name, 
       products.price
FROM products
INNER JOIN providers
ON products.id_providers = providers.id
INNER JOIN categories
ON products.id_categories = categories.id
WHERE products.price > 1000 
  AND categories.name = 'Super Luxury';