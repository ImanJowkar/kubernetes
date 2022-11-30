# installation

[refrenece](https://github.com/skooner-k8s/skooner)

```
kubectl apply -f https://raw.githubusercontent.com/skooner-k8s/skooner/master/kubernetes-skooner.yaml


# and deploy 

kind: Ingress
apiVersion: networking.k8s.io/v1
metadata:
  name: skooner
  namespace: kube-system
spec:
  rules:
    - host: skooner.example.com
      http:
        paths:
          - path: /
            backend:
              service:
                name: skooner
                port:
                  number: 80
            pathType: ImplementationSpecific

```