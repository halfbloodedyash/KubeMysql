# KubeMysqlOperator
[![N|Solid](https://i.postimg.cc/Pf2jxZ1F/1-Pbb5rmrwh-e-AFWXd8ws79-A.png)](https://kubernetes.io/)

## _"Streamline MySQL in Kubernetes : Simplify. Automate. Scale."_


KubeMySQLOperator is a Kubernetes operator designed to streamline MySQL management within Kubernetes clusters by automating deployment, configuration, and scaling tasks. It simplifies database operations by providing seamless provisioning of MySQL instances as stateful sets with attached persistent volumes and manages configurations while ensuring reliability and consistency through logical updates.hat

## Problems
- Creating MySQL as a stateful set with attached persistent volume
- Managing MySQL configurations using the operator
- Creating two Kubernetes services: one with a cluster IP and the other as a headless service
- Updating MySQL stateful-set and configuration from the operator using a logical approach.
## Features

- Automated Deployment: Provision MySQL instances as stateful sets with attached persistent volumes, simplifying the deployment process.
- Service Creation: Automatically create Kubernetes services for accessing MySQL databases, including both cluster IP and headless services.
- Configuration Management: Manage MySQL configurations such as tuning parameters and replication settings directly from the operator.
- Logical Updates: Enable seamless updates to MySQL stateful sets and configurations using a logical approach to maintain reliability and consistency.
- Scalability: Easily scale MySQL instances within Kubernetes clusters to meet changing demands without manual intervention.
- Monitoring : Integrate monitoring functionality to provide visibility into the health and performance of MySQL databases.
- Customization: Allow customization of deployment and configuration options to cater to specific use cases and requirements.
- Security: Enhance security by implementing best practices for securing MySQL deployments within Kubernetes environments.
- Documentation and Support: Provide comprehensive documentation and support resources to assist users in deploying, configuring, and troubleshooting the operator.
- Backup Management: Facilitate automated backups of MySQL databases, enabling users to schedule and manage backup tasks directly from the operator.
- Configuration Flexibility: Offer flexibility in configuring MySQL instances, allowing users to customize parameters and settings according to their specific requirements.
- Testing Integration: Integrate testing functionalities to validate the integrity and performance of MySQL deployments, ensuring reliability and stability.

## Prerequisites
- First requirement is to download Kubernetes
```sh
https://kubernetes.io/releases/download/
```
  
- Test and ensure the version of installed Kubernetes using this command:
```sh
kubectl --version client
```
- Second prerequisite is Minikube
```sh
https://minikube.sigs.k8s.io/docs/start/
```
- Install Docker (Prerequisities of Minikube. (Install Docker from https://docs.docker.com/get-docker/)
```sh
https://docs.docker.com/get-docker/
```
- Use the following command to start Minikube.
```sh
minikube start 
```
- Minikube comes with a dashboard. To open dashboard type this command.
```sh
minikube dashboard
```
- Minikube dashboard should open on your default browser.
![N|Solid](https://i.postimg.cc/59nbYwKj/Screenshot-from-2024-02-16-03-28-58.png)


#  Installation of MySQL Operator for Kubernetes
#### Leveraging Manifest Files with kubectl
First we need to deploy the Custom Resource Definition (CRDs):
```sh
 kubectl apply -f https://raw.githubusercontent.com/halfbloodedyash/KubeMysql/main/deploy-crds.yaml
```
Then deploy MySQL Operator for Kubernetes:
```sh
 kubectl apply -f https://raw.githubusercontent.com/halfbloodedyash/KubeMysql/main/sql_operator.yaml
```
![N|Solid](https://dev.mysql.com/doc/refman/8.0/en/images/innodb_cluster_overview.png)

Verify the operator is running by checking the deployment inside the mysql-operator namespace:
```sh
kubectl get deployment -n mysql-operator mysql-operator
```
[![N|Solid](https://i.postimg.cc/8c0M02ZY/Screenshot-from-2024-02-16-03-09-31.png)]

# MySQL InnoDB Cluster Installation
#### Using kubectl
```sh
 kubectl create secret generic mypwds \
        --from-literal=rootUser=root \
        --from-literal=rootHost=% \
        --from-literal=rootPassword="root"
```
#### Define your MySQL InnoDB Cluster, which references the secret. For example:
We will create a Yaml file named accordingly and paste this into it
```sh
apiVersion: mysql.oracle.com/v2
kind: InnoDBCluster
metadata:
  name: mycluster
spec:
  secretName: mypwds
  tlsUseSelfSigned: true
  instances: 3
  router:
    instances: 1
```
#### Assume it's saved as mycluster.yaml, deploy it:

```sh
kubectl apply -f mycluster.yaml
```
##### This example sets up an InnoDB Cluster comprising three MySQL Server instances and one MySQL Router instance. You can monitor the entire process by:
```sh
kubectl get innodbcluster --watch
```
![N|Solid](https://i.postimg.cc/5NDBJFVk/Screenshot-from-2024-02-16-03-34-16.png)

## Connecting to MySQL InnoDB Cluster
###### A MySQL InnoDB Cluster Service is created inside the Kubernetes cluster:
```sh
 kubectl get service mycluster
 ```
 ![N|Solid](https://i.postimg.cc/vZbQ4b5L/Screenshot-from-2024-02-16-03-42-59.png)
 #### To check Persistent Volumes and Persistent Volume Claims
 ![N|Solid]( https://i.postimg.cc/vZyxzRw3/Screenshot-from-2024-02-16-03-54-35.png)
 #### Use this Command to execute Mysql on Kubernetes
 ```sh
 kubectl exec -it <Your_Pod_Name> -- mysql -u root -p
```
![N|Solid](https://i.postimg.cc/0Qv8gvZB/Screenshot-from-2024-02-16-04-01-18.png)
![N|Solid](https://i.postimg.cc/9FLLkb0y/Screenshot-from-2024-02-16-06-40-17.png)

#### Headless_Service.yaml
![N|Solid](https://i.postimg.cc/2yGKC2K4/Screenshot-from-2024-02-16-05-24-42.png
)

#### All Services

![N|Solid](https://i.postimg.cc/jq3zv90G/hhh.jpg)

#### Using Port Forwarding
```sh
kubectl port-forward service/mycluster mysql
```
![N|Solid](https://i.postimg.cc/LsKxVsgC/portforwarding.jpg)


# MySQL Management Script

This Python script provides functionalities for managing a MySQL database running in Kubernetes. It utilizes subprocess to execute various commands related to backup, configuration management, rolling updates, testing, and monitoring.

## Features

- **Backup Data**: Performs a MySQL backup using mysqldump and writes the backup to a file named `backup.sql`.
- **Update Configuration**: Placeholder function for updating configuration. You can replace it with actual commands as per your requirements.
- **Rolling Update**: Triggers a rolling update for the StatefulSet managing MySQL.
- **Configuration Management**: Checks the MySQL configuration within Pods.
- **Testing**: Conducts various tests such as selection, CRUD operations, and replication verification.
- **Monitoring**: Retrieves the list of MySQL Pods and checks their status.

## Prerequisites

- Python 3.x
- MySQL client tools installed
- kubectl configured to access the Kubernetes cluster

## Usage

. Ensure that Python and required dependencies are installed.
. Configure access to the Kubernetes cluster using `kubectl`.
. Modify the script if necessary to fit your environment.
. Execute the script using Python.

```bash
python /Automation.py
```
![N|Solid](https://i.postimg.cc/yNJwV5tm/Screenshot-from-2024-02-16-06-39-41.png)





