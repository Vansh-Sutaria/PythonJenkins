pipeline {
    agent any // Runs on the built-in Windows node

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                git branch: 'main', url: 'https://github.com/SamyuktaNair/Python_jenkins.git'
            }
        }

        stage('Setup Environment') {
            steps {
                echo 'Setting up Python Venv and installing dependencies...'
                // Use 'bat' for Windows commands
                bat '''
                // 1. Create venv using 'python' (instead of python3)
                python -m venv venv
                
                // 2. Activate venv and install requirements (Windows path)
                venv\\Scripts\\activate.bat & pip install -r requirements.txt
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo 'Executing tests...'
                // Use 'bat' for Windows commands
                bat '''
                // 1. Activate venv (Windows path)
                venv\\Scripts\\activate.bat & 
                
                // 2. Run pytest with output to report.xml
                pytest --maxfail=1 --disable-warnings -q --junitxml=report.xml
                '''
            }
        }

        stage('Publish Results') {
            steps {
                echo 'Publishing results to Jenkins...'
                junit 'report.xml'
            }
        }
    }
}