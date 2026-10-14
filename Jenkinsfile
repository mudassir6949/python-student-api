
stage('Install Dependencies') {
    steps {
        sh '''
            docker run --rm \
              -v "$WORKSPACE:/app" \
              -w /app \
              python:3.13-slim \
              sh -c "python -m pip install --upgrade pip && python -m pip install -r requirements.txt"
        '''
    }
}
