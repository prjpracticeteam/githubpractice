pipeline {
    agent any
    stages {
        stage('git chechout '){
            steps{
                git branch: 'project_task', url: 'https://github.com/prjpracticeteam/githubpractice.git'
            }
        }
        stage('docker image  build') {
            steps {
                sh 'sudo docker build .'
            }
        }
    }
}
