pipeline {
    agent any

    stages {
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

        stage('Train Model') {
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
    }
}
