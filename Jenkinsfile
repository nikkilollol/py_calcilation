pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest -s -v ./calculation/tests/test_calc.py'
            }
        }
         stage('Deploy') 
            }
        }
    }
}
