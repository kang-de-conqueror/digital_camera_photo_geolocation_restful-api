# **Digital Camera Photo Geolocation**

## **1. Application Description**

A restful API server which serves the functions of uploading (POST) and getting (GET) routes. Detail information can be found in *DCPG_API_Doc.yaml* . You may also find in this repo all other config files which are needed for the deployment or automating deployment.

## **2. Main Feature**

- **Uploading**: Let mobile app users upload their newly recorded route to the MongoDB (via Django) or S3 (via AWS).

- **Getting**: Let CLI app user get route records from Mongo (via Django) or S3 (via AWS).

## **3. Technology**
- AWS
- Django
- Docker/ Jenkin
- Fabric/ Supervisorctl

## **4. Installation**

- Follow closely this instruction to understand how to deploy Django in developing stage : https://docs.djangoproject.com/en/3.0/intro/tutorial01/.

- For production stage, depends on your server hosting platform, the installation may vary.

- Official guides for API Gateway, Lambda, S3 and other services can be found on : https://aws.amazon.com/

## **5. Contact (Author & Maintainer)**
The Team of Khang VU, Khang TRAN, Huy TRAN from INTEK Institute TP.HCM
