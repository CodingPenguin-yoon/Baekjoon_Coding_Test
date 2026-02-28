-- 코드를 입력하세요
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
from (
    select
    *,
    RANK() over (PARTITION BY FOOD_TYPE order by FAVORITES desc) as rnk
    from REST_INFO
) AS ranked_info
where rnk = 1
order by FOOD_TYPE desc;