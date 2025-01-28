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
          // Capture the output of hello.py, excluding the command prompt and non-CSV output
          def helloOutput = bat(script: 'python hello.py', returnStdout: true).trim()
          
          // Debugging: echo the captured output to make sure it's just the CSV string
          echo "Captured helloOutput: ${helloOutput}"
          
          // Set the environment variable RESULT with the DataFrame CSV string
          withEnv(["RESULT=${helloOutput}"]) {
            // Call script2.py to read the RESULT environment variable
            bat 'python script2.py'
          }
        }
      }
    }
  }
}
