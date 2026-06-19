#!/usr/bin/env python3
"""
Data ingestion module for Azure Data Pipeline
This script handles ingestion from various sources to Bronze layer
"""

import logging
from azure.storage.blob import BlobServiceClient
from azure.identity import DefaultAzureCredential

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def ingest_csv_to_bronze(source_path, destination_container, destination_blob):
    """
    Ingests CSV data from source to Azure Blob Storage (Bronze layer)
    
    Args:
        source_path: Local path to CSV file
        destination_container: Container name in ADLS
        destination_blob: Blob path in ADLS
    """
    try:
        # Using Managed Identity for authentication
        credential = DefaultAzureCredential()
        blob_service_client = BlobServiceClient(
            account_url="https://yourstorage.blob.core.windows.net",
            credential=credential
        )
        
        # Upload file
        with open(source_path, "rb") as data:
            blob_client = blob_service_client.get_blob_client(
                container=destination_container,
                blob=destination_blob
            )
            blob_client.upload_blob(data, overwrite=True)
            logger.info(f"Successfully ingested {source_path} to Bronze layer")
            
    except Exception as e:
        logger.error(f"Error during ingestion: {str(e)}")
        raise

if __name__ == "__main__":
    # Example usage
    ingest_csv_to_bronze(
        source_path="data/sample.csv",
        destination_container="bronze",
        destination_blob="raw_data/sample.csv"
    )
