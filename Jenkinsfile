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
              sh 'pip install -r ./calculation/requirements.txt'
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
