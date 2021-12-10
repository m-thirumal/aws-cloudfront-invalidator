# AWS cloud front invalidator

CloudFront Invalidation in CodePipeline using Lambda 

![Pipeline](img/code_pipline_1.png)

#### Framework

    pip install chalice

#### Deploy

Run `chalice deploy` to deploy your Chalice application:

    chalice deploy

#### User parameters 

Replace `{distribution_id}` 

    {
       "distributionId": "{distribution_id}", 
       "objectPaths": ["/*"]
    }

![Pipeline](img/pipeline.png)