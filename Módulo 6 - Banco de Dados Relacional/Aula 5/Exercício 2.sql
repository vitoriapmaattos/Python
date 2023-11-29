-- Exercicio 2
SELECT * FROM products;
-- A)
SELECT SUM(quantity_in_stock) "Estoque"
FROM products;
-- B)
SELECT ROUND(AVG(price::numeric), 2)::money FROM products;
-- C)
SELECT product "Produto", price "Preço"
FROM products ORDER BY 2 DESC LIMIT 1;
-- D)
SELECT product "Produto", price "Preço"
FROM products ORDER BY 2 ASC LIMIT 1;
-- E)
SELECT 
	product "Nome do Produto", 
	price "Preço", 
	quantity_in_stock "Estoque",
	price * quantity_in_stock "Valor em estoque"
FROM products;
-- F)
SELECT COUNT(*)
FROM products
WHERE quantity_in_stock< 20;
-- G)
SELECT 
	product "Produto", price * quantity_in_stock "Valor em estoque"
FROM products
ORDER BY 2 DESC
LIMIT 1;