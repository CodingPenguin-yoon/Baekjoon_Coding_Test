-- 코드를 입력하세요
SELECT INGREDIENT_TYPE, sum(TOTAL_ORDER)
from FIRST_HALF as a
join ICECREAM_INFO as b on a.FLAVOR = b.FLAVOR
group by b.INGREDIENT_TYPE
order by sum(TOTAL_ORDER) asc;