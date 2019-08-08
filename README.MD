# LSP
Dwi Dian Ayu - LSP . Selamatkan 1.7Jt kawan!
Odoo plugin ada di folder add_ons

## Requirement
- Docker
- Docker Compose

### Local Deployment | Docker
```bash
  $ docker network create dda # create an isolate docker network
  # run service
  $ docker-compose up -d
  # remove service
  $ docker-compose down
```
buka di browser http://localhost:8069

#### Note :
jika proses terasa lama, coba check logs pada container dengan perintah
```bash
  $ docker-compose logs --follow -tail=10
```