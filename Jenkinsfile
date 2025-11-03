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

    // FIX: Define the executable path in the environment block
    environment {
        // This is now correctly defined at the pipeline level
        PYTHON_EXECUTABLE = "C:\\Users\\Vansh\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                checkout scm 
            }
        }

        stage('Setup Environment') {
            steps {
                echo 'Setting up Python Venv and installing dependencies...'
                
                // Now we reference the environment variable, which works inside 'bat'
                bat """
                // 1. Create venv using the absolute path from the environment block
                "${env.PYTHON_EXECUTABLE}" -m venv venv
                
                // 2. Install dependencies using the venv's pip executable
                venv\\Scripts\\activate.bat & venv\\Scripts\\pip.exe install -r requirements.txt
                """
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo 'Executing tests....'
                // CORRECTION: Ensure pytest.exe is on the next line or chained with '&'
                bat """
                venv\\Scripts\\activate.bat & venv\\Scripts\\pytest.exe --maxfail=1 --disable-warnings -q --junitxml=report.xml
                """
            }
        }

        stage('Publish Results') {
            steps {
                echo 'Publishing results to Jenkins...'
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
