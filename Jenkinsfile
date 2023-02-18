node {
    stage("Checkout"){
        checkout([
        $class: 'GitSCM',
        branches: [["name":"origin/master"]],
        doGenerateSubmoduleConfigurations: scm.doGenerateSubmoduleConfigurations,
        extensions: scm.extensions,
        userRemoteConfigs: [["url": "https://github.com/ksprakash/python_jenkins"]],
        depth: 1
    ])
        
    }
    stage("ChangeLog"){
    def changeSet = currentBuild.changeSets
    println changeSet.size()
        for(int i=0; i < changeSet.size();i++){
            println changeSet[i].getClass().getName()
            def entries = changeSet[i].items
            println entries
            for (int j=0; j < entries.length; j++){
                def entry = entries[j]
                println entry
                println "msg: " + entry.msg
    }
    }
    }
    stage("Build"){
      //  ws("/var/jenkins_home/workspace/customizedWorkspace"){
        def workspace = pwd()
        println "WorkSPace" + ":" +workspace
      //  docker.withRegistry('https://registry-1.docker.io','docker-credentials'){
        def image = docker.build("vijayasurya/python:v2.2")
        image.inside('-e astage=Dev',{
            sh "pwd"
          
            sh 'echo "Stage: $astage"'
            
        })
      //  }
     //   }
    }
}
