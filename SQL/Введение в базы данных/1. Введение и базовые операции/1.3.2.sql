USE project_simple;

SELECT AVG(budget) FROM project;

SELECT 
	client_name,
    AVG(DATEDIFF(project_finish, project_start)) as avg_days,
    MAX(DATEDIFF(project_finish, project_start)) as max_days,
    MIN(DATEDIFF(project_finish, project_start)) as min_days
FROM project WHERE project_finish is not null and DATEDIFF(project_finish, project_start) > 0
group by client_name
order by max_days DESC
LIMIT 10;