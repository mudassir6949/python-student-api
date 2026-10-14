
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Python Student API source code is ready'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Build') {
            steps {
                echo 'Building Python Student API'
            }
        }
    }
}
