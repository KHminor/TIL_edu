-- 틀림
SELECT T2.HISTORY_ID, (CASE
                        WHEN 7 > DATEDIFF(T2.END_DATE+1, T2.START_DATE) THEN 
                            ROUND(DATEDIFF(T2.END_DATE+1, T2.START_DATE) * T1.DAILY_FEE)
                        WHEN (DATEDIFF(T2.END_DATE+1, T2.START_DATE) BETWEEN 7 AND 29) THEN
                            ROUND((
                                SELECT T3.DISCOUNT_RATE 
                                FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN T3
                                WHERE T3.CAR_TYPE = '트럭' AND T3.DURATION_TYPE LIKE '7%'
                            ) * 0.01 * T1.DAILY_FEE * DATEDIFF(T2.END_DATE+1, T2.START_DATE))
                        WHEN (DATEDIFF(T2.END_DATE+1, T2.START_DATE) BETWEEN 30 AND 89) THEN
                            ROUND((
                                SELECT T3.DISCOUNT_RATE 
                                FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN T3
                                WHERE T3.CAR_TYPE = '트럭' AND T3.DURATION_TYPE LIKE '30%'
                            ) * 0.01 * T1.DAILY_FEE * DATEDIFF(T2.END_DATE+1, T2.START_DATE))
                        WHEN DATEDIFF(T2.END_DATE+1, T2.START_DATE) >= 90 THEN
                            ROUND((
                                SELECT T3.DISCOUNT_RATE 
                                FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN T3
                                WHERE T3.CAR_TYPE = '트럭' AND T3.DURATION_TYPE LIKE '90%'
                            ) * 0.01 * T1.DAILY_FEE * DATEDIFF(T2.END_DATE+1, T2.START_DATE))
                      END
                    ) AS FEE
FROM CAR_RENTAL_COMPANY_CAR T1 JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY T2 
    ON T1.CAR_ID = T2.CAR_ID 
WHERE T1.CAR_TYPE = '트럭'
ORDER BY 2 DESC, 1 DESC