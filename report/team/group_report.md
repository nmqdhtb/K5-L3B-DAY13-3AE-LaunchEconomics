# Báo cáo nhóm 3AE · Gate 2a

## 1. Nhóm thực hiện

Lớp L3B · Nguyễn Minh Quân (nhóm trưởng), Nguyễn Ngọc Quang, Trương Thu Hà.

## 2. Mục tiêu và cách tiếp cận

LogiX-VN cần quyết định loại yêu cầu hoàn phí nào đáng đưa vào pilot. Nhóm đối chiếu 1.200 yêu cầu với 1.624 lần chạy qua mã yêu cầu, tính cả chi phí của các lần thử lại và thời gian nhân viên xử lý.

## 3. Giải pháp

| Nhiệm vụ | Cách thực hiện và bằng chứng |
| --- | --- |
| A–B | Tính chi phí theo loại yêu cầu, thử 9 kịch bản độ nhạy và so sánh giới hạn 1–3 lần chạy sau khi cộng tiền nhân viên tiếp quản. [Bảng chi phí](bang_chi_phi.md) |
| C | Hà và Quang trùng 7/20 ca khi gắn độc lập (35%). Nhóm đã viết lại định nghĩa, ghi quy tắc cho 13 ca lệch và lập bảng khắc phục đủ 5 loại. Nhãn chốt khớp đáp án 20/20 ca. [Bảng lỗi](bang_loi.md) |
| D | Chia ngẫu nhiên theo yêu cầu trong cùng depot và loại hàng, tỷ lệ 1:1. Cần 1.251 yêu cầu mỗi nhánh, đủ thời gian theo dõi. [Kế hoạch pilot](pilot_plan.yaml) |
| E | Đặc tả 5 chỉ số, 8 sự kiện và 2 rủi ro kinh tế. [Chỉ số và rủi ro](chi_so.md) |

## 4. Kết quả và đề xuất

**Go có điều kiện** cho yêu cầu nội địa và hàng nặng tại D01–D06. Trên toàn mẫu, chi phí là 4.472 đ/việc thành công, hoặc 5.865 đ/yêu cầu khi tính cả nhân viên tiếp quản (simulated). Với 100% kết quả OK được xem lại và 15,3 phút làm lại/ca, phạm vi pilot có thể tốn 12.415 đ/việc (simulated), vượt mốc tự làm 12.000 đ.

Trong đợt chạy thử, 994/1.200 yêu cầu đạt chỉ số chính (82,83%), 48/177 gợi ý đã xem bị sửa hoặc bỏ (27,12%) và 51/1.200 yêu cầu mở lại (4,25%). Điều kiện mở pilot và người có quyền dừng được ghi trong [hồ sơ Gate 2a](ho_so_launch_v0.md).

**3AE chấm 5AE.** Cả ba tiêu chí đạt 10/10, tổng **30/30**. Hội đồng chọn **Go có điều kiện**. Phiếu ghi lý do, câu hỏi về tỷ lệ mở lại của `hang_nang` và câu trả lời của 5AE. [Phiếu chấm 5AE](phieu_cham.md)

**Kết quả hội đồng chấm 3AE.** Nhóm đang chờ phiếu hoặc biên bản từ hội đồng.

## 5. Khó khăn và cách xử lý

Một yêu cầu có thể chạy nhiều lần. Nhóm cộng token và tool ở cấp lần chạy, sau đó đếm kết quả ở cấp yêu cầu. Phép kiểm 5.600 lượt gọi tool × 15 đ = 84.000 đ đối chiếu trực tiếp với bảng A2.

## 6. Đóng góp

Quân phụ trách mô hình chi phí, kiểm số và thiết kế pilot. Hà phụ trách bảng lỗi. Quang tổng hợp chỉ số, rủi ro và hồ sơ Gate 2a. Chi tiết và bằng chứng ở [phân công nhóm](../../TEAM.md).

## 7. Hạn chế và hướng cải thiện

Đợt chạy thử thiếu nhóm đối chứng. Pilot sẽ đo chênh lệch giữa hai nhánh cùng thời gian, theo dõi truy cập chéo và dùng phút xem lại, làm lại thực tế để cập nhật dự toán sau tuần đầu.

## 8. Tài liệu tham khảo

[Dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md) · [Hướng dẫn Lab 13](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md) · [Mã tính toán](../../src/lab13.py)
