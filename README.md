# AWS_Lambda_API_Gateway_EventBridge
https://www.youtube.com/watch?v=5rG-YgTHMC8&amp;ab_channel=DigitalCloudTraining


-LambdaMessage.py code needs to be added into AWS lambda section
-deploy it
-then test and event with the jsonEvent.json file
-on test tab , the save the jsonEvent content, and select test

-invoke lambda function into console (CLI)
-create payload on the console, and then 
  aws lambda invoke --function-name WriteToCloudWatch --payload fileb://payload.json response.json

-make sure to delete s3 bucket files and lambda functions after practice