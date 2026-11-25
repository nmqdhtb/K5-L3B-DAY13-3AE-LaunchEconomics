# CP3 · Bài mẫu phân loại 20 ca lỗi hoàn phí

Hai cột A và B là nhãn mô phỏng trên 20 tình huống tự tạo. Ví dụ minh họa cách giữ nhãn ban đầu, tính mức đồng thuận và chọn biện pháp khắc phục. Hà và Quang ghi kết quả độc lập cho các ca trong [đề gốc](Ngay13_Lab13_De_bai_hoc_vien.docx) vào [bảng CP3 của nhóm](../report/team/bang_loi.md).

## 1. Hai bộ nhãn và kết quả thống nhất

| Ca | Tình huống | Nhãn A | Nhãn B | Trùng? | Nhãn thống nhất |
|---:|---|---|---|:---:|---|
| 1 | Khách nhập ngày giao hàng là 31/02. Biểu mẫu yêu cầu nhập lại. | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Chính sách hoàn 20% phí đóng gói. Trợ lý tính thành 30%, nhân viên phát hiện khi xem gợi ý. | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Lệnh hoàn mới được duyệt. Ứng dụng hiện “Đã xử lý”, khiến khách hiểu rằng tiền đã về ví. | Ngữ cảnh | Hệ thống | Khác | Ngữ cảnh |
| 4 | Khách muốn nhận tiền qua một loại ví mà LogiX chưa tích hợp. Trợ lý giải thích và đưa ra hai phương thức được hỗ trợ. | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Khi đối soát tháng, kế toán phát hiện hệ thống hoàn phí đóng gói hai lần cho nhiều đơn. Trước đó mọi giao dịch đều qua kiểm tra. | Ngầm | Ngầm | Có | Ngầm |
| 6 | Khách có hai đơn cùng ngày, chọn nhầm đơn đã giao đúng hạn để khiếu nại giao trễ. | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Dịch vụ tra cứu trả trạng thái “đã hủy”, nhưng trợ lý đọc nhầm trường và báo “đang giao”. Khách phản hồi ngay. | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Trợ lý trả đúng hạn xử lý là “3 ngày làm việc”. Khách đếm cả cuối tuần và mở lại yêu cầu vào sáng thứ Hai. | Ngữ cảnh | Do người dùng | Khác | Ngữ cảnh |
| 9 | Khách gửi tệp chứng từ có mật khẩu. Hệ thống chỉ đọc được tệp chưa mã hóa và hướng dẫn khách gửi bản phù hợp. | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 10 | Báo cáo tuần cho thấy thời gian xử lý trung bình rất thấp. Kiểm tra mẫu mới phát hiện các ca chờ lâu đều bị bỏ khỏi phép tính. | Ngầm | Ngầm | Có | Ngầm |
| 11 | Khách đính kèm hóa đơn của đơn khác. Mã trên hóa đơn khác mã yêu cầu đang mở. | Do người dùng | Do người dùng | Có | Do người dùng |
| 12 | Nhân viên chọn “Hoàn một phần”, nhưng màn hình xác nhận hiển thị toàn bộ giá trị đơn. Nhân viên hủy lệnh trước khi ghi sổ. | Hệ thống | Hệ thống | Có | Hệ thống |
| 13 | Ứng dụng hiển thị tiền hoàn theo từng kiện. Khách gửi ba kiện hiểu số tiền của kiện đầu tiên là tổng tiền hoàn cả đơn. | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 14 | Khách muốn hủy khoản hoàn đã quyết toán ngân hàng. Trợ lý chỉ có quyền tra cứu sau quyết toán và chuyển ca cho kế toán. | Giới hạn hệ thống | Hệ thống | Khác | Giới hạn hệ thống |
| 15 | Kiểm toán cuối quý phát hiện việc làm tròn xuống ở từng dòng phí khiến một số khoản hoàn thiếu vài trăm đồng. Trước đó mọi lệnh đều báo thành công. | Ngầm | Ngầm | Có | Ngầm |
| 16 | Khách chép nhầm một chữ số của mã biên nhận. Khi khách sửa mã, hệ thống tìm được giao dịch. | Do người dùng | Do người dùng | Có | Do người dùng |
| 17 | Nhân viên sửa 80.000 đ thành 60.000 đ. Bản xem trước hiện đúng nhưng lệnh gửi đi vẫn là 80.000 đ. Màn hình đối soát báo lệch ngay. | Hệ thống | Hệ thống | Có | Hệ thống |
| 18 | Thông báo ghi “Hoàn về phương thức ban đầu”. Khách đã đổi thẻ nên liên hệ lại để biết khoản tiền sẽ về thẻ nào. | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Khách yêu cầu hoàn cả khoản thuế do hải quan thu trực tiếp. LogiX chỉ có thẩm quyền hoàn phí vận chuyển của mình. | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Một depot ngừng gửi sự kiện mở lại. Dashboard vẫn hiện tỷ lệ mở lại 0%. Hai tuần sau, khi so với sổ CSKH, nhóm mới phát hiện dữ liệu thiếu. | Hệ thống | Ngầm | Khác | Ngầm |

## 2. Đồng thuận ban đầu

A và B trùng **16/20 ca = 80%**. Bốn ca khác nhau là **3, 8, 14 và 20**. Tử số đếm các hàng có nhãn A bằng nhãn B trước khi thảo luận.

## 3. Quy tắc cho từng ca bất đồng

| Ca | Lý do chọn nhãn thống nhất |
|---:|---|
| 3 | Chọn **Ngữ cảnh** vì giao dịch đang ở đúng trạng thái đã duyệt, nhưng thông báo khiến khách hiểu là ví đã ghi có. |
| 8 | Chọn **Ngữ cảnh** vì thời hạn đúng chính sách nhưng thiếu ngày dự kiến cụ thể để khách biết cuối tuần ảnh hưởng thế nào. |
| 14 | Chọn **Giới hạn hệ thống** vì trợ lý chỉ có quyền tra cứu sau quyết toán và đã chuyển ca đúng thẩm quyền. |
| 20 | Chọn **Ngầm** vì dữ liệu bị thiếu suốt hai tuần mà dashboard vẫn cho ra một tỷ lệ có vẻ hợp lệ. |

## 4. Biện pháp khắc phục cho năm loại lỗi

Các ngưỡng trong bảng là đề xuất của bài mẫu.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Vai trò phụ trách |
|---:|---|---|---|---|
| 11 | Do người dùng | Đối chiếu mã đơn mỗi lần tải hóa đơn. Ghi sự kiện khi lệch và tổng hợp số ca theo tuần. | Hiện hai mã cạnh nhau để khách chọn lại đơn hoặc tải đúng hóa đơn trước khi gửi. | PM trợ lý hoàn phí |
| 17 | Hệ thống | Trước mỗi lần ghi sổ, đối chiếu số tiền đã duyệt với số tiền trong lệnh. Chặn ngay từ 1 giao dịch lệch. | Tạo lệnh từ bản duyệt cuối, lưu phiên bản và số tiền đã duyệt để đối soát. | Trưởng nhóm kỹ thuật thanh toán |
| 3 | Ngữ cảnh | Hằng tuần đếm ca mở lại vì “chưa nhận tiền” sau thông báo “Đã xử lý”. Với mỗi ca, so thời điểm thông báo và thời điểm ví ghi có. | Gửi “Đã duyệt hoàn tiền” sau bước duyệt. Gửi “Tiền đã vào ví” khi ví xác nhận ghi có. | Trưởng nhóm CSKH |
| 14 | Giới hạn hệ thống | Với mỗi yêu cầu hủy sau quyết toán, báo trưởng ca nếu quá 15 phút vẫn thiếu mã bàn giao kế toán. | Chuyển mã giao dịch, số tiền và thời điểm quyết toán cho kế toán. Gửi khách mã tiếp nhận. | Trưởng nhóm vận hành |
| 20 | Ngầm | Hằng ngày đối chiếu số lượt mở lại theo depot giữa sổ CSKH và kho sự kiện. Báo khi sổ có ít nhất 1 lượt còn kho ghi 0. | Đánh dấu depot đang thiếu dữ liệu, khôi phục luồng sự kiện, nạp bù rồi tính lại chỉ số. | Trưởng nhóm dữ liệu |
