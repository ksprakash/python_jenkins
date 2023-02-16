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
                                    [$class: 'RelativeTargetDirectory', relativeTargetDir: projectName]
                            ],
                            submoduleCfg                     : [],
                            userRemoteConfigs                : scm.userRemoteConfigs])

                    releaseTools = release.configure(scm: GIT_VARS, credentialsId: USERPASS_GITHUB_ID)
                }
            }
    }
 }