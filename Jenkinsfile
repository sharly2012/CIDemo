pipeline {
    agent any
    environment {
        PROJECT_ID = "${PROJECT_ID}"
        LANGUAGE = "Python"
        DEPLOY_TO = "production"
    }
    stages {
        stage('Build Environment') {
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
                echo 'This is the Build Environment part ...'
                sh '''python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt'''
            }
            post{
                failure {
                    script {
                        sh 'echo "Build Environment failure"'
                    }
                }
                success {
                    script {
                        sh 'echo "Build Environment success"'
                    }
                }
                aborted {
                    script {
                        sh 'echo "Build Environment aborted"'
                    }
                }
            }
        }
        stage('Execute'){
            steps {
                echo 'This is Execute Test part ...'
                sh 'venv/bin/python -m pytest testcases --alluredir ${WORKSPACE}/report/${BUILD_ID}/xml'
            }
            post{
                failure {
                    script {
                        sh 'echo "Execute The job failure"'
                    }
                }
                success {
                    script {
                        sh 'echo "Execute The job success"'
                    }
                }
                aborted {
                    script {
                        sh 'echo "Execute The job aborted"'
                    }
                }
            }
        }
        stage('Report'){
            steps {
                echo 'This is report'
                allure includeProperties: false, jdk: '', results: [[path: 'report/${BUILD_ID}/xml']]
            }
            post{
                failure {
                    script {
                        sh 'echo "Generate report failure"'
                    }
                }
                success {
                    script {
                        sh 'echo "Generate report success"'
                    }
                }
                aborted {
                    script {
                        sh 'echo "Generate report aborted"'
                    }
                }
            }
        }
    }
}
