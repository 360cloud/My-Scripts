pipeline {
  agent any
  stages {
    stage('auto deployment') {
      steps {
        parallel(
          "auto deployment": {
            sh 'echo $HOSTNAME'
            
          },
          "SIT Deployment": {
            echo 'SIT Environment'
            
          },
          "Pre-Prod Deployment": {
            input(message: 'Production Deployment', id: 'a464508', ok: 'Deploy')
            
          }
        )
      }
    }
  }
  environment {
    VERSION = '1.0.0'
  }
}