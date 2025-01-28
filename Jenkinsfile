pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python --version'  // Remplace 'python3' par 'python' sur Windows
      }
    }
    stage('hello') {
      steps {
        bat 'python hello.py'  // Remplace 'python3' par 'python' pour exécuter ton script
      }
    }
  }
}
