# Chỉ số, sự kiện và rủi ro kinh tế

## E1 · Chỉ số

Đơn vị đếm là yêu cầu hoàn phí (`request_id`). Mẫu chạy thử có 1.200 yêu cầu. Các tỷ lệ dưới đây mô tả đợt chạy thử. Pilot sẽ so sánh hai nhánh đối chứng và trợ lý trong cùng thời gian.

| Loại | Chỉ số | Tử số / mẫu số | Kết quả từ CSV |
| --- | --- | --- | ---: |
| Chính | Đóng trong 24 giờ và không mở lại trong 7 ngày | Đếm dòng có `dong_trong_24h=1` và `mo_lai_trong_7_ngay=0` / tổng số dòng | 994 / 1.200 = **82,83%** |
| Sử dụng | Gợi ý bị sửa hoặc bỏ sau khi xem | Trong các dòng có `duoc_xem_lai=1`, đếm quyết định `sua` hoặc `bo` / số dòng đã xem | (41 + 7) / 177 = **27,12%** |
| An toàn | Yêu cầu mở lại trong 7 ngày | Đếm dòng có `mo_lai_trong_7_ngay=1` / tổng số dòng | 51 / 1.200 = **4,25%** |
| Sử dụng · đề xuất | Nhân viên mở gợi ý | Yêu cầu có ít nhất một lượt mở gợi ý / toàn bộ yêu cầu phân vào nhánh trợ lý | Đo trong pilot |
| An toàn · đề xuất | Hoàn sai số tiền trong mẫu kiểm toán | Số yêu cầu có tiền thực hoàn khác tiền được duyệt / số yêu cầu hoàn tiền được kiểm tra trong mẫu ngẫu nhiên hằng tuần | Đo trong pilot |

## Sự kiện cần ghi trong pilot

Mỗi sự kiện dưới đây có `event_id`, `occurred_at`, `request_id` và `trace_id`. Hệ thống tạo trace khi tiếp nhận yêu cầu ở cả hai nhánh. Mỗi lần agent chạy lại ghi thêm `run_id` và liên kết trace của lần chạy với yêu cầu gốc.

| Sự kiện | Nơi ghi | Thời điểm | Thuộc tính bổ sung |
| --- | --- | --- | --- |
| `request_assigned` | Dịch vụ phân bổ | Khi yêu cầu được chọn và gán nhánh | arm, depot, loai, created_at |
| `agent_run_completed` | Agent | Sau mỗi lần chạy, kể cả lỗi | run_id, attempt, tokens_in, tokens_out, tool_calls, status |
| `suggestion_opened` | Giao diện CSKH | Khi nhân viên mở gợi ý | staff_id, suggestion_id |
| `review_completed` | Giao diện CSKH | Khi nhân viên chốt quyết định xem lại | staff_id, final_decision (giu/sua/bo), review_minutes |
| `rework_completed` | Hệ thống CSKH | Khi nhân viên hoàn tất làm lại | staff_id, rework_minutes |
| `ticket_closed` | Hệ thống ticket | Khi đóng yêu cầu | closed_at |
| `ticket_reopened` | Hệ thống ticket | Khi mở lại | reopened_at, reason |
| `refund_audited` | Kế toán đối soát | Khi hoàn tất kiểm tra một yêu cầu trong mẫu tuần | sample_week, paid_vnd, approved_vnd |

**Cách tính từ sự kiện.** Đếm mỗi yêu cầu một lần trong nhánh đã gán. Chỉ chốt hai chỉ số liên quan mở lại khi các yêu cầu đã đủ thời gian quan sát.

| Chỉ số | Sự kiện dùng để tính |
| --- | --- |
| Đóng đúng hạn, không mở lại | Từ `request_assigned`, kiểm tra `ticket_closed` trong 24 giờ và lịch sử `ticket_reopened` trong cửa sổ 7 ngày sau khi đóng. |
| Sửa hoặc bỏ | Dùng quyết định cuối của `review_completed` trên từng yêu cầu đã xem. |
| Mở lại trong 7 ngày | Nối `ticket_closed` và `ticket_reopened` để xét cửa sổ 7 ngày, lấy mẫu số từ `request_assigned`. |
| Mở gợi ý | Ghép `suggestion_opened` với `request_assigned` ở nhánh trợ lý. |
| Hoàn sai số tiền | So sánh paid_vnd và approved_vnd trong `refund_audited`. |

## E2 · Rủi ro kinh tế

| Rủi ro | Tác động theo kịch bản | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | B1 toàn mẫu đạt 6.787 đ/việc, tăng 51,8% (simulated). | Đếm `rework_completed` theo tuần trên mỗi 100 yêu cầu, tách theo loại. | Rà các trace làm lại. Nếu chi phí vượt 8.000 đ/việc trong 2 tuần, dừng mở rộng theo kế hoạch pilot (ngưỡng simulated). | PM trợ lý hoàn phí |
| Phải xem lại mọi kết quả OK | B4 trong phạm vi pilot đạt 11.743 đ/việc ở 9 phút làm lại. Với 15,3 phút làm lại, chi phí đạt 12.415 đ/việc, vượt mức tự làm 12.000 đ (simulated). | Theo dõi tỷ lệ xem lại và số phút xem, làm lại thực đo mỗi tuần. Ở giả định 15,3 phút, xem lại trên 4,80 phút vượt hòa vốn (simulated). | Đo thời lượng thực từ tuần 1, rà nhóm ca tốn thời gian trước khi đề nghị đổi chính sách xem lại. | Trưởng nhóm CSKH |

Nguồn tính chi phí và phạm vi của từng kịch bản nằm trong [bảng chi phí](bang_chi_phi.md).
