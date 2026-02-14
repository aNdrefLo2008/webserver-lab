<!-- @format -->

> # Web Server Lab

Ein vollständiges Load-Balanced Web-Server Setup als Lernprojekt.

## Architektur

Nginx Load Balancer (:80)

├─→ App Server 1 (:8001)

├─→ App Server 2 (:8002)

└─→ App Server 3 (:8003)

## Setup

1. Services starten:sudo systemctl start webserver-{1,2,3} nginx  
   ├─→ App Server 2 (:8002)

└─→ App Server 3 (:8003)

## Setup

1. Services starten:sudo systemctl start webserver-{1,2,3} nginx 2. Status checken: ./scripts/[monitor.sh](http://monitor.sh) 3. Testen: curl [http://localhost/](http://localhost/) ## Management Commands

### Deployment ./scripts/[deploy.sh](http://deploy.sh)

### Monitoring ./scripts/[monitor.sh](http://monitor.sh) ### Log Analysis ./scripts/log\_[analysis.sh](http://analysis.sh)

### Load Testing ab -n 1000 -c 10 [http://localhost/](http://localhost/) ## Endpoints

- `GET /` - Server info
- `GET /health` - Health check
- `GET /info` - Detailed request info
- `GET /slow` - Simulated slow request (2s)

## Troubleshooting

### Service nicht erreichbar

systemctl status webserver-1

journalctl -u webserver-1 -n 50

### Load Balancer funktioniert nicht

sudo nginx -t

sudo systemctl status nginx

sudo tail /var/log/nginx/webserver-lab-error.log

### Ports checken

ss -tlnp | grep -E ':(80|8001|8002|8003)'
