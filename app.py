import json
import boto3
import logging

from chalice import Chalice

app = Chalice(app_name='aws-cloudfront-invalidator', debug=True, configure_logs=False)
app.debug = True
logging.getLogger().setLevel(logging.DEBUG)
# -----------------------------------
# @Author       : Thirumal
# @Email        : m.thirumal@hotmail.com
# @Phone number : +91-8973697871
# Github        : m-thirumal
# Twitter       : _thirumal
# -----------------------------------

code_pipeline = boto3.client("codepipeline")
cloud_front = boto3.client("cloudfront")


@app.lambda_function()
def lambda_handler(event, context):
    logging.debug("AWS cloud front invalidator started with event {}".format(event))
    job_id = event["CodePipeline.job"]["id"]
    logging.debug("Code pipeline job id is {}".format(job_id))
    try:
        user_params = json.loads(
            event["CodePipeline.job"]
            ["data"]
            ["actionConfiguration"]
            ["configuration"]
            ["UserParameters"]
        )
        invalidation = cloud_front.create_invalidation(
            DistributionId=user_params["distributionId"],
            InvalidationBatch={
                "Paths": {
                    "Quantity": len(user_params["objectPaths"]),
                    "Items": user_params["objectPaths"],
                },
                "CallerReference": event["CodePipeline.job"]["id"],
            },
        )
        logging.debug("Create invalidation {}".format(invalidation))
    except Exception as e:
        code_pipeline.put_job_failure_result(
            jobId=job_id,
            failureDetails={
                "type": "JobFailed",
                "message": str(e),
            },
        )
    else:
        code_pipeline.put_job_success_result(
            jobId=job_id,
        )
    logging.debug("!!!!! Invalidation is complete !!!!!")

