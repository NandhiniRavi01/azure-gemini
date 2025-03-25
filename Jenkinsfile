pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                script {
                    sh '''
                    cd /var/lib/jenkins/workspace/azure-cicd
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Train Model') {
            steps {
                script {
                    sh '''
                    source venv/bin/activate
                    rm -f anomaly_detector.pkl scaler.pkl  # Delete old models
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
