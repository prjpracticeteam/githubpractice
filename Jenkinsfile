pipeline {
    agent any
    stages{
        stage('docker image Execution') {
           agent { docker {image 'python:latest'} }
        stages {
        stage('Checkout') {
            steps {
               checkout([$class: 'GitSCM', branches: [[name: '*/feat-project2']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/prjpracticeteam/githubpractice.git']]])
            }
        }
        stage('Run python program') {
            steps {
                git branch: 'feat-project2', url: 'https://github.com/prjpracticeteam/githubpractice.git'
                sh 'python hashmap.py L1.txt L2.txt R.txt'
            }
        }                 
           }
        }
    }
}
