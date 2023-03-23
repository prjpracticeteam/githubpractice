pipeline {
    agent any
    stages {
        stage('docker image  build') {
            steps {
                sh 'docker build .'
            }
        }
        stage('checkout '){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/feat-project2']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/prjpracticeteam/githubpractice.git']]])
            }
        }
        stage('git '){
            steps{
                git branch: 'feat-project2', url: 'https://github.com/prjpracticeteam/githubpractice.git'
            }
        }
    }
}
