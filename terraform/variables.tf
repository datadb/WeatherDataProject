variable "credentials" {
  description = "My Credential to GCP"
  default     = "/workspaces/WeatherDataProject/keys/my-creds.json"
}

variable "project" {
  description = "Project"
  default     = "myweatherdataproject"
}

variable "region" {
  description = "Region"
  // Update the below to your desired region
  default = "europe-west1"
}

variable "location" {
  description = "Project Location"
  // Update the below to your desired location
  default = "EU"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  // Update the below to a unique bucket name
  default = "myweatherdataproject-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  # Update the below to what you want your dataset to be called
  default = "weather_dataset"
}





