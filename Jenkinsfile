pipeline {
    agent any

    stages {
        stage('Git Repo Clone') {
            steps {
                sh 'git clone https://github.com/chad-38/cicdpractice.git'
            }
        }
        stage('Build Docker image') {
            steps {
                echo "Building the Docker Image..."
                withCredentials([usernamePassword(credentialsId: 'docker-hub-repo', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                sh "echo $PASS | docker login -u $USER --password-stdin"
                sh 'docker build -t chad38/demo-app:1.1 .'
                sh 'docker push chad38/demo-app:1.1'
                }
            }
        }    
        stage("Removing the content") {
            steps {
                echo "Removing the residuos"
                sh 'rm -rf /var/lib/jenkins/workspace/my-cicd-pipeline/cicdpractice/'
            }
        }
    }
}
