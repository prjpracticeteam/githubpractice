pipeline {
    agent { 
        docker { 
            image 'python:latest'
        stages {
        stage('Checkout') {
            steps {
               checkout scmGit(branches: [[name: '*/project-2-div']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/prjpracticeteam/githubpractice.git']])
            }
        }
        stage('Run python program') {
            steps {
               
                sh 'python main.py'
            }
        }                 
           
        
    }
}
