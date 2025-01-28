pipeline {
  agent any
  stages {
    stage('Install dependencies') {
      steps {
        bat 'pip install pandas'  // Installer pandas
        bat 'python -c "import pandas; print(pandas.__version__)"'  // Vérifier l'installation de pandas
      }
    }
    stage('version') {
      steps {
        bat 'python --version'  // Vérifier la version de Python
      }
    }
    stage('hello') {
      steps {
        bat 'python hello.py'  // Exécuter ton script Python
      }
    }
  }
}
