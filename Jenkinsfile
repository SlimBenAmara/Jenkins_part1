pipeline {
  agent any
  stages {
    stage('version') {
    steps {
        bat 'python --version'  // Utilise 'python' au lieu de 'python3' sur Windows
    }
    }
    stage('hello') {
      steps {
        bat 'python hello.py'
      }
    }
  }
}
