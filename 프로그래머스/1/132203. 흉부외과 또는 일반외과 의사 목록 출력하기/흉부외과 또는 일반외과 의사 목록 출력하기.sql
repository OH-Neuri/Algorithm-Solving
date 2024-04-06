
SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD,'%Y-%m-%d') from doctor
where MCDP_CD = 'CS' OR MCDP_CD = 'GS'
order by hire_ymd desc, dr_name; 