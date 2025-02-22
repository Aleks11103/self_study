USE store_simple;

SELECT category, count(1) FROM store
GROUP BY category
ORDER BY category;

SELECT sum(price * sold_num) FROM store;
    
SELECT 
	category,
    COUNT(product_name) AS count_product,
    SUM(sold_num) AS sold_product,
    SUM(sold_num * price) AS revenue
FROM
	store
GROUP BY category
ORDER BY revenue DESC;
    
SELECT * FROM store;

SELECT 
	product_name, 
    sold_num, 
    price, 
    sold_num * price AS revenue_product
FROM store
ORDER BY sold_num DESC, price DESC
LIMIT 10;