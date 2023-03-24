pipeline {
    agent any
    stages {
        stage('docker image  build') {
            steps {
                sh 'sudo docker build .'
            }
        }
        stage('checkout '){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/project_task']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/prjpracticeteam/githubpractice.git']]])
            }
        }
        stage('git '){
            steps{
                git branch: 'project_task', url: 'https://github.com/prjpracticeteam/githubpractice.git'
            }
        }
    }
}
