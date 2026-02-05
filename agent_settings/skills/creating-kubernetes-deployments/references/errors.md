# Error Handling Reference

**Image Pull Error**
- Error: "ErrImagePull" or "ImagePullBackOff"
- Solution: Verify image name, tag, and registry credentials in imagePullSecrets

**CrashLoopBackOff**
- Error: Pod repeatedly crashes and restarts
- Solution: Check application logs with `kubectl logs` and review container health

**Resource Quota Exceeded**
- Error: "forbidden: exceeded quota"
- Solution: Reduce resource requests or increase namespace quota

**Ingress Not Working**
- Error: 404 or 503 on ingress domain
- Solution: Verify ingress controller is running and service endpoints are ready

**TLS Certificate Error**
- Error: "certificate signed by unknown authority"
- Solution: Create or update TLS secret with valid certificate
