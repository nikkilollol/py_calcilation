pipeline {
        agent any

        stages {
            stage('Build') {
                steps {
                    echo 'Building..'
                    echo "Running $(env.BUILD_ID) $(env.BUID_DISPLAY_NAME) on $(env.NODE_NAME) and JOB $(env.JOB_NAME)
                }
            }
        stage('Test') {
          steps (
              sh 'python3 test_calc.py'
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
