pipeline {
  agent {
    node {
      label 'dockercli-slave'
    }
    
  }
  stages {
    stage('build') {
      steps {
        sh 'docker build -t hello:0.0.1 .'
      }
    }
    stage('test') {
      steps {
        parallel(
          "run": {
            sh 'docker run -d --network=build-network --ip=172.25.1.1 --name hello hello:0.0.1'
            
          },
          "test": {
            sh 'curl -f -I http://172.25.1.1:5555'
            sh 'docker kill hello'
            sh 'docker rm hello'
            
          }
        )
      }
    }
    stage('deploy') {
      steps {
        parallel(
          "deploy": {
            sh 'docker run -d --network=build-network --ip=172.25.1.1 --name hello hello:0.0.1'
            
          },
          "prod-test": {
            sh 'curl -I -f http://172.25.1.1:5555'
            sh 'docker kill hello'
            sh 'docker rm hello'
            
          }
        )
      }
    }
  }
}