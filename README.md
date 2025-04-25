1. ##### Clone source code về  -> sau đó khởi động docker : 
```bash
cd {tên thư mục}
```

```bash
docker-compose pull
```
2. #####  -> sau đó: 
```bash
docker-compose up -d
```
3. ##### Nếu muốn thêm module thì thêm vào thư mục addons module sẽ tự mount vào: 

## Muốn update module mới thì exec vào service odoo đang chạy và chạy terminal -> trong docker desktop có phần exec terminal
update
```bash
odoo -d {db_name (setup lúc khởi chạy lần đầu)} -u {tên module} --stop-after-init
```
##install
```bash
odoo -d {db_name (setup lúc khởi chạy lần đầu)} -i {tên module} --stop-after-init
```
####nếu muốn reset lại tất cả thì phải 
```bash
docker-compose down -v
```
sau đó xóa folder volumes
rồi up lại sẽ hoạt động như ban đầu
##master-pass lúc setup database là
```bash 
changeme
```