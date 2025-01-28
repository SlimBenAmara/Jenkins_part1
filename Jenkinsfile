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
    stage('version') {
      steps {
        bat 'python --version'
      }
    }
    stage('Scripts executions') {
      steps {
        script {
          // Capture the output of hello.py
          def helloOutput = bat(script: 'python hello.py', returnStdout: true).trim()
          
          // Clean the helloOutput to remove command and only keep the CSV data
          // Split the output by lines, remove any lines that don't contain CSV data, and rejoin the CSV data
          def csvData = helloOutput.split("\n").findAll { it.contains(",") }.join("\n")
          
          // Debugging: echo the cleaned CSV data to ensure it's valid
          echo "Captured and cleaned CSV data: ${csvData}"
          
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
