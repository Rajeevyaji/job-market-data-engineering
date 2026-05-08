CREATE TABLE salary_analytics AS
SELECT
    title,
    location,
    COUNT(*) AS total_jobs,
    ROUND(AVG(salary_min)) AS avg_salary,
    MAX(salary_max) AS highest_salary,
    MIN(salary_min) AS lowest_salary
FROM job_postings
GROUP BY title, location;