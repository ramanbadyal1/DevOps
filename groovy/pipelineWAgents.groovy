pipeline {
    agent none
    stages {
        stage ('Build Stage') {
            agent {
                label 'jenkins-agent-1'
            }
            steps {
                script {
                    echo 'building the first stage'
                }
            }
        }
        stage ('second stage') {
            agent {
                label 'jenkins-agent-1'
            }
            steps {
                script {
                    echo 'building the second stage'
                }
            }
        }
        stage ('third stage') {
            agent {
                label 'jenkins-agent-2'
            }
            steps {
                script {
                    echo 'building the third stage'
            }
            }
        }
    }
}