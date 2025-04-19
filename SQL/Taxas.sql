SELECT 
    name AS person_name,
    ROUND(salary * 0.10, 2) AS tax_amount
FROM people
WHERE salary > 3000;