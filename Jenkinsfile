pipeline {
agent any

```
environment {
    AWS_REGION = 'ap-south-2'
    ACCOUNT_ID = '633031012723'

    ECR_REPO = 'my-node-app'

    CLUSTER = 'my-cluster'
    SERVICE = 'my-service'

    IMAGE_TAG = "${BUILD_NUMBER}"
}

stages {

    stage('Build Docker Image') {
        steps {
            sh '''
            docker build -t web-app:${IMAGE_TAG} .
            '''
        }
    }

    stage('Login to ECR') {
        steps {
            sh '''
            aws ecr get-login-password --region ${AWS_REGION} | \
            docker login --username AWS --password-stdin \
            ${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com
            '''
        }
    }

    stage('Tag Docker Image') {
        steps {
            sh '''
            docker tag web-app:${IMAGE_TAG} \
            ${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}

            docker tag web-app:${IMAGE_TAG} \
            ${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:latest
            '''
        }
    }

    stage('Push Image to ECR') {
        steps {
            sh '''
            docker push ${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG}

            docker push ${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:latest
            '''
        }
    }

    stage('Deploy ECS') {
        steps {
            sh '''
            aws ecs update-service \
            --cluster ${CLUSTER} \
            --service ${SERVICE} \
            --force-new-deployment \
            --region ${AWS_REGION}
            '''
        }
    }

    stage('Wait for ECS Deployment') {
        steps {
            sh '''
            aws ecs wait services-stable \
            --cluster ${CLUSTER} \
            --services ${SERVICE} \
            --region ${AWS_REGION}
            '''
        }
    }

    stage('Cleanup') {
        steps {
            sh '''
            docker rmi web-app:${IMAGE_TAG} || true

            docker rmi \
            ${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:${IMAGE_TAG} || true

            docker rmi \
            ${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:latest || true
            '''
        }
    }
}

post {
    success {
        echo 'Deployment completed successfully!'
    }

    failure {
        echo 'Deployment failed!'
    }
}
```

}
