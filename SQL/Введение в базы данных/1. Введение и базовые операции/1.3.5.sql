USE store_simple;

SELECT 
	category,
    COUNT(product_name) AS count_product
FROM store
GROUP BY category
ORDER BY category;