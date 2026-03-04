


select USER_ID, NICKNAME, sum(PRICE) as TOTAL_SALES
from USED_GOODS_BOARD as a
left join USED_GOODS_USER as b
on a.WRITER_ID = b.USER_ID
WHERE a.STATUS = 'DONE'
group by a.WRITER_ID
having sum(PRICE) >= 700000
order by sum(PRICE) asc