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
                sh 'curl -X POST -H "Content-Type: application/json" https://portainer.stephanevdb.com/api/stacks/webhooks/d1a57ad8-f428-48b0-957a-a8c1cfa2b6fb'
            }
        }
    }
}