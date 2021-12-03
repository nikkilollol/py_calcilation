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
              sh 'echo "Hello'
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
