--Highest Paying Roles 
SELECT *
FROM salary_analytics
ORDER BY avg_salary DESC
LIMIT 10;
-- Most common jobs
SELECT
    title,
    COUNT(*) AS total_jobs
FROM job_postings
GROUP BY title
ORDER BY total_jobs DESC
LIMIT 10;
-- Average salary by location
SELECT
    location,
    ROUND(AVG(salary_min)) AS avg_salary
FROM job_postings
GROUP BY location
ORDER BY avg_salary DESC;