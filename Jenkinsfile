pipeline {
    agent any

    stages {
        stage('DEV') {
            steps {
                echo 'Building..'
            }
        }
        stage('PREPROD') {
            steps {
                echo 'Testing..'
            }
        }
        stage('PROD') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}