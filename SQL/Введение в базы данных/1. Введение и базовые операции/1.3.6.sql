USE store_simple;

SELECT
	category,
    SUM(price * sold_num) AS vir
FROM store
GROUP BY category
ORDER by vir DESC
LIMIT 5;