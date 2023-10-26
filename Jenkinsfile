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
                sh 'curl -X POST -H "Content-Type: application/json" https://portainer.stephanevdb.com/api/webhooks/7174daef-8fc8-42ff-8236-8832a9505866'
            }
        }
    }
}