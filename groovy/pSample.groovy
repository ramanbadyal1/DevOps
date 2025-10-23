pipeline {
  agent none                       // top-level: no single agent; set per-stage/branch
  options {
    timestamps()
    ansiColor('xterm')
    buildDiscarder(logRotator(numToKeepStr: '20'))
  }
  environment {
    APP_NAME = "my-app"
    // Example: replace with real credentials IDs if used
    // SSH_KEY = credentials('deploy-ssh-key')
  }

  stages {
    stage('Prepare') {
      // run on controller (or a label you choose)
      agent { label 'master' }
      steps {
        checkout scm
        script {
          // Demonstrate Groovy implicit parameter `it` with a simple list
          def envs = ['dev', 'qa', 'prod']
          // prints: Environment: dev  (and so on)
          envs.each { echo "Environment: ${it}" }   // <-- use of `it` (implicit param)
        }
      }
    }

    stage('Parallel Build & Test') {
      // run builds in parallel on different agent labels
      parallel {
        stage('Build on Linux') {
          agent { label 'linux' }
          steps {
            script {
              sh 'uname -a || true'
              sh 'echo building on linux...'
              sh 'mkdir -p build && echo "linux-binary" > build/app.bin'
              stash name: 'app-linux', includes: 'build/**'
            }
          }
          post {
            always {
              junit allowEmptyResults: true, testResults: 'build/test-results-*.xml'
            }
          }
        }

        stage('Build on Windows') {
          agent { label 'windows' }
          steps {
            script {
              // On a Windows agent we'd use bat; include a guard to avoid failure on non-windows controller
              if (isUnix()) {
                echo "Simulating windows build on Unix agent (for demo only)"
                sh 'mkdir -p build && echo "windows-binary" > build/app.exe'
              } else {
                bat 'echo building on windows...'
                bat 'mkdir build 2>nul || true'
                bat 'echo windows-binary > build\\app.exe'
              }
              stash name: 'app-windows', includes: 'build/**'
            }
          }
        }

        stage('Build on Mac') {
          agent { label 'mac' }
          steps {
            script {
              sh 'echo building on mac...'
              sh 'mkdir -p build && echo "mac-binary" > build/app.mac'
              stash name: 'app-mac', includes: 'build/**'
            }
          }
        }
      } // end parallel
    } // end stage

    stage('Aggregate & Test') {
      agent { label 'master' }   // aggregation on master (or a specific reporting node)
      steps {
        script {
          // Unstash whichever artifacts exist and run a lightweight integration check
          def possibleStashes = ['app-linux', 'app-windows', 'app-mac']
          // filter only stashes that exist: we attempt to unstash inside try/catch
          def available = []
          possibleStashes.each { // use `it` again as implicit param
            def s = it
            try {
              unstash s
              available << s
            } catch (e) {
              echo "Stash ${s} not found (skipping)."
            }
          }

          echo "Available builds: ${available}"

          // Example: list files we have and show the use of `it`
          def files = sh(script: "ls -1 build || true", returnStdout: true).trim().split("\n").findAll{ it }
          if (files) {
            echo "Files in build/:"
            files.each { echo "  - ${it}" }   // `it` used as the file name inside closure
          } else {
            echo "No build files present (possibly simulated environment)."
          }

          // Placeholder: run integration tests (simulate)
          sh '''
            mkdir -p test-results
            echo "<testsuite></testsuite>" > test-results/results.xml
          '''
          junit testResults: 'test-results/*.xml', allowEmptyResults: true
        }
      }
    }

    stage('Deploy to QA (one of available agents)') {
      // Example: choose available agent dynamically (just demonstration)
      agent { label 'linux' }
      steps {
        script {
          // choose which artifact to deploy: prefer linux, else windows, else mac
          def preferredOrder = ['app-linux', 'app-windows', 'app-mac']
          def chosen = preferredOrder.find { stashName ->
            // try unstash inside try/catch and if successful, set chosen
            try {
              unstash stashName
              echo "Selected artifact: ${stashName}"
              return true   // find stops at first true
            } catch (err) {
              echo "No ${stashName}, continuing search..."
              return false
            }
          }
          if (!chosen) {
            error "No artifacts available to deploy!"
          }

          // deploy (simulated)
          sh 'echo Deploying artifact to QA...'
          // demonstrate use of a map and `it` inside a each loop
          def servers = [ 'qa-1.company.local', 'qa-2.company.local' ]
          servers.each { echo "Notifying server ${it} about new deploy" }  // `it` used again
        }
      }
    }
  } // end stages

  post {
    always {
      echo "Pipeline finished. Cleaning workspace..."
      cleanWs()
    }
    success {
      echo "SUCCESS: Pipeline completed."
    }
    failure {
      echo "FAILURE: Something went wrong."
    }
  }
} // end pipeline
