pipeline {
    agent any

    environment {
        PYTHON_VERSION = "3.10"
        AZURE_API_URL = "http://your-azure-api-url/detect"  // Replace with your actual API URL
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/your-repo.git' // Replace with your Git repo
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                script {
                    sh '''
                    cd /var/lib/jenkins/workspace/azure-cicd
                    if [ ! -d "venv" ]; then
                        python3 -m venv venv
                    fi
                    '''
                }
            }
        }

        stage('Activate Virtual Environment & Install Dependencies') {
            steps {
                script {
                    sh '''
                    cd /var/lib/jenkins/workspace/azure-cicd
                    /bin/bash -c "source venv/bin/activate && pip install -r requirements.txt"
                    '''
                }
            }
        }

        stage('Run Optimize Pipeline') {
            steps {
                script {
                    sh '''
                    cd /var/lib/jenkins/workspace/azure-cicd
                    /bin/bash -c "source venv/bin/activate && python optimize_pipeline.py"
                    '''
                }
            }
        }

        stage('Train Anomaly Detection Model') {
            steps {
                script {
                    sh '''
                    cd /var/lib/jenkins/workspace/azure-cicd
                    /bin/bash -c "source venv/bin/activate && python train_anomaly_model.py"
                    '''
                }
            }
        }

        stage('Verify Model Files') {
            steps {
                script {
                    sh '''
                    cd /var/lib/jenkins/workspace/azure-cicd
                    if [ -f anomaly_detector.pkl ] && [ -f scaler.pkl ]; then
                        echo "✅ Model files exist!"
                    else
                        echo "❌ Model files missing!"
                        exit 1
                    fi
                    '''
                }
            }
        }

        stage('Run DevOps AI Workflow') {
            steps {
                script {
                    sh '''
                    cd /var/lib/jenkins/workspace/azure-cicd
                    /bin/bash -c "source venv/bin/activate && python devops_ai.py"
                    '''
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
