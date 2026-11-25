# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

Xem [bài mẫu CP3 với 20 tình huống tự tạo](../../docs/CP3_bai_mau.md) để tham khảo cách trình bày và tính đồng thuận.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Trương Thu Hà · Người gắn nhãn 2: Nguyễn Ngọc Quang (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Hệ thống | ... | ... | ... |
| 2 | Giới hạn hệ thống | ... | ... | ... |
| 3 | Hệ thống | ... | ... | ... |
| 4 | Giới hạn hệ thống | ... | ... | ... |
| 5 | Ngầm | ... | ... | ... |
| 6 | Do người dùng | ... | ... | ... |
| 7 | Ngầm | ... | ... | ... |
| 8 | Ngữ cảnh | ... | ... | ... |
| 9 | Giới hạn hệ thống | ... | ... | ... |
| 10 | Hệ thống | ... | ... | ... |
| 11 | Giới hạn hệ thống | ... | ... | ... |
| 12 | Do người dùng | ... | ... | ... |
| 13 | Ngữ cảnh | ... | ... | ... |
| 14 | Do người dùng | ... | ... | ... |
| 15 | Hệ thống | ... | ... | ... |
| 16 | Ngữ cảnh | ... | ... | ... |
| 17 | Do người dùng | ... | ... | ... |
| 18 | Giới hạn hệ thống | ... | ... | ... |
| 19 | Hệ thống | ... | ... | ... |
| 20 | Ngữ cảnh | ... | ... | ... |

**Tỉ lệ đồng thuận ban đầu:** chờ hai bộ nhãn độc lập. Khi đủ dữ liệu, lấy số ca có hai nhãn gốc giống nhau chia cho 20. Mốc 80% tương ứng 16 ca.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

<details>
<summary>Đối chiếu sau khi khóa hai bộ nhãn gốc · 20 ca trong đề</summary>

| Loại lỗi tham khảo | Ca | Căn cứ phân loại |
| --- | --- | --- |
| Do người dùng | 1, 6, 9, 14 | Khách nhập thiếu số tài khoản, chọn nhầm mục khiếu nại, dùng nhầm loại mã hoặc xác nhận nhầm đã nhận tiền. |
| Hệ thống | 2, 7, 8, 15, 20 | Trợ lý chọn sai tham số giá, báo hoàn thành khi ghi sổ thất bại, viện dẫn điều khoản không tồn tại, tính sai tỷ lệ hoặc ghi hoàn trùng. |
| Ngữ cảnh | 3, 10, 16, 18 | Ví nhận tiền, lời hứa giao trong 24 giờ, giờ gửi thông báo hoặc cách giải thích số tiền khiến kết quả khác kỳ vọng của khách. |
| Giới hạn hệ thống | 4, 11, 13, 19 | Trợ lý thiếu dữ liệu chặng đối tác, khả năng đọc âm thanh, quyền xử lý bảo hiểm hoặc lịch sử đơn quá 12 tháng. |
| Ngầm | 5, 12, 17 | Hoàn thừa do mã giảm giá, chi phí gọi tool tăng kéo dài hoặc dùng bảng giá cũ. Sai lệch tồn tại qua nhiều đơn và chỉ lộ khi rà soát. |

Nguồn phân loại là mục “Nhãn tham khảo cho 20 ca” trong [hướng dẫn của lab](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md). Khi xử lý ca bất đồng thực tế, giữ nguyên cả hai nhãn gốc, ghi nhãn chốt và dẫn một chi tiết quyết định từ tình huống.

</details>

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện đo được bằng event, ngưỡng và tần suất. Mỗi dòng có một vai trò phụ trách. Bản nháp do Quân soạn; Hà rà soát, bổ sung tên event và đối chiếu với nhãn thống nhất.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `input_validation_failed` cho mỗi lệnh hoàn: kiểm định dạng số tài khoản theo ngân hàng nhận. Ngưỡng: báo ngay khi có 1 lệnh được gửi dù kiểm tra độ dài thất bại. | Chặn gửi lệnh và hướng dẫn khách sửa số tài khoản. Chỉ cho gửi lại sau khi dữ liệu hợp lệ. | Trưởng nhóm tích hợp thanh toán |
| 20 | Hệ thống | Event `refund_ledger_write` sau mỗi lần ghi sổ: đếm giao dịch hoàn thành theo mã nghĩa vụ hoàn phí. Ngưỡng: báo ngay từ giao dịch thành công thứ 2 cho cùng nghĩa vụ. | Dùng một khóa chống trùng (idempotency key) cho mọi lần gửi lại cùng nghĩa vụ. Khi phát hiện hoàn hai lần, khóa yêu cầu và chuyển kế toán đối soát. | Trưởng nhóm kỹ thuật thanh toán |
| 18 | Ngữ cảnh | Event `ticket_reopened` với lý do "hoàn thiếu", rà hằng tuần. Ngưỡng: ghi nhận từ 1 ca có số tiền đúng nhưng thông báo thiếu cách tính. | Hiển thị phí gốc, tỷ lệ và số tiền hoàn trong cùng thông báo. Với ca này, khách sẽ thấy 30.000 đ × 50% = 15.000 đ. | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Event `handoff_to_staff` cho từng yêu cầu về đơn quá 12 tháng: kiểm tra có mã đơn và lý do vượt thời hạn tra cứu. Ngưỡng: báo nếu thiếu 1 lượt chuyển. | Giữ cách chuyển kèm tóm tắt như trong đề. Xác nhận mã tiếp nhận cho khách và giao nhân viên tra kho lưu trữ. | Trưởng nhóm vận hành |
| 5 | Ngầm | Event `refund_audited` mỗi tuần: kế toán đối chiếu tiền thực hoàn với giá sau giảm của các đơn dùng mã giảm giá. Ngưỡng: mở ca điều tra ngay khi phát hiện 1 khoản hoàn thừa. | Tính hoàn từ giá khách thực trả. Rà lại 14 đơn phát hiện trong đề và kiểm tra các đơn dùng cùng quy tắc tính. | Kế toán trưởng |