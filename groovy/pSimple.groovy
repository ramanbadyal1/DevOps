pipeline {
    agent none
    stages {
        stage('Quality Gate') {
            steps {
                    script {
                        echo 'This is the first stage.'
                    }
            }
        }
        stage('production Build Stage') {
            steps {
                script {
                    echo 'Building the application...'
                }
            }
        }
        stage('Deploy Stage') {
            steps {
                script {
                    echo 'Deploying the application...'
                }
            }
        }
    }
}
