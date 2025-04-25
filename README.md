1. ##### Clone source code về  -> sau đó: 
```bash
docker-compose pull
```
2. ##### Khởi động docker -> sau đó: 
```bash
docker-compose up -d
```
3. ##### Nếu muốn thêm module thì thêm vào thư mục addons module sẽ tự mount vào: 

## Muốn update module mới thì exec vào service odoo đang chạy và chạy terminal -> trong docker desktop có phần exec terminal
update
```bash
odoo -d {db_name (setup lúc khởi chạy lần đầu)} -u customer_metrics --stop-after-init
```
##install
```bash
odoo -d {db_name (setup lúc khởi chạy lần đầu)} -i customer_metrics --stop-after-init
```
####nếu muốn reset lại tất cả thì phải 
```bash
docker-compose down -v
```
sau đó xóa folder volumes
rồi up lại sẽ hoạt động như ban đầu
master-pass lúc setup database là changeme