# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Trương Thu Hà · Người gắn nhãn 2: Nguyễn Ngọc Quang (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |
| 4 | ... | ... | ... | ... |
| 5 | ... | ... | ... | ... |
| 6 | ... | ... | ... | ... |
| 7 | ... | ... | ... | ... |
| 8 | ... | ... | ... | ... |
| 9 | ... | ... | ... | ... |
| 10 | ... | ... | ... | ... |
| 11 | ... | ... | ... | ... |
| 12 | ... | ... | ... | ... |
| 13 | ... | ... | ... | ... |
| 14 | ... | ... | ... | ... |
| 15 | ... | ... | ... | ... |
| 16 | ... | ... | ... | ... |
| 17 | ... | ... | ... | ... |
| 18 | ... | ... | ... | ... |
| 19 | ... | ... | ... | ... |
| 20 | ... | ... | ... | ... |

**Tỉ lệ đồng thuận:** ... / 20 = ...%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- ...

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện đo được bằng event, ngưỡng và tần suất. Mỗi dòng có một vai trò phụ trách. Bản nháp do Quân soạn; Hà rà soát, bổ sung tên event và đối chiếu với nhãn thống nhất.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `input_validation_failed` cho mỗi lệnh hoàn: kiểm định dạng số tài khoản theo ngân hàng nhận. Ngưỡng: báo ngay khi có 1 lệnh được gửi dù kiểm tra độ dài thất bại. | Chặn gửi lệnh và hướng dẫn khách sửa số tài khoản. Chỉ cho gửi lại sau khi dữ liệu hợp lệ. | Trưởng nhóm tích hợp thanh toán |
| 20 | Hệ thống | Event `refund_ledger_write` sau mỗi lần ghi sổ: đếm giao dịch hoàn thành theo mã nghĩa vụ hoàn phí. Ngưỡng: báo ngay từ giao dịch thành công thứ 2 cho cùng nghĩa vụ. | Dùng một khóa chống trùng (idempotency key) cho mọi lần gửi lại cùng nghĩa vụ. Khi phát hiện hoàn hai lần, khóa yêu cầu và chuyển kế toán đối soát. | Trưởng nhóm kỹ thuật thanh toán |
| 18 | Ngữ cảnh | Event `ticket_reopened` với lý do "hoàn thiếu", rà hằng tuần. Ngưỡng: ghi nhận từ 1 ca có số tiền đúng nhưng thông báo thiếu cách tính. | Hiển thị phí gốc, tỷ lệ và số tiền hoàn trong cùng thông báo. Với ca này, khách sẽ thấy 30.000 đ × 50% = 15.000 đ. | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Event `handoff_to_staff` cho từng yêu cầu về đơn quá 12 tháng: kiểm tra có mã đơn và lý do vượt thời hạn tra cứu. Ngưỡng: báo nếu thiếu 1 lượt chuyển. | Giữ cách chuyển kèm tóm tắt như trong đề. Xác nhận mã tiếp nhận cho khách và giao nhân viên tra kho lưu trữ. | Trưởng nhóm vận hành |
| 5 | Ngầm | Event `refund_audited` mỗi tuần: kế toán đối chiếu tiền thực hoàn với giá sau giảm của các đơn dùng mã giảm giá. Ngưỡng: mở ca điều tra ngay khi phát hiện 1 khoản hoàn thừa. | Tính hoàn từ giá khách thực trả. Rà lại 14 đơn phát hiện trong đề và kiểm tra các đơn dùng cùng quy tắc tính. | Kế toán trưởng |