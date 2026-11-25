# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Trương Thu Hà · Người gắn nhãn 2: Nguyễn Ngọc Quang (gắn trong 8 phút, không trao đổi)

Có thể kiểm tra riêng từng bộ nhãn theo số ca ở ba bản lưu. [Nhãn gốc của Hà](https://github.com/nmqdhtb/K5-L3B-DAY13-3AE-LaunchEconomics/blob/55d9ecc681df5c3a2132f7d20ddd760b1d83de3b/report/team/bang_loi.md) · [Nhãn gốc của Quang](https://github.com/nmqdhtb/K5-L3B-DAY13-3AE-LaunchEconomics/blob/f5e5d9bb46be15529f97a5b9ff2b2d5b93a39002/report/team/bang_loi.md) · [Bản đối chiếu của nhóm](https://github.com/nmqdhtb/K5-L3B-DAY13-3AE-LaunchEconomics/blob/30090cfab8da90fe6505a7dc20e32c47d0d65d56/report/team/bang_loi.md)

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

**Đồng thuận độc lập.** Hà và Quang trùng nhãn ở các ca 4, 5, 6, 11, 14, 15 và 16. Tỉ lệ là **7/20 = 35%**, dưới ngưỡng 16/20 của tiêu chí C3. [Rubric C3](../../RUBRIC.md#rubric)

**Xử lý 13 ca bất đồng.** Theo điều kiện “Xong khi” của CP3, nhóm viết lại định nghĩa cho cả 5 loại lỗi và ghi căn cứ chốt từng ca ở bảng dưới. Đối chiếu cột “Nhãn thống nhất” theo số ca với đáp án của lab cho kết quả **20/20**. [Hướng dẫn nhiệm vụ C](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md#nhiệm-vụ-c--bảng-lỗi-và-cách-khắc-phục-30-phút)

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
| 12 | Do người dùng | Ngầm | Ngầm | Tool của D05 trả thiếu một trường khiến trợ lý phải gọi lại. Kết quả vẫn đúng nên chi phí token gấp 3 lần các depot khác suốt 3 tuần mới được phát hiện. |
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

Quân soạn bảng khắc phục, Hà rà soát và bổ sung tên sự kiện. Bảng dưới mô tả các phép kiểm đề xuất cho pilot. Dùng `request_id` và `trace_id` để tra lại hồ sơ của từng cảnh báo. Hai sự kiện `ticket_reopened` và `refund_audited` dùng chung với [bảng chỉ số E1](chi_so.md).

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Mỗi lần gửi biểu mẫu, đối chiếu độ dài số tài khoản với quy tắc của ngân hàng nhận. Ngay lần sai đầu tiên, ghi `input_validation_failed` với ngân hàng và số chữ số đã nhập. | Chặn tạo lệnh hoàn, hiển thị số chữ số cần nhập và cho khách sửa tại chỗ. | Trưởng nhóm tích hợp thanh toán |
| 20 | Hệ thống | Sau mỗi `refund_ledger_write` thành công, đếm mã giao dịch sổ cái khác nhau cho cùng mã nghĩa vụ hoàn phí. Cảnh báo ngay khi có giao dịch thứ 2. | Dùng cùng khóa chống trùng cho mọi lần gửi lại một nghĩa vụ. Nếu đã ghi hoàn hai lần, khóa yêu cầu và chuyển kế toán đối soát. | Trưởng nhóm kỹ thuật thanh toán |
| 18 | Ngữ cảnh | Hằng tuần, rà các `ticket_reopened` vì “hoàn thiếu”. Với từng ca, tính lại tiền theo chính sách và đọc bản tin thực gửi. Ghi nhận từ 1 ca có số tiền đúng nhưng bản tin thiếu phép tính. | Hiển thị phí gốc, tỷ lệ và số tiền hoàn trong cùng thông báo. Ở ca 18, khách sẽ thấy 30.000 đ × 50% = 15.000 đ. | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Đếm yêu cầu có kết quả tra cứu “quá 12 tháng” mỗi giờ. Ghép với `handoff_to_staff` do hàng đợi ghi khi cấp mã tiếp nhận. Cảnh báo từ 1 yêu cầu đã quá 1 giờ kể từ lúc tra cứu mà vẫn thiếu mã tiếp nhận. | Giải thích giới hạn 12 tháng, chuyển mã đơn cùng tóm tắt cho nhân viên và xác nhận bàn giao khi có mã tiếp nhận. | Trưởng nhóm vận hành |
| 5 | Ngầm | Hằng tuần, kế toán lấy mẫu đơn có mã giảm giá và tính lại số tiền đúng từ hóa đơn sau giảm theo chính sách áp dụng. Khi kiểm các đơn này, ghi thêm số tính lại (`expected_vnd`) vào `refund_audited`. Điều tra từ 1 ca có số thực chi trong sổ cái (`paid_vnd`) lớn hơn `expected_vnd`. | Tính hoàn từ giá khách thực trả. Đối soát 14 đơn trong đề và rà các giao dịch đã dùng cùng quy tắc tính. | Kế toán trưởng |
