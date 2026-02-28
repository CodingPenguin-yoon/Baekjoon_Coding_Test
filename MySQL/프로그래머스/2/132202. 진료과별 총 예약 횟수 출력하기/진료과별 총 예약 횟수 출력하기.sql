-- 코드를 입력하세요
SELECT MCDP_CD as "c진료과코드", count(*)
from APPOINTMENT
where DATE_FORMAT(APNT_YMD,'%y-%m') = '22-05'
group by MCDP_CD
order by count(*) asc,  MCDP_CD asc;