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