
import psycopg2
from mypack.config.utils import config_parser
import os
import mypack

config_path = os.path.dirname(mypack.__file__ )+ '/config/database.ini'


chrun_rate = """
select 1 - (
	COUNT(DISTINCT(CASE WHEN EXTRACT(MONTH FROM created_at) = 12 THEN company_id END)) * 1.0
	/
 	COUNT(DISTINCT(CASE WHEN EXTRACT(MONTH FROM created_at) = 1 THEN company_id END))
	)AS churn_rate
	
FROM SESSION
"""

revenue = """
SELECT SUM(subscription_amount) as revenue
FROM (
	SELECT 
	company_id
	FROM session 
	GROUP BY EXTRACT(MONTH FROM created_at), company_id
) as gp
 LEFT JOIN subscription as s ON s.company_id = gp.company_id
"""

avg_session_count_per_comapny_in_month = """
SELECT AVG(session_counts)
FROM
(
SELECT EXTRACT(MONTH FROM created_at) as month, company_id, count(*) as session_counts
FROM session 
group by EXTRACT(MONTH FROM created_at), company_id
) as a
"""


def query_exec(sql):

    conn = None
    try:
        # read database configuration
        params = config_parser(config_path)
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchone()
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print('pggggg', error)
    finally:
        if conn is not None:
            conn.close()
        return res[0]

if __name__ == '__main__':
    queries = ['chrun_rate', 'revenue', 'avg_session_count_per_comapny_in_month']

    for q in queries:
        print(q, ': ', query_exec(eval(q)))







