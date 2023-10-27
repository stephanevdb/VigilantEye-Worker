pipeline {
    agent any
    stages {
        stage('Build local image') {
            steps {
                sh 'echo "Building"'
                sh 'docker buildx build -t stephanevdb/vigilanteye-worker:latest .'
            }
        }
        stage('Push image') {
            steps {
                sh 'echo "Pushing"'
                sh 'docker buildx build --push --platform linux/amd64,linux/arm64 -t stephanevdb/vigilanteye-worker:latest .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Sending POST request"'
                sh 'curl -X POST -H "Content-Type: application/json" https://portainer.stephanevdb.com/api/webhooks/27a7d9cf-081b-4356-93a1-139885372606'
                sh 'curl -X POST -H "Content-Type: application/json" https://portainer.stephanevdb.com/api/webhooks/2610ff18-36fb-41fb-a0e3-62ee612e46b5'
            }
        }
    }
}