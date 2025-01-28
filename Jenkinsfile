pipeline {
  agent any
  stages {
    stage('test message') { 'print("just testing")'}
    stage('version') {
    steps {
        bat 'python --version'  // Utilise 'python' au lieu de 'python3' sur Windows
    }
    }
    stage('hello') {
      steps {
        bat 'python3 hello.py'
      }
    }
  }
}
