# REST API 

- Link tham khảo 
- https://realpython.com/flask-connexion-rest-api/
- https://realpython.com/flask-connexion-rest-api-part-2/
- https://realpython.com/flask-connexion-rest-api-part-3/
- https://realpython.com/python3-object-oriented-programming/

## Require

- __Python__
- __Flask__
- __SQLAlchemy__: tạo datamodel, kết nối với db và làm trung gian giữa db và backend
- __Marshmallow__ : converting complex datatypes, such as objects, to and from native Python datatypes.
- __Psycopg2__
- __Connexion__: cho phép sử dụng __swagger__, cung cấp validate input and output data from API 

## Structure Folder

- __controller :__ khi gọi một phương thức get, swagger ánh xạ tới một function trong controller. funtion xử lý và trả lại kết quả.
- __models :__ tạo model của dữ liệu.
- __static :__ lưu trữ file css, js, ảnh...
- __templates :__ lưu trữ file html render ra front end. Tuy nhiên ta viết rest api nên không cần quan tâm tới nó lắm

## Checklist
- Khởi tạo Project, kết nối tới swagger

### Phân quyền
- Step 1: Login và trả về token để xác thực user là thằng nào
- Step 2: Tài nguyên: lấy ra tài nguyên đang sở hữu <Ảnh, Video>
- Step 3: Xem tài nguyên của thằng khác: - Xem được của người dưới cấp, cùng cấp nếu có quyền share

### How to start Project

- Step 1: Tạo database trong PostgreSQL
    - Tạo một DB mới trong PGAdmin4
    - Copy pase lệnh trong __database/database.sql__ và chạy
- Step 2: Sửa chuỗi kết nối tới SQL trong file __config.py__
- Step 2: Chạy project
    - __python server.py__