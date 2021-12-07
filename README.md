This project in git contain three branches: 
1.Feature branch where each developer write feautures and merge them to develop branch
2.Develop branch where approvers review and approve code. After their approve this branch merges to main branch - master branch.
3.Master branch with the latest and approved version of code which is work with Jenkins. 
Сode is passed to jenkins with Jenkinsfile which contain instructions for the pipeline stages: build, test and deploy.
If status of the test is success - our code deloing to diffirent enviroments - dev, uat and prodaction.


