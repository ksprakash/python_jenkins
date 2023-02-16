 pipeline {
    agent any
    stages {

    stage('Prep') {
            steps {
                script {
                   println "This is the Prep stage"
                }
            }
    }
    docker.image('httpd').inside {

        sh "ls -la"
        sh "hostname"
    }
 }
 }