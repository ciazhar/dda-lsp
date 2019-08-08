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

## Multiple Stack | Deploy
```
  $ docker-compose -f Stack/{version} up -d # run service
  $ docker-compose -f Stack/{version} down # remove service
  $ docker-compose -f Stack/{version} logs # logs service

  # ex:
  $ docker-compose -f Stack/version-10.yml up -d 
  # will run odoo service version 10
```