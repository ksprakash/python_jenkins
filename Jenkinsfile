 pipeline {
    agent any
    stages {

    stage('Prep') {
            steps {
                script {
                    GIT_VARS = checkout([
                            $class                           : 'GitSCM',
                            branches                         : scm.branches,
                            doGenerateSubmoduleConfigurations: false,
                            extensions                       : scm.extensions + [
                                    [$class: 'CleanBeforeCheckout'],
                                    [$class: 'SubmoduleOption', disableSubmodules: false, recursiveSubmodules: true, reference: '', trackingSubmodules: false],
                                    [$class: 'RelativeTargetDirectory', relativeTargetDir: 'NewProjectName']
                            ],
                            submoduleCfg                     : [],
                            userRemoteConfigs                : scm.userRemoteConfigs])

                    releaseTools = release.configure(scm: GIT_VARS, credentialsId: 'github-credentials')
                }
            }
    }
 }
 }