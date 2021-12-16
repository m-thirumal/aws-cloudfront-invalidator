# AWS cloud front invalidator

![Python](https://img.shields.io/badge/-Python-333333?style=flat&logo=python)
![AWS Cloud](https://img.shields.io/badge/-AWS%20Cloud-333333?style=flat&logo=amazon)

CloudFront Invalidation in CodePipeline using Lambda 

![Pipeline](img/code_pipline_1.png)

#### Framework

    pip install chalice

#### Deploy

1. Make sure `~ .aws/credentials`, file contains `IAM` user with permission of `lambda, IAM role`

Run `chalice deploy` to deploy your Chalice application:

    chalice deploy

#### User parameters 

Replace `{distribution_id}` 

    {
       "distributionId": "{distribution_id}", 
       "objectPaths": ["/*"]
    }

![Pipeline](img/pipeline.png)