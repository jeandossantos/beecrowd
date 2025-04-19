SELECT 
    products.name AS product_name,
    providers.name AS provider_name,
    categories.name AS category_name
FROM products
INNER JOIN providers
ON products.id_providers = providers.id
INNER JOIN categories
ON products.id_categories = categories.id
WHERE providers.name = 'Sansul SA'
  AND categories.name = 'Imported';