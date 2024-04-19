## DATASOURCE

#### GlobalLandTemperaturesByCountry.csv
#### from Climate Change: Earth Surface Temperature Data Kaggle dataset

## SCOPE

## INSTRUCTIONS

#### clone the repo to your local/virtual machine
#### cp dev.env .env

#### CREATE A PROJECT IN https://console.cloud.google.com/:

#### project name: MyWeatherDataProject
#### project ID: myweatherdataproject

#### CREATE A GOOGLE STORAGE BUCKET

#### CREATE A SERVICE ACCOUNT WITH ROLES
#### viewer
#### storage admin
#### storage object admin
#### bigquery admin
#### bigquery data owner

#### CREATE A JSON KEY FOR THIS SERVICE ACCOUNT
#### download and rename the file as my-creds.json

#### CREATE A /keys FOLDER in your home/  AND PLACE THE my-creds.json FILE THERE
#### COPY THE my-creds.json FILE INTO FOLDER mage/

#### follow terraform instructions
#### follow mage instructions
#### follow bigquery instructions
#### create your dashboard

#### Tools/ Resources Used
#### 1. Terraform
#### 2. Mage
#### 3. GCP Cloud Storage
#### 4. GCP Bigquery
#### 5. Docker/docker-compose
#### 6. Google Looker Studio

## Locate the terraform file with cd and 
#### terraform init
#### terraform plan
#### terraform apply

## Locate the mage folrder with cs and 
#### docker compose build
#### docker compose up -d
#### forward port 6789 if not automatically forwarded

## @ http://localhost:6789/
#### run the .py scripts in the following order:
#### load_weather_data_dt.py
#### transform_weather_data_dt.py
#### export_weather_data_gs.py
#### load_weather_data_from_parguet.py
#### export_weather_data_bigquery.py

## @ bigquery dashboard
#### run the sql.sql query to create 2 tables
#### (partitioned_clustered and report)

## @ looker studio
#### create a datasource from the report table
#### create your visualisations

### do not forget to
### terraform destroy
### in order to delete your google cloud resources


