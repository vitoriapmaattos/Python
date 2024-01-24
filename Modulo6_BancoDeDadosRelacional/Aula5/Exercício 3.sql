-- Exercicio 3
-- A)
SELECT e.name "Funcionário", e.role "Cargo", d.name "Departamento"
from employees e
LEFT JOIN departments d on (e.department_id = d.id);
-- B)
SELECT 
	e.name Nome, 
	e.role Cargo, 
	e.salary Salário, 
	d.name Departamento
FROM employees e
INNER JOIN departments d
ON e.department_id = d.id
WHERE d.name ILIKE 'vendas';
-- C)
SELECT
	e.name "Colaborador",
	e.role "Cargo",
	e.salary "Salário"
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
WHERE salary::numeric > 3500 AND d.name = 'Vendas';
-- D)
SELECT 
	e.name funcionário, 
	e.role, 
	e.salary, 
	STRING_AGG(p.name, ', ') projetos
FROM employees e
INNER JOIN departments d
ON e.department_id = d.id
INNER JOIN projects p
ON p.department_id = d.id
GROUP BY e.id;
-- E)
SELECT 
	SUM(salary) "Folha de Pagamento"
FROM employees;
-- F)
SELECT
	d.name "Nome do departamento",
	SUM(e.salary) "Folha de Pagamento"
FROM departments d
INNER JOIN employees e
ON e.department_id = d.id
GROUP BY d.id;
-- G)
SELECT
	d.name "Departamento",
	MAX(e.salary) "Maior salário"
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
GROUP BY d.id;