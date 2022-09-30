from google.cloud import bigquery

def log_in():
    # Construct a BigQuery client object.
    # client = bigquery.Client()
    service_key_path = "C://Users/abhiv/Downloads/sample-db-363712-cae944fe1e4d.json"
    # client = bigquery.Client.from_sevice_account.json(service_key_path)
    client = bigquery.Client.from_service_account_json(service_key_path)

    # TODO(developer): Set dataset_id to the ID of the dataset to create.
    # dataset_id = "{}.your_dataset".format(client.project)
    # client = bigquery.Client.from_service_account_json(SERVICE_ACCOUNT_JSON)
    # bucket_name = "extracted_dataset"
    project =  "sample-db-363712"
    dataset_id = 'pricesmart'

    # Construct a full Dataset object to send to the API.
    dataset = bigquery.Dataset(dataset_id)

    # TODO(developer): Specify the geographic location where the dataset should reside.
    dataset.location = "US"

    # Send the dataset to the API for creation, with an explicit timeout.
    # Raises google.api_core.exceptions.Conflict if the Dataset already
    # exists within the project.
    dataset = client.create_dataset(dataset, timeout=30)  # Make an API request.
    print("Created dataset {}.{}".format(project, dataset.dataset_id))