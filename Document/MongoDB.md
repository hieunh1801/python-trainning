# Learning MongoDB
## Cài đặt && Chạy MongoDB
- Step 1: Cài đặt
  + Tải file .msi => chạy tất cả mặc định
  + Các file cài đặt và file run sẽ ở trong thư mục __C:\Program Files\MongoDB\Server\4.0__
- Thêm Path variable __C:\Program Files\MongoDB\Server\4.0\bin__
- Để chạy: __mongod__ để chạy server && __mongo__ để chạy client.
## Syntax in mongo client

-- __FOR__ dabase: thêm, sửa, xóa, show current, show all

| Syntax            | Description                                    |
|:------------------|:-----------------------------------------------|
| use school        | sử dụng db school (nếu chưa có sẽ tự tạo)      |
| show dbs          | show tất cả database                           |
| show collections  | Hiển thị tất cả các collections                |
| db                | kiểm tra db hiện tại                           |
| db.dropDatabase() | xóa db hiện tại (chú ý check kĩ trước khi xóa) |

-- __FOR__ Collections: tạo mới, xóa
> __Trong mongo ta không cần tạo collection, khi ta thêm một Document thì mongo tự tạo luôn Collection đó__

| Syntax                                            | Description                                                          |
|:--------------------------------------------------|:---------------------------------------------------------------------|
| show collections                                  | Hiển thị tất cả các collections                                      |
| db.createCollection("student")                    | Tạo collection mới có tên là student                                 |
| db.createCollection("student", { capped : true }) | Tạo collection mới có tên là student, các option liệt kê ở phía dưới |

Các option khi tạo một collections mới
| Field       | Type    | Descriptions                                                                                                       |
|:------------|:--------|:-------------------------------------------------------------------------------------------------------------------|
| capped      | boolean | collections có kích cỡ cố định, tự động ghi đè các bản ghi cũ nếu tới kích cỡ tối đa. do đó cần cung cấp thêm size |
| autoIndexID | boolean | tự động đánh index trên trường _id. mặc định là false                                                              |
| size        | int     | kích cỡ tối đa (byte) cho một capped collection                                                                    |
| max         | int     | xác định số Document tối đa trong một capped collection                                                            |

-- __FOR__ Document: tạo một bản ghi mới, xóa, tìm kiếm, ....
- Document có dạng key value
```json
{
  name: "Nguyen Huu Hieu",
  class: "12A1",
  age: 21,
  subjects: ["mongodb", "mysql", "postgreSQL", "python"]
}
```
- Khi ta tạo một Document mới mà không cung cấp id thì mongo sẽ cung cấp id mặc định

| Syntax                                       | Description                                                                         |
|:---------------------------------------------|:------------------------------------------------------------------------------------|
| db.student.insert({name: "Nguyen Huu Hieu"}) | thêm một document {name: "Nguyen Huu Hieu"} vào trong collection student            |
| db.student.find()                            | hiển thị tất cả document trong collection student                                   |
| db.student.findOne()                         | hiển thị document đầu tiên tìm được trong collection student                        |
| db.student.find().pretty()                   | hiển thị tất cả document trong collection student dưới dạng dễ nhìn hơn             |
| db.student.find({age:{$lt: 23}})             | $lt: less than, $lte: less than equal , $gt: greater than, $gte: greater than equal |
| db.student.find({age:{$ne: 23}})             | $ne: not equal                                                                      |



## Core Concept
  + Collection
  + Document