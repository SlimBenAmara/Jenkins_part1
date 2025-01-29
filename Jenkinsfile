pipeline {
  agent any
  stages {
    stage('Install dependencies') {
      steps {
        bat 'python -m pip install --upgrade pip'
        bat 'python -m pip install pandas'
        bat 'python -m pip install numpy'
        bat 'python -c "import pandas; print(pandas.__version__)"'
      }
    }

    stage('Scripts executions') {
      steps {
        script {
          // Capture the output of hello.py
          def csvData = bat(script: 'python hello.py', returnStdout: true)
 
          // Set the environment variable RESULT with the cleaned CSV data
          withEnv(["RESULT=${csvData}"]) {
            // Call script2.py to read the RESULT environment variable
            bat 'python script2.py'
          }
        }
      }
    }
  }
}
