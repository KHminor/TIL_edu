SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, "%Y-%m-%d") AS PUBLISHED_DATE
FROM BOOK
WHERE PUBLISHED_DATE LIKE "2021%"
GROUP BY CATEGORY
HAVING CATEGORY = '인문'
ORDER BY 2


SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, "%Y-%m-%d") AS PUBLISHED_DATE
FROM BOOK
WHERE CATEGORY = "인문" AND PUBLISHED_DATE LIKE "2021%"
ORDER BY 2