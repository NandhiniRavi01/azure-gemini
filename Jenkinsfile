pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                script {
                    sh '''
                    cd /var/lib/jenkins/workspace/azure-cicd
                    python3 -m venv venv
                    . venv/bin/activate  # Use "." instead of "source"
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Train Model') {
            steps {
                script {
                    sh '''
                    . venv/bin/activate  # Activate venv
                    rm -f anomaly_detector.pkl scaler.pkl  # Remove old models
                    python train_anomaly_model.py
                    '''
                }
            }
        }

        stage('Verify Model Files') {
            steps {
                script {
                    sh '''
                    if [ -f anomaly_detector.pkl ] && [ -f scaler.pkl ]; then
                        echo "✅ Model files exist!"
                    else
                        echo "❌ Model files not found!"
                        exit 1
                    fi
                    '''
                }
            }
        }
    }
}
