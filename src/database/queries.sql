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
