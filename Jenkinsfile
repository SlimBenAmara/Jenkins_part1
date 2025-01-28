pipeline {
  agent any
  stages {
    stage('Install dependencies') {
      steps {
        //bat 'python -m pip install --upgrade pip'  // Assurer que pip est à jour
        //bat 'python -m pip install pandas'  // Installer pandas en utilisant python -m pip
        //bat 'python -m pip install numpy' 
        bat 'python -c "import numpy'
        bat 'python -c "import pandas; print(pandas.__version__)"'  // Vérifier l'installation de pandas
      }
    }
    stage('version') {
      steps {
        bat 'python --version'  // Vérifier la version de Python
      }
    }
    stage('Scripts executions') {
      steps {
        script {
          def helloOutput = bat(script: 'python hello.py', returnStdout: true).trim()
          withEnv(["RESULT=${helloOutput}"]) {
            bat 'python script2.py'
          }
        }
      }
    }
  }
}
