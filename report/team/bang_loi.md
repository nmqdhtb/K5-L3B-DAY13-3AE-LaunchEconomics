# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Trương Thu Hà · Người gắn nhãn 2: Nguyễn Ngọc Quang (gắn trong 8 phút, không trao đổi)

Hai cột nhãn gốc được lưu ở commit `55d9ecc` (Hà) và `f5e5d9b` (Quang). Nhóm ghi kết quả đối chiếu ở commit `30090cf`.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Hệ thống | Do người dùng | Không | Do người dùng |
| 2 | Giới hạn hệ thống | Hệ thống | Không | Hệ thống |
| 3 | Hệ thống | Ngữ cảnh | Không | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Ngầm | Hệ thống | Không | Hệ thống |
| 8 | Ngữ cảnh | Hệ thống | Không | Hệ thống |
| 9 | Giới hạn hệ thống | Do người dùng | Không | Do người dùng |
| 10 | Hệ thống | Ngữ cảnh | Không | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Do người dùng | Ngầm | Không | Ngầm |
| 13 | Ngữ cảnh | Giới hạn hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Do người dùng | Ngầm | Không | Ngầm |
| 18 | Giới hạn hệ thống | Ngữ cảnh | Không | Ngữ cảnh |
| 19 | Hệ thống | Giới hạn hệ thống | Không | Giới hạn hệ thống |
| 20 | Ngữ cảnh | Hệ thống | Không | Hệ thống |

**Tỉ lệ đồng thuận ban đầu:** 7 / 20 = 35%. Hai bộ nhãn gốc trùng ở ca 4, 5, 6, 11, 14, 15, 16. Mức này dưới mốc 80% (16 ca), nên nhóm viết lại định nghĩa năm loại lỗi bên dưới rồi mới chốt nhãn thống nhất cho 13 ca lệch.

**Đối chiếu đáp án:** So từng ô ở cột “Nhãn thống nhất” với nhãn tham khảo của lab cho cùng số ca, kết quả khớp 20/20. Tỉ lệ đồng thuận độc lập vẫn là 7/20.

## Quy tắc phân biệt cho các ca không trùng

**Định nghĩa đã viết lại (vì đồng thuận dưới 80%).** Hỏi theo thứ tự, dừng ở câu đầu tiên trả lời "có":

1. **Do người dùng:** lỗi bắt đầu từ thông tin khách nhập, chọn hoặc bấm sai, kể cả khi trợ lý lẽ ra nên hỏi lại. Việc trợ lý cần gợi ý tốt hơn ghi ở cột khắc phục, không đổi nhãn.
2. **Giới hạn hệ thống:** trợ lý không thể làm được dù cố gắng: thiếu dữ liệu, yêu cầu ngoài phạm vi, hoặc dạng đầu vào không xử lý được. Trả lời kém trong tình huống này vẫn là Giới hạn.
3. **Ngữ cảnh:** trợ lý làm đúng thiết kế và chính sách, nhưng giả định không khớp hoàn cảnh hoặc kỳ vọng của khách.
4. **Hệ thống:** trợ lý làm trái thiết kế hoặc chính sách (tính sai, gọi sai tham số, trích dẫn sai, báo sai trạng thái, thiếu khóa chống trùng) và cái sai đã lộ ra.
5. **Ngầm:** có sai về tiền hoặc chi phí kéo dài mà cả khách lẫn hệ thống không nhận ra, chỉ lộ khi kiểm tra mẫu.

| Ca | Nhãn Hà | Nhãn Quang | Nhãn chốt | Quy tắc phân biệt |
| --: | --- | --- | --- | --- |
| 1 | Hệ thống | Do người dùng | Do người dùng | Gốc lỗi là khách nhập thiếu hai chữ số tài khoản; việc trợ lý không kiểm định dạng là chỗ khắc phục, không phải nguyên nhân. |
| 2 | Giới hạn hệ thống | Hệ thống | Hệ thống | Trợ lý có đủ bảng giá hàng nặng nhưng gọi sai tham số, nên làm được mà làm sai; khách mở lại nên lỗi đã lộ. |
| 3 | Hệ thống | Ngữ cảnh | Ngữ cảnh | Hoàn về ví trong 5 phút đúng thiết kế; chỉ kỳ vọng nhận tiền qua ngân hàng của khách không khớp. |
| 7 | Ngầm | Hệ thống | Hệ thống | Sổ cái đã trả lỗi 503 và cả 3 lần thử lại đều thất bại, nên thông báo “đã hoàn tiền thành công” trái với trạng thái trợ lý đã nhận. |
| 8 | Ngữ cảnh | Hệ thống | Hệ thống | Viện dẫn điều 7.2 không tồn tại là sai so với chính sách dù số tiền đúng; trích dẫn sai nhìn thấy được nên không phải Ngầm. |
| 9 | Giới hạn hệ thống | Do người dùng | Do người dùng | Khách nhập mã đơn của sàn thay vì mã vận đơn; trợ lý không gợi ý là việc cần cải thiện ở cột khắc phục. |
| 10 | Hệ thống | Ngữ cảnh | Ngữ cảnh | Từ chối theo điều khoản bất khả kháng là đúng chính sách; khách thấy sai vì kỳ vọng từ dòng "cam kết giao 24 giờ". |
| 12 | Do người dùng | Ngầm | Ngầm | Kết quả vẫn đúng nhưng chi phí token gấp 3 lần suốt 3 tuần mà không ai thấy; "sai" ở đây là sai về chi phí, không liên quan thao tác của khách. |
| 13 | Ngữ cảnh | Giới hạn hệ thống | Giới hạn hệ thống | Phí bảo hiểm là sản phẩm của đối tác, ngoài phạm vi trợ lý; trả lời chung chung là xử lý giới hạn kém, ghi ở cột khắc phục. |
| 17 | Do người dùng | Ngầm | Ngầm | Dùng bảng giá cũ làm 212 đơn lệch trong 9 ngày, không khách nào mở lại; lỗi chỉ lộ khi đối chiếu với bảng giá hiện hành. |
| 18 | Giới hạn hệ thống | Ngữ cảnh | Ngữ cảnh | Số tiền 15.000 đ đúng chính sách; khách hiểu sai vì thông báo thiếu cách tính, không phải vì trợ lý thiếu khả năng. |
| 19 | Hệ thống | Giới hạn hệ thống | Giới hạn hệ thống | Trợ lý chỉ truy cập được dữ liệu 12 tháng và đã nói rõ rồi chuyển nhân viên, tức là gặp giới hạn và xử lý đúng. |
| 20 | Ngữ cảnh | Hệ thống | Hệ thống | Hoàn hai lần vì lệnh thứ hai thiếu khóa chống trùng là lỗi thiết kế; khách gửi lại sau 10 phút là hành vi hợp lệ. |

<details>
<summary>Đối chiếu sau khi khóa hai bộ nhãn gốc · 20 ca trong đề</summary>

| Loại lỗi tham khảo | Ca | Căn cứ phân loại |
| --- | --- | --- |
| Do người dùng | 1, 6, 9, 14 | Khách nhập thiếu số tài khoản, chọn nhầm mục khiếu nại, dùng nhầm loại mã hoặc xác nhận nhầm đã nhận tiền. |
| Hệ thống | 2, 7, 8, 15, 20 | Trợ lý chọn sai tham số giá, báo hoàn thành khi ghi sổ thất bại, viện dẫn điều khoản không tồn tại, tính sai tỷ lệ hoặc ghi hoàn trùng. |
| Ngữ cảnh | 3, 10, 16, 18 | Ví nhận tiền, lời hứa giao trong 24 giờ, giờ gửi thông báo hoặc cách giải thích số tiền khiến kết quả khác kỳ vọng của khách. |
| Giới hạn hệ thống | 4, 11, 13, 19 | Trợ lý thiếu dữ liệu chặng đối tác, khả năng đọc âm thanh, quyền xử lý bảo hiểm hoặc lịch sử đơn quá 12 tháng. |
| Ngầm | 5, 12, 17 | Hoàn thừa do mã giảm giá, chi phí token tăng kéo dài ở D05 hoặc dùng bảng giá cũ. Sai lệch tồn tại qua nhiều đơn và chỉ lộ khi rà soát. |

Nguồn phân loại là mục “Nhãn tham khảo cho 20 ca” trong [hướng dẫn của lab](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md). Khi xử lý ca bất đồng thực tế, giữ nguyên cả hai nhãn gốc, ghi nhãn chốt và dẫn một chi tiết quyết định từ tình huống.

</details>

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Quân soạn bảng khắc phục, Hà rà soát và bổ sung tên sự kiện. Bảng dưới ghi các phép kiểm đề xuất cho pilot.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Mỗi lần khách gửi biểu mẫu, kiểm độ dài số tài khoản theo ngân hàng nhận. Ghi `input_validation_failed` và báo ngay cho khách từ lần đầu sai định dạng. | Chặn tạo lệnh hoàn, chỉ rõ số chữ số ngân hàng yêu cầu và cho khách sửa trước khi gửi lại. | Trưởng nhóm tích hợp thanh toán |
| 20 | Hệ thống | Event `refund_ledger_write` sau mỗi lần ghi sổ: đếm giao dịch hoàn thành theo mã nghĩa vụ hoàn phí. Ngưỡng: báo ngay từ giao dịch thành công thứ 2 cho cùng nghĩa vụ. | Dùng một khóa chống trùng (idempotency key) cho mọi lần gửi lại cùng nghĩa vụ. Khi phát hiện hoàn hai lần, khóa yêu cầu và chuyển kế toán đối soát. | Trưởng nhóm kỹ thuật thanh toán |
| 18 | Ngữ cảnh | Event `ticket_reopened` với lý do "hoàn thiếu", rà hằng tuần. Ngưỡng: ghi nhận từ 1 ca có số tiền đúng nhưng thông báo thiếu cách tính. | Hiển thị phí gốc, tỷ lệ và số tiền hoàn trong cùng thông báo. Với ca này, khách sẽ thấy 30.000 đ × 50% = 15.000 đ. | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Mỗi giờ, lọc nhật ký tra cứu lấy các yêu cầu trả kết quả “đơn quá 12 tháng”. Ghép với `handoff_to_staff` theo `request_id`. Báo khi có ít nhất 1 yêu cầu đã quá 1 giờ mà hàng đợi nhân viên chưa ghi nhận. | Trợ lý giải thích giới hạn tra cứu và chuyển mã đơn cùng tóm tắt cho nhân viên. Chỉ báo đã bàn giao khi hàng đợi trả mã tiếp nhận. | Trưởng nhóm vận hành |
| 5 | Ngầm | Mỗi tuần, kế toán lấy mẫu đơn có mã giảm giá, tính lại tiền được hoàn từ hóa đơn sau giảm và chính sách áp dụng, rồi so với tiền thực chi trong sổ cái. Ghi `refund_audited` và mở điều tra từ 1 khoản hoàn thừa. | Tính hoàn từ giá khách thực trả. Rà lại 14 đơn phát hiện trong đề và kiểm tra các đơn dùng cùng quy tắc tính. | Kế toán trưởng |
