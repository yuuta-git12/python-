import psycopg2

# 接続情報
# dbname:接続先のDB名, host:接続先のアドレス, user:接続に使用するDBユーザ名, password:接続に使用するDBユーザのパスワード
dsn = "dbname=fishing_diary host=localhost user=postgres password="

# 釣果入力フォームで入力した値をDBに登録するクエリ
query = "INSERT INTO fishing_log(fish_name,fish_weight,fish_scale,fishing_place,fishing_date) VALUES(%s,%s,%s,%s,%s) "

# 日付順に並び替えてデータを取得するクエリ
query2 = "SELECT * from fishing_log ORDER BY fishing_date"


def select_all():
    with psycopg2.connect(dsn) as conn:
        with conn.cursor() as cur:

            cur.execute(query2)
            list_db = cur.fetchall()

            list_range = len(list_db)
            return list_db,list_range


def form_insert(val1, val2, val3, val4, val5):
    with psycopg2.connect(dsn) as conn:
        with conn.cursor() as cur:
            cur.execute(query,(val1, val2, val3, val4, val5))
            conn.commit()





