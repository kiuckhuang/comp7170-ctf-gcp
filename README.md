# comp7170-ctf-gcp
COMP7170 CTF Game - SQL Injection

# Local
## build the docker image and run at local
```
docker buildx build --platform linux/amd64,linux/arm64 -t comp7170-ctf-gcp .
```

## run local
```
docker run -p 8080:8080 --name comp7170-ctf-gcp -d comp7170-ctf-gcp
```

# Docker Repository
## tag and push to docker repo
```
docker buildx build --platform linux/amd64,linux/arm64 -t kiuckhuang/comp7170:ctf_version1 --push .
```
## run from repo
```
docker run -p 8080:8080 --name comp7170-ctf-v1 -d kiuckhuang/comp7170:ctf_version1
```
