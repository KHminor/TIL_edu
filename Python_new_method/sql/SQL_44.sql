-- 평균 일일 대여 요금 구하기
SELECT ROUND(AVG(DAILY_FEE)) AS AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR 
WHERE CAR_TYPE = "SUV"

SELECT ROUND(AVG(DAILY_FEE)) AS AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR 
GROUP BY CAR_TYPE
HAVING CAR_TYPE = "SUV"