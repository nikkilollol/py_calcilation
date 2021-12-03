pipeline {
        agent any

        stages {
            stage('Build') {
                steps {
                    echo 'Building..'
                }
            }
        stage('Test') {
          steps (
              sh 'pytest -s -v ./calculation/tests/test_calc.py'
          )
        }
        stage('Deploy')  (
            when {
                    expression {
                      currentBuild.result == null || currentBuild.result == 'SUCCESS'
                    }       
                 }
                 steps {
                     sh 'cp -R src/* /var/jenkins_home/${GIT_BRANCH}'
                 }
}
