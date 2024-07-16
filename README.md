This repository provides a minimum reproducible example of an unexpected behavior exhibited by the `GcsBucket` class from the `prefect-gcp` package.

## Setup

```
python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

## Step 1: Create a GcsBucket storage block

```shell
$ python build_gcs_bucket_block.py
```


## Step 2: Copy the project to the GCS bucket 

```shelll
$ python example.py
```

## Expected

The current working directory is uploaded to the bucket path

```
gs://prefect-gcp-mre/example/v0.1.0/
```

## Observed

The current working directory is upload to the bucket path

```
gs://prefect-gcp-mre/example/v0.1.0/example/v0.1.0/
```