## Hướng dẫn cài đặt
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

## Update: Muốn update module mới thì exec vào service odoo đang chạy và chạy terminal -> trong docker desktop có phần exec terminal
update
```bash
odoo -d {db_name (setup lúc khởi chạy lần đầu)} -u {tên module} --stop-after-init
```
##install
```bash
odoo -d {db_name (setup lúc khởi chạy lần đầu)} -i {tên module} --stop-after-init
```
## Reset: nếu muốn reset lại tất cả thì phải 
```bash
docker-compose down -v
```
sau đó xóa folder volumes
rồi up lại sẽ hoạt động như ban đầu
#### master-pass lúc setup database là
```bash 
changeme
```
## Mở db
### 2. Mở pgAdmin và tạo Server mới  
1. **Mở** pgAdmin trên máy (Windows/Mac/Linux).  
2. **Chuột phải** lên “Servers” → **add new server…**  
3. **Tab General**:  
   - Name: `docker-postgres` (hoặc bất kỳ tên nào bạn thích)  
4. **Tab Connection**:  
   - **Host name/address**: `localhost`  
   - **Port**: `5433`  
   - **Username**: giá trị của `POSTGRES_USER` (ví dụ `odoo18`)  - ở trong odoo.conf
   - **Password**: giá trị của `POSTGRES_PASSWORD` (ví dụ `odoo18`)  - ở trong odoo.conf
   - **Maintenance database**: `your_db` (hoặc `postgres` nếu bạn chưa tạo DB riêng)  -> cái này tạo lúc mở odoo ban đầu
5. **Save** để kết nối ngay lập tức. :contentReference[oaicite:2]{index=2}
