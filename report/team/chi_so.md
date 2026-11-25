# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | Số yêu cầu có `dong_trong_24h = 1` và `mo_lai_trong_7_ngay = 0` / tổng số yêu cầu | 994 / 1.200 = **82,83%** |
| Dùng | Tỉ lệ bỏ qua gợi ý (sửa hoặc bỏ) | Trong các yêu cầu có `duoc_xem_lai = 1`, đếm yêu cầu có `quyet_dinh_xem_lai` là `sua` hoặc `bo` / số yêu cầu đã xem lại | (41 sửa + 7 bỏ) / 177 = **27,12%** |
| An toàn | Tỉ lệ lỗi lọt đến khách, đo bằng số yêu cầu mở lại trong 7 ngày | Số yêu cầu có `mo_lai_trong_7_ngay = 1` / tổng số yêu cầu | 51 / 1.200 = **4,25%** |
| Dùng | Nhóm tự đề xuất: tỉ lệ yêu cầu có nhân viên mở gợi ý | Số yêu cầu ở nhánh trợ lý có ít nhất một lần mở gợi ý / tổng số yêu cầu được gán vào nhánh trợ lý | Đo trong pilot |
| An toàn | Nhóm tự đề xuất: tỉ lệ hoàn khác số tiền đã duyệt | Số yêu cầu có tiền thực chi khác tiền đã duyệt / số yêu cầu hoàn tiền được kiểm tra trong mẫu ngẫu nhiên hằng tuần | Đo trong pilot |

Ba tỉ lệ trên mô tả đợt chạy thử. Pilot sẽ so sánh hai nhánh trong cùng thời gian để ước tính tác động của trợ lý. [Dữ liệu chạy thử](../../src/logix_requests.csv)

## Danh sách event

Mỗi event có `event_id`, `occurred_at`, `request_id` và `trace_id`. Hệ thống tạo trace khi tiếp nhận yêu cầu ở cả hai nhánh. Mỗi lần chạy lại có `run_id` riêng và liên kết về cùng yêu cầu gốc.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `request_assigned` | Dịch vụ phân bổ | `trace_id`, `arm`, `depot`, `loai`, `created_at` | Khi gán yêu cầu vào một nhánh pilot |
| `agent_run_completed` | Agent | `trace_id`, `run_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status` | Sau mỗi lần chạy, kể cả lần lỗi |
| `suggestion_opened` | Giao diện CSKH | `trace_id`, `staff_id`, `suggestion_id` | Khi nhân viên mở gợi ý |
| `review_completed` | Giao diện CSKH | `trace_id`, `staff_id`, `final_decision` (`giu`, `sua`, `bo`), `review_minutes` | Khi nhân viên chốt quyết định xem lại |
| `rework_completed` | Hệ thống CSKH | `trace_id`, `staff_id`, `rework_minutes` | Khi nhân viên hoàn tất làm lại |
| `ticket_closed` | Hệ thống quản lý yêu cầu | `trace_id`, `closed_at` | Khi đóng yêu cầu |
| `ticket_reopened` | Hệ thống quản lý yêu cầu | `trace_id`, `reopened_at`, `reason` | Khi mở lại yêu cầu |
| `refund_audited` | Kế toán đối soát | `trace_id`, `sample_week`, `sample_type`, `paid_vnd`, `approved_vnd` | Khi hoàn tất kiểm tra một yêu cầu trong mẫu tuần |

**Kiểm tra chéo.** Nối các event bằng `request_id`, đếm mỗi yêu cầu một lần trong nhánh đã gán. Với hai chỉ số có cửa sổ 7 ngày, chỉ chốt kết quả khi đủ thời gian theo dõi.

- **Đóng đúng hạn và không mở lại.** Từ `request_assigned`, so `created_at` với `closed_at` của `ticket_closed`. Đếm yêu cầu đóng trong 24 giờ và không có `ticket_reopened` trong 7 ngày sau khi đóng. Mẫu số là toàn bộ yêu cầu đã gán.
- **Bỏ qua gợi ý.** Lấy quyết định cuối của `review_completed` trên từng yêu cầu. Chia số yêu cầu kết thúc bằng `sua` hoặc `bo` cho tổng số yêu cầu có event này.
- **Mở lại trong 7 ngày.** Ghép `ticket_closed` với `ticket_reopened`, đếm yêu cầu có lần mở lại trong 7 ngày sau khi đóng. Lấy mẫu số từ `request_assigned`.
- **Mở gợi ý.** Lọc nhánh trợ lý trong `request_assigned`, rồi tính tỉ lệ yêu cầu có ít nhất một `suggestion_opened`.
- **Hoàn khác số tiền đã duyệt.** Trong `refund_audited`, lọc mẫu ngẫu nhiên theo `sample_type` và tuần. Tính tỉ lệ yêu cầu có `paid_vnd` khác `approved_vnd`.

## E2 · Rủi ro kinh tế

Chi phí theo kịch bản lấy từ B1 và B4. Ngưỡng dừng mở rộng lấy từ kế hoạch pilot của nhóm. [Bảng chi phí](bang_chi_phi.md) · [Kế hoạch pilot](pilot_plan.yaml)

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | B1 trên toàn mẫu cho chi phí **6.787 đ/việc thành công**, tăng **51,8%** (simulated). | Hằng tuần, đếm yêu cầu có `rework_completed` trên mỗi 100 yêu cầu ở nhánh trợ lý, tách theo loại. | Rà trace các yêu cầu làm lại. Dừng mở rộng nếu chi phí biến đổi vượt 8.000 đ/việc thành công trong 2 tuần liên tiếp (ngưỡng simulated). | PM trợ lý hoàn phí |
| Phải xem lại mọi kết quả OK | B4 trong phạm vi pilot cho **11.743 đ/việc thành công** nếu làm lại mất 9 phút/ca. Với 15,3 phút/ca, chi phí lên **12.415 đ/việc**, vượt mức tự làm 12.000 đ (simulated). | Theo dõi tỉ lệ xem lại và số phút xem lại, làm lại mỗi tuần. Ở mức 15,3 phút làm lại/ca, ngưỡng hoà vốn là 4,80 phút xem lại (simulated). | Đo `review_minutes` và `rework_minutes` từ tuần 1. Rà các yêu cầu tốn nhiều thời gian trước khi đề xuất thay đổi chính sách xem lại. | Trưởng nhóm CSKH |
