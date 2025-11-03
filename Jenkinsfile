// pipeline {
//     agent any // Runs on the built-in Windows node

//     stages {
//         stage('Checkout') {
//             steps {
//                 echo 'Checking out code...'
//                 git branch: 'main', url: 'https://github.com/SamyuktaNair/Python_jenkins.git'
//             }
//         }

//         stage('Setup Environment') {
//             steps {
//                 echo 'Setting up Python Venv and installing dependencies...'
//                 // Use 'bat' for Windows commands
//                 bat '''
//                 // 1. Create venv using 'python' (instead of python3)
//                 python -m venv venv
                
//                 // 2. Activate venv and install requirements (Windows path)
//                 venv\\Scripts\\activate.bat & pip install -r requirements.txt
//                 '''
//             }
//         }

//         stage('Run Selenium Tests') {
//             steps {
//                 echo 'Executing tests...'
//                 // Use 'bat' for Windows commands
//                 bat '''
//                 // 1. Activate venv (Windows path)
//                 venv\\Scripts\\activate.bat & 
                
//                 // 2. Run pytest with output to report.xml
//                 pytest --maxfail=1 --disable-warnings -q --junitxml=report.xml
//                 '''
//             }
//         }

//         stage('Publish Results') {
//             steps {
//                 echo 'Publishing results to Jenkins...'
//                 junit 'report.xml'
//             }
//         }
//     }
// }

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                // FIX C: Use the repository URL linked to this job (Vansh-Sutaria/PythonJenkins)
                // Using 'checkout scm' is the best practice here.
                checkout scm 
            }
        }

        stage('Setup Environment') {
            steps {
                echo 'Setting up Python Venv and installing dependencies...'
                // FIX A: Removed all '//' comments.
                // FIX B: We rely on the 'python' executable being in PATH or using 'py' (Windows Python Launcher).
                // If 'python' fails, try replacing all 'python' commands with 'py'
                bat '''
                python -m venv venv
                venv\\Scripts\\activate.bat & pip install -r requirements.txt
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo 'Executing tests...'
                // FIX A: Removed all '//' comments.
                bat '''
                venv\\Scripts\\activate.bat & 
                pytest --maxfail=1 --disable-warnings -q --junitxml=report.xml
                '''
            }
        }

        stage('Publish Results') {
            steps {
                echo 'Publishing results to Jenkins...'
                // Pytest creates the file, we just publish it.
                junit 'report.xml'
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        success {
            echo '✅ Pipeline finished: SUCCESS!'
        }
        failure {
            echo '❌ Pipeline finished: FAILED. Check logs.'
        }
    }
}
