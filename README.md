# Phần mềm clone html bằng python

## Mô tả phẩn mềm

- Phần mềm clone code của một trang web sử dụng python
- Clone code cấp độ một của các trang web có địa chỉ đúng(ví dụ: https)
- Phần mềm có khả năng bỏ qua các đường link bị lỗi, có khả năng nâng cấp lên clone html cấp độ cao hơn khi cần thiết (dễ nâng cấp)

## Tác Gỉa

- Phạm Quang Huy
- Mã sinh viên: 685105031

## Cách cài đặt

### Cài đặt cơ sở dữ liệu

- Cài đặt CSDL(sử dụng sql server):
  > create database Web
  > create table DB(Name nvarchar(max), Code nvarchar(max))
- Import dữ liệu từ file Sql Script/script.sql

### Cài đặt thư viện cần thiết cho python

- Cài đặt bộ thư viện cho python: pyodbc, urllib, requests, bs4
- Toàn bộ thư viện cần sử dụng được đặt trong thư mục Lib

### Hướng dẫn sử dụng

- Thay đổi đường dẫn đúng đến SQL Server trong máy
- Thay đổi đường dẫn lưu file .html nếu cần thiết
- Chạy file Project2.py bằng IDE của python (Khuyến cáo nên sử dụng Python 3.9)
- Copy đường link có định dạng chuẩn http và đưa vào ô input theo giao diện
- Qúa trình clone code được diễn ra trong khoảng 20s đối với các trang web có nhiều tab do đó nên theo dõi màn hình console để xem qua trình chạy nếu bị chậm
