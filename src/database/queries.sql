--create table employers
CREATE TABLE IF NOT EXISTS employers(
    company_id INT PRIMARY KEY,
    company_name VARCHAR(30) NOT NULL
);

--create table vacancies
CREATE TABLE IF NOT EXISTS vacancies(
    vacancy_id SERIAL PRIMARY KEY,
    company_id INT REFERENCES employers(company_id),
    vacancy_name VARCHAR(100) NOT NULL,
    vacancy_salary_from INTEGER NOT NULL,
    vacancy_salary_to INTEGER NOT NULL,
    vacancy_currency VARCHAR(10) NOT NULL,
    vacancy_url VARCHAR(255) UNIQUE NOT NULL
);

--update employers
INSERT INTO employers (company_id, company_name)
VALUES(%s, %s);

--get employers
SELECT company_id, company_name FROM employers;

--update vacancies
INSERT INTO vacancies (company_id, vacancy_name, vacancy_salary_from, vacancy_salary_to,
vacancy_currency, vacancy_url)
VALUES (%s, %s, %s, %s, %s, %s);

--count company vacancies
SELECT company_name, COUNT(*) AS vacancies_total
FROM vacancies LEFT JOIN employers USING(company_id)
GROUP BY company_name;

--get vacancies data
SELECT company_name, vacancy_name, vacancy_salary_from, vacancy_salary_to, vacancy_url
FROM vacancies LEFT JOIN employers USING(company_id);

--get avg salary
SELECT AVG((vacancy_salary_from + vacancy_salary_to) / 2) FROM vacancies;

--get vacancies with higher salary
SELECT company_name, vacancy_name, vacancy_salary_from, vacancy_salary_to, vacancy_url
FROM vacancies LEFT JOIN employers USING(company_id) WHERE vacancy_salary_from >=
(SELECT AVG((vacancy_salary_from + vacancy_salary_to) / 2) FROM vacancies);
