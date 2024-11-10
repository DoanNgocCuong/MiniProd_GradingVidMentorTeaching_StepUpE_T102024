```bash
docker build -t doanngoccuong/deployh3_5promptdetandscoring .
docker push doanngoccuong/deployh3_5promptdetandscoring
``` 

Cách pull

   - Người khác có thể tải xuống và chạy container từ Docker Hub bằng lệnh:
     ```bash
     docker pull doanngoccuong/deployh3_5promptdetandscoring
     ```

### 2. **Chạy Container từ Docker Hub**
   - Người dùng khác có thể chạy container từ image Docker của bạn bằng lệnh:
     ```bash
     docker run --env-file .env -p 25034:25034 doanngoccuong/deployh3_5promptdetandscoring
     ```
   - **Lưu ý**: Đảm bảo rằng người dùng khác có file `.env` với các biến môi trường cần thiết cho ứng dụng.