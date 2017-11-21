#!/usr/bin/env python3

import psycopg2

"""Reporting tool that prints out reports (in plain text)
based on the data in the database"""

#  Database name
DBNAME = 'news'

#  What are the most popular three articles of all time?
#  Which articles have been accessed the most?
#  Present this information as a sorted list
#  with the most popular article at the top
msg1 = 'What are the most popular three articles of all time?'
query1 = '''
SELECT title, views
FROM articles
INNER JOIN
    (SELECT path, count(path) AS views
     FROM log
     GROUP BY log.path) AS log
ON log.path = '/article/' || articles.slug
ORDER BY views DESC
LIMIT 3;
'''

#  Who are the most popular article authors of all time?
#  That is, when you sum up all of the articles each author has written,
#  which authors get the most page views?
#  Present this as a sorted list with the most popular author at the top.
msg2 = 'Who are the most popular article authors of all time?'
query2 = '''
SELECT
  authors.name,
  COUNT(authors.id) AS top
FROM log
JOIN articles
  ON log.path = concat('/article/', articles.slug)
JOIN authors
  ON articles.author = authors.id
GROUP BY authors.id
ORDER BY top DESC
'''

#  On which days did more than 1% of requests lead to errors?
#  The log table includes a column status that indicates the HTTP status code
#  that the news site sent to the user's browser.
msg3 = 'On which days did more than 1% of requests lead to errors?'
query3 = '''
SELECT date, round(percentage, 3)
FROM
(
    SELECT
      time::DATE AS date,
      SUM (
        CASE WHEN status LIKE '%404%'
        THEN 1
        ELSE 0
        END)::NUMERIC / COUNT (status) * 100 AS percentage
    FROM log
    GROUP BY date
)
AS errors
WHERE percentage > 1.0;
'''


def get_result_set(query):
    """Connects to DB for fetching result set by executing query"""
    try:
        db = psycopg2.connect(database=DBNAME)
        cursor = db.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        db.close()
        return results
    except psycopg2.Error as e:
        print(e.pgerror)


def print_result(msg,
                 results,
                 show_index=1,
                 show_article=0,
                 show_author=0,
                 show_date=0,
                 show_pplar=0,
                 show_errors=0):
    """Flexible for printing popular items or error percentage logs"""
    print(msg)  # printing message
    # iterating over a fixed list of size(2)
    for index, result in enumerate(results, 1):
        print("{}) {}{}{} {}\t{} {}{} {}{}".format(show_index * index,
                                                   show_article * 'Article:',
                                                   show_author * 'Author:',
                                                   show_date * 'Date:',
                                                   result[0],
                                                   show_pplar * 'Popularity:',
                                                   show_errors * 'Errors:',
                                                   result[1],
                                                   show_pplar * 'views',
                                                   show_errors * '%'))
	print()

if __name__ == '__main__':
    articles = get_result_set(query1)  # loading top articles
    print_result(msg1, articles, show_article=1, show_pplar=1)
    authors = get_result_set(query2)  # loading top authors
    print_result(msg2, authors, show_author=1, show_pplar=1)
    errors = get_result_set(query3)  # loading errors > 1%
    print_result(msg3, errors, show_date=1, show_errors=1)
