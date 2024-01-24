-- Exercício 1
SELECT * FROM books;
-- A)
SELECT title, author FROM books;
-- B)
SELECT title FROM books WHERE author LIKE 'Henry Davis';
-- C)
SELECT title, author, release_year FROM books WHERE release_year < 1900;
-- D)
SELECT title FROM books WHERE title LIKE 'O%';
-- E)
SELECT title, author FROM books WHERE release_year > 1950;
-- F)
SELECT COUNT(*) FROM books;
-- G)
SELECT author "Autor", COUNT(*) "Quantidade de Livros" 
FROM books GROUP BY 1 ORDER BY 1 LIMIT 1;
-- H)
SELECT title "Titulo", release_year "Ano de Publicação"
FROM books ORDER BY 2;
-- I)
SELECT title "Titulo", release_year "Ano de Publicação"
FROM books ORDER BY 2 ASC LIMIT 1;
-- J)
SELECT title "Titulo", release_year "Ano de Publicação"
FROM books ORDER BY 2 DESC LIMIT 1;
--K)
SELECT title "Titulo", author "Autor"
FROM books ORDER BY id DESC LIMIT 3;