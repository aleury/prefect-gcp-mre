from prefect_gcp import GcsBucket

storage = GcsBucket(
    bucket="prefect-gcp-mre",
    bucket_folder="example/v0.1.0",
)
storage.save("prefect-gcp-mre", overwrite=True)
