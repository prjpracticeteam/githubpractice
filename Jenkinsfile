pipeline {
    agent any
    stages {
        stage('git chechout '){
            steps{
                git branch: 'project-2-div', url: 'https://github.com/prjpracticeteam/githubpractice.git'
            }
        }
        stage('docker image  build') {
            steps {
                sh 'sudo docker build -t myimage .'
            }
        }
    }
}
