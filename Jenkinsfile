pipeline {
    agent any

    environment {
        PYTHON_VERSION = "3.10"
        AZURE_API_URL = "http://your-azure-api-url/detect"  // Replace with actual Azure API URL
        WORKSPACE_DIR = "/var/lib/jenkins/workspace/azure-cicd"
    }

    stages {
        stage('Setup Virtual Environment') {
            steps {
                dir("$WORKSPACE_DIR") {
                    script {
                        sh '''
                        if [ ! -d "venv" ]; then
                            python3 -m venv venv
                        fi
                        '''
                    }
                }
            }
        }

        stage('Activate Virtual Environment & Install Dependencies') {
            steps {
                dir("$WORKSPACE_DIR") {
                    script {
                        sh '''
                        /bin/bash -c "source venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt"
                        '''
                    }
                }
            }
        }

        stage('Run Optimize Pipeline') {
            steps {
                dir("$WORKSPACE_DIR") {
                    script {
                        sh '''
                        /bin/bash -c "source venv/bin/activate && python optimize_pipeline.py"
                        '''
                    }
                }
            }
        }

        stage('Train Anomaly Detection Model') {
            steps {
                dir("$WORKSPACE_DIR") {
                    script {
                        sh '''
                        /bin/bash -c "source venv/bin/activate && python train_anomaly_model.py"
                        '''
                    }
                }
            }
        }

         stage('Train Anomaly Detection Model') {
            steps {
                dir("$WORKSPACE_DIR") {
                    script {
                        sh '''
                        /bin/bash -c "source venv/bin/activate && python monitor_cpu.py"
                        '''
                    }
                }
            }
        }

        stage('Verify Model Files') {
            steps {
                dir("$WORKSPACE_DIR") {
                    script {
                        sh '''
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
        }

        stage('Run DevOps AI Workflow') {
            steps {
                dir("$WORKSPACE_DIR") {
                    script {
                        sh '''
                        /bin/bash -c "source venv/bin/activate && python devops_ai.py"
                        '''
                    }
                }
            }
        }

        stage('Send Logs to Azure Monitoring') {
            steps {
                dir("$WORKSPACE_DIR") {
                    script {
                        def logs = sh(script: 'cat jenkins.log | jq -Rs .', returnStdout: true).trim()
                        def response = sh(script: """
                            curl -X POST "$AZURE_API_URL" \
                            -H "Content-Type: application/json" \
                            -d '{"logs": $logs}'
                        """, returnStdout: true).trim()

                        echo "Azure Monitoring Response: ${response}"
                    }
                }
            }
        }
    }

    post {
        always {
            dir("$WORKSPACE_DIR") {
                sh '''
                /bin/bash -c "source venv/bin/activate && deactivate"
                '''
            }
        }
    }
}
