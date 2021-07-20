pipeline {
    agent any
    environment {
        PROJECT_ID = "${PROJECT_ID}"
        LANGUAGE = "Python"
        DEPLOY_TO = "production"
    }
    stages {
        stage('Execute') {
            when {
                anyOf {
                    expression {
                        PROJECT_ID == "1000"
                    }
                    allOf {
                        environment name: "LANGUAGE", value: "Python"
                        environment name: 'DEPLOY_TO', value: 'production'
                    }
                }
            }
            steps {
                echo 'This is the execute part ...'
            }
            post{
                failure {
                    script {
                        sh 'echo "The job failure"'
                    }
                }
                success {
                    script {
                        sh 'echo "The job success"'
                    }
                }
                aborted {
                    script {
                        sh 'echo "The job aborted"'
                    }
                }
            }
        }
        stage('Report'){
            steps {
                echo 'This is report'
                sh 'echo $PATH'
            }
        }
    }
}
