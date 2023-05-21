# Jenkins


### Install jenkins
```
docker run -p 8000:8000 -p 5000:5000 -d --name jenkins -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts


docker exec -u 0 -it jenkins bash  # login as a root


docker run -p 8080:8080 -p 5000:5000 -d -v jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock -v $(which docker):/usr/bin/docker jenkins/jenkins:lts



```

* be sure the time of jenkins-server and jenkins-runner must be sync.


### By default, Jenkins stores all of its data in this directory on the file system
* /var/lib/jenkins
* /home/jenkins



# important directory in jenkins
* /var/lib/jenkins/jobs
* /var/lib/jenkins/workspace

# number of executers
* never have the number of executers exceed the number of CPUS or vcpus available on the agent.

## list of env variable: 
* http://IP:port/env-vars.html/