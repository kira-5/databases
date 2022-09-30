from google.cloud import bigquery

def log_in():
    # Construct a BigQuery client object.
    # client = bigquery.Client()
    # BigQuery project id as listed in the Google Developers Console.
    service_key_path = "C://Users/abhiv/Downloads/sample-db-363712-cae944fe1e4d.json"
    # client = bigquery.Client.from_sevice_account.json(service_key_path)
    client = bigquery.Client.from_service_account_json(service_key_path)

    # Submit an async query.
    job_id, _results = client.query('SELECT * FROM dataset.my_table LIMIT 1000')

    # Check if the query has finished running.
    complete, row_count = client.check_job(job_id)

    # Retrieve the results.
    results = client.get_query_rows(job_id)
    
    if complete:
        results = client.get_query_rows(job_id)
    # You can also specify a non-zero timeout value if you want your query to be synchronous.

    # Submit a synchronous query
    try:
        _job_id, results = client.query('SELECT * FROM dataset.my_table LIMIT 1000', timeout=10)
    except Exception:
        print("Timeout")