pipeline {
    agent any

    environment {
        PYTHON_VERSION = "3.10"
        AZURE_API_URL = "https://myfunctionappname1.azurewebsites.net/api/monitoring?"  // Replace with your actual API URL
    }

    stages {
       

        stage('Setup Python Environment') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Optimize Pipeline') {
            steps {
                script {
                    sh 'source venv/bin/activate && python optimize_pipeline.py'
                }
            }
        }

        stage('Train Anomaly Detection Model') {
            steps {
                script {
                    sh 'source venv/bin/activate && python train_anomaly_model.py'
                }
            }
        }

        stage('Run DevOps AI Workflow') {
            steps {
                script {
                    sh 'source venv/bin/activate && python devops_ai.py'
                }
            }
        }

        stage('Send Logs to Azure Monitoring') {
            steps {
                script {
                    def logs = sh(script: 'cat jenkins.log', returnStdout: true).trim()
                    def response = sh(script: """
                        curl -X POST "$AZURE_API_URL" \
                        -H "Content-Type: application/json" \
                        -d '{"logs": "${logs}"}'
                    """, returnStdout: true).trim()
                    
                    echo "Azure Monitoring Response: ${response}"
                }
            }
        }
    }

    post {
        always {
            sh 'deactivate'
        }
    }
}

