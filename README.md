Web Server Lab

Ein vollständiges Load-Balanced Web-Server Setup als Lernprojekt.

Architektur
Nginx Load Balancer (:80)
├─→ App Server 1 (:8001)
├─→ App Server 2 (:8002)
└─→ App Server 3 (:8003)

Setup
1. Services starten
sudo systemctl start webserver-{1,2,3} nginx

2. Status prüfen
./scripts/monitor.sh

3. Testen
curl http://localhost/

Management Commands
Task	Command	Description
Deployment	./scripts/deploy.sh	Deploy die App Server
Monitoring	./scripts/monitor.sh	Prüfe Status aller Services
Log Analyse	./scripts/log_analysis.sh	Analysiere Logs
Load Testing	ab -n 1000 -c 10 http://localhost/	Simuliere Lasttests
Endpoints
Methode	Pfad	Beschreibung
GET	/	Server Info
GET	/health	Health Check
GET	/info	Detaillierte Request Info
GET	/slow	Simulierter langsamer Request (2s)
Troubleshooting
Service nicht erreichbar
systemctl status webserver-1
journalctl -u webserver-1 -n 50

Load Balancer funktioniert nicht
sudo nginx -t
sudo systemctl status nginx
sudo tail /var/log/nginx/webserver-lab-error.log

Ports checken
ss -tlnp | grep -E ':(80|8001|8002|8003)'
