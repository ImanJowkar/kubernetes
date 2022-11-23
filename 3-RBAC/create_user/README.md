## generate private key and csr

```
openssl genrsa -out user-jack.key 2048 # generate private key
openssl req -new -key user-jack.key -subj "/CN=jack" -out user-jack.csr
```

## create CSR yaml file 
```
cat user-jack.csr | base64 | tr -d "\n"
```

## create csr yaml file

```
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: user-jack
spec:
  request: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS0KTUlJQ1V6Q0NBVHNDQVFBd0RqRU1NQW9HQTFVRUF3d0RkRzl0TUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQwpBUThBTUlJQkNnS0NBUUVBcGhWZFlkNmYvd3VhanQyUitaYVArV0xnaHBXbDJVS1ZFM01OZjlqNWtMbHJlaEZNCi9TeEdjdjRpcUo5djBmUEppTVVRNXhhK21uSzZBdGZrZ1publlyM0JvM2YvTGgxMEkvR3ZITEU4dXZ5RUFWSzUKUGhkMHZHODhYS2FJd1VYVWlsaWFES0tQQ3NkNm5QbjFiM1lqZWd2MlczRjdEd1c2MmRnbng5MUVvUGI0a1IwdAowTnpzcm1SWEtQeHZ5cVFwdjFLYXpUMHVQY0VBQnRPUGZWZ05LNjhvV0lPb1FmZ2Nlb2FHRlhNUkQ1NVZCa01kClE5Ly9jMlJEZ1RHOEVFcjFmRUN3TFU2c09abHVKWFpQazhZcjQzdXZJOVpBekQyVFhpd3BzcUY2OWlaZ1NzMTMKTGZoQTVaVWRqN2xpOWJMNlBSWWtjN1JIOEcvbUhkUU5SZTRZUHdJREFRQUJvQUF3RFFZSktvWklodmNOQVFFTApCUUFEZ2dFQkFCTHBtb1AxSjVFY0ludmhIMWNISXV0QkRlTmxROEFiclU0cXpLb0FiQ2JGZ1ljZ1plTmtxWkc1ClF1UURKWGVZc2ZERDIxbnhaYjdrTG5uRVNLenViOHNtcUFiOVd5VHZUakJQUnRjY05lNWN0aVhKSVhDR2lLMC8KeERpUXMzSDNtWXlmb2U1aHVyMGM3Mm5ESGFWNHhTYVk4UkdTWlo3ZzBNTSt2WDdyS2NkYWpwckpKdnhIa0laZQpBeE96K1lhQ2grTndqM2piNWMzZUJMVzlYVEFNVFR3WVRBdStYVFlVc1FWNXNUcHlLVHo2dXFnbStyaWpQS1BuCnRRQ2JaS3VQaW9DdVJMNnNwZGxwM1hDdC8yVnUwNE43UzNtZ2RwdXcxSzJCVVNxY0NiNWxpdXQzOXY2SzlmMzcKVWM1OVRMNW5sK2hmU3pkRXh6WmYrVE5CMTB5Z3pKND0KLS0tLS1FTkQgQ0VSVElGSUNBVEUgUkVRVUVTVC0tLS0tCg== 
  signerName: kubernetes.io/kube-apiserver-client
  usages:
  - client auth
```
### apply 
```
kubectl apply -f user-jack-csr.yaml
```

## Approve the request
```
kubectl get csr
kubectl certificate approve user-jack
```

### now, you can get certificate

```
kubectl get csr user-jack -o yaml
```


## copy The certificate from previous command and decode with base64
```
echo "certificate" | base64 --decode > user-jack.crt
```

## now we can create cofig file for jack user to access to the cluster
```
base64 user-jack.key | tr -d "\n"
base64 user-jack.crt | tr -d "\n"

```
## finally create role and rolebindig or clusterrole and clusterrolebinding for this user

### clusterrole
```

apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: jack-clusterrole
rules:
- apiGroups: [""]
  resources: ["pods", "service"]
  verbs: ["get", "create", "list", "update", "delete"]
  #verbs: ["*"]

- apiGroups: ["apps"]
  resources: ["deployments", "statefulSet"]
  verbs: ["get", "create", "list", "update", "delete"]


```
### clusterrolebinding
```

apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: jack-clusterrolebinding
subjects:
- kind: User
  name: jack
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: jack-clusterrole
  apiGroup: rbac.authorization.k8s.io

```

#### now work with cluster

```
kubectl --kubeconfig jack-user.conf get pod
```
