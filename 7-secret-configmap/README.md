# configmap and secrets
```

# configmap 
kubectl create configmap config_name --from-literal=APP_COLOR=blue
kubectl create configmap app-config2 --from-literal="APP_COLOR=blue" --from-literal=APP=4


kubectl create configmap config_name --from-file=<path-to-file>

# declaritive way
apiVersion: v1
kind: ConfigMap
metadata:
  name: myapp-config
data:
  db_data: mysql-service
  db_port: 3306



# secret

kubectl create secret generic secret_name --from-literal=DB_Host=mysql --from-literal=DB_Pass=pass


echo username | base64
echo bXl1c2Vy | base64 -d
echo -n "bXl1c2Vy" | base64 -d
```