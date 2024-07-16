from prefect_gcp.cloud_storage import GcsBucket

gcp_cloud_storage_bucket_block = GcsBucket.load("prefect-gcp-mre")

gcp_cloud_storage_bucket_block.put_directory()
