#!/usr/bin/env python
import psycopg2


def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Unable to connect to the database")


# What are the most popular three articles of all time?
query_1_title = "What are the most popular three articles of all time?"
query_1 = (
    "select articles.title, count(*) as views "
    "from articles "
    "inner join log on log.path "
    "like concat('%', articles.slug, '%') "
    "where log.status like '%200%' "
    "group by articles.title, log.path order by views desc limit 3")

# Who are the most popular article authors of all time?
query_2_title = "Who are the most popular article authors of all time?"
query_2 = (
    "select authors.name, count(*) as views "
    "from articles inner "
    "join authors on articles.author = authors.id "
    "inner join log "
    "on log.path like concat('%', articles.slug, '%') "
    "where "
    "log.status like '%200%' "
    "group by authors.name order by views desc")

# On which days did more than 1% of requests lead to errors
query_3_title = "On which days did more than 1% of requests lead to errors?"
query_3 = (
    "select day, perc "
    "from (select day, round((sum(requests)/(select count(*) "
    "from log where "
    "substring(cast(log.time as text), 0, 11) = day) * 100), 2) as perc "
    "from (select substring(cast(log.time as text), 0, 11) as day, "
    "count(*) as requests from log where status like '%404%' group by day)"
    "as log_percentage group by day order by perc desc) as final_query "
    "where perc >= 1")


def get_query_results(query):
    db, cursor = connect()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()


def query_results(query_results):
    print(query_results[1])
    logresults = open("LogAnalysis", "a")
    logresults.write(query_results[1] + '\n')
    for index, results in enumerate(query_results[0]):
        print(
            index + 1, "-", results[0],
            str(results[1]), "views")
        logresults.write(str(results[0]) + " - " +
                         str(results[1]) + " views" + '\n')
    logresults.close()


def error_results(query_results):
    print (query_results[1])
    logresults = open("LogAnalysis", 'a')
    logresults.write(query_results[1] + '\n')
    for results in query_results[0]:
        print(results[0], "-", str(results[1]) + "% errors")
        logresults.write(str(results[0]) + " - " +
                         str(results[1]) + "% errors")
    logresults.close()


if __name__ == '__main__':
    # store query results
    popular_articles_results = get_query_results(query_1), query_1_title
    popular_authors_results = get_query_results(query_2), query_2_title
    load_error_days = get_query_results(query_3), query_3_title

    # print query results
    query_results(popular_articles_results)
    query_results(popular_authors_results)
    error_results(load_error_days)
