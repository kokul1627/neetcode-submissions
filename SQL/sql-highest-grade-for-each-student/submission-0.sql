-- Write your query below
select distinct on (student_id)student_id,exam_id,score 
from exam_results
group by  exam_id,student_id
order by student_id, score DESC , exam_id ASC;

