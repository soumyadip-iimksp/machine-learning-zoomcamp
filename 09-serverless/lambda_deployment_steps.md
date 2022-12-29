 Create aws ecr repository
    ```
    aws ecr create-repository --repository-name clothing-tflite-images
    ```

Login to docker on desktop with ECR account
    ```
    aws ecr get-login-password | docker login --username AWS --password-stdin xxxxxxxxx.dkr.ecr.ap-south-1.amazonaws.com/clothing-tflite-images
    ```

Pick Account details from "repositoryURI"
    ->

```
ACCOUNT = xxxxxxxxxx
REGION = ap-south-1
REGISTRY = clothing-tflite-images
PREFIX = ${ACCOUNT}.dkr.ecr.${REGION}.amazonaws.com/${REGISTRY} 

TAG = clothing-model-xception-v6-001
REMOTE_URI = ${PREFIX}:${TAG}

REMOTE_URI = <repositoryURI>:clothing-model-xception-v6-001
```

Tag the created container to the ECR 
    ->  
```
docker tag clothing-model:latest REMOTE_URI
```

Push the container to ECR
    ->  
```
    docker push REMOTE_URI
```

```
Go to Lambda 
    ->  click on Create functions 
        ->   Select Container Image  
            ->  Name "clothing classifier" 
                ->   Click on Container image URI 
                    -> Selectthe applicable container and then click Create function
                        ->   Click on Test and Create a new event: put the pants url in the dictionary
                            -> Failed the test due to task time out (3 sec) as for 1st time it will take longer duration to initialize 
                                ->  Go to Configuration -> General Information -> Edit memory to 1024 MB and Timeout to 30 sec -> Run Test again
```

Need to create API gateway to expose Lambda function as API gateway

```
Search and go to API Gateway
```
```
Click on Build for REST API
```
```
Click on New API and enter API name and CREATE API
```
```
Click on ACTIONS and from dropdown choose CREATE RESOURCE then enter "predict" in RESOURCE NAME
```
```
Click on CREATE METHOD to create a method (POST) to invoke the ENDPOINT 
```

```
Click the tick mark under POST and select LAMBDA FUNCTION as Integration Type, choose the LAMBDA FUNCTION name and SAVE
```

```
Click on TEST and enter the url as dictionary (JSON Format) in the REQUEST BODY and run TEST agaian to check and confirm the response
```
```
Click on ACTIONS and then on DEPLOY API
```
To find the AURL of the API again, 
```
Go to API gateway
Select the corret name of the API
Select STAGES and then will find the invoke url
```
