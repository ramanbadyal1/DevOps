pipeline {
  agent any

  environment {
    REPO_URL = 'https://github.com/<your-username>/<your-repo>.git'
    BRANCH   = 'main'
  }

  stages {

    stage('Checkout') {
      steps {
        echo "Cloning repository from ${REPO_URL}..."
        // This automatically checks out the specified branch
        git branch: "${BRANCH}", url: "${REPO_URL}"
      }
    }

    stage('Build') {
      steps {
        script {
          // Example: run build depending on your project type
          // For Node.js:
          if (fileExists('package.json')) {
            sh 'npm install'
            sh 'npm run build'
          }
          // For Python:
          else if (fileExists('requirements.txt')) {
            sh 'pip install -r requirements.txt'
          }
          // For Java:
          else if (fileExists('pom.xml')) {
            sh 'mvn clean package -DskipTests'
          } else {
            echo "No recognized build file found — skipping build."
          }
        }
      }
    }

    stage('Test') {
      steps {
        script {
          if (fileExists('package.json')) {
            sh 'npm test || true'  // continue even if tests fail
          } else if (fileExists('pom.xml')) {
            sh 'mvn test || true'
          } else {
            echo "No test stage defined for this project."
          }
        }
      }
    }

    stage('Run Application') {
      steps {
        script {
          echo "Running code from repository..."
          // Example: run depending on project
          if (fileExists('package.json')) {
            sh 'npm start &'
          } else if (fileExists('app.py')) {
            sh 'python3 app.py &'
          } else if (fileExists('target/*.jar')) {
            sh 'java -jar target/*.jar &'
          } else {
            echo "No runnable file detected."
          }
        }
      }
    }
  }

  post {
    success {
      echo "✅ Pipeline completed successfully!"
    }
    failure {
      echo "❌ Pipeline failed. Check logs above."
    }
  }
}
