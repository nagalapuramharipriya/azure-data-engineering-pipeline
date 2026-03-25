SELECT product, SUM(amount) AS total_sales
FROM sales
GROUP BY product;
