# Báo cáo nhóm

## 1. Thông tin nhóm

- Tên nhóm: 3AE
- Lớp: L3B
- Thành viên: Nguyễn Minh Quân (nhóm trưởng), Nguyễn Ngọc Quang và Trương Thu Hà. [Phân công nhóm](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

Nhóm đánh giá loại yêu cầu hoàn phí nào phù hợp để thử nghiệm trợ lý tại LogiX-VN. Nhóm ghép 1.200 yêu cầu với 1.624 lần chạy theo mã yêu cầu, tính chi phí chạy lại và thời gian nhân viên xử lý, rồi so sánh với chi phí nhân viên tự làm.

## 3. Giải pháp

| Nhiệm vụ | Cách thực hiện và bằng chứng |
| --- | --- |
| A · Chi phí | Tính chi phí mỗi việc thành công theo loại yêu cầu. Phân bổ chi phí cố định cho phạm vi pilot ở hai mức sản lượng. [Bảng chi phí](bang_chi_phi.md) |
| B · Độ nhạy | Thử 9 kịch bản. Khi tính cả tiền nhân viên tiếp quản, giới hạn 2 lần chạy cho tổng chi phí thấp nhất trong 3 phương án (simulated). [Bảng độ nhạy](bang_chi_phi.md) |
| C · Lỗi | Hai người gắn nhãn độc lập trùng 7/20 ca (35%). Nhóm sửa định nghĩa, giải thích 13 ca lệch và đề xuất biện pháp cho 5 loại lỗi. Nhãn chốt khớp đáp án 20/20. [Bảng lỗi](bang_loi.md) |
| D · Pilot | Chia ngẫu nhiên 1:1 theo yêu cầu trong từng depot và loại hàng. Cần 1.251 yêu cầu mỗi nhánh để phát hiện chênh lệch 5 điểm phần trăm. [Kế hoạch pilot](pilot_plan.yaml) |
| E · Chỉ số và hồ sơ | Đặc tả 5 chỉ số, 8 sự kiện và 2 rủi ro kinh tế làm cơ sở cho đề xuất Gate 2a. [Chỉ số và rủi ro](chi_so.md) · [Hồ sơ launch](ho_so_launch_v0.md) |

## 4. Kết quả

**3AE đề xuất Go có điều kiện** cho yêu cầu nội địa và hàng nặng tại D01–D06. Trên toàn mẫu, trước chi phí cố định, chi phí là 4.472 đ/việc thành công và 5.865 đ/yêu cầu khi tính cả nhân viên tiếp quản (simulated). Trong phạm vi pilot, nếu nhân viên xem lại mọi kết quả OK và mất 15,3 phút làm lại mỗi ca, chi phí lên tới 12.415 đ/việc thành công (simulated), vượt mức tự làm 12.000 đ.

Trong đợt chạy thử, 994/1.200 yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày (82,83%). Nhân viên sửa hoặc bỏ 48/177 gợi ý đã xem (27,12%). Có 51/1.200 yêu cầu mở lại trong 7 ngày (4,25%).

**3AE đã hoàn thành chấm 5AE.** 3AE cho 5AE 10/10 ở mỗi tiêu chí, tổng **30/30**, và kết luận **Go có điều kiện**. Phiếu ghi câu hỏi của 3AE về tỷ lệ mở lại của các yêu cầu hàng nặng và câu trả lời của 5AE. [Phiếu 3AE chấm 5AE](phieu_cham.md)

**Điểm 3AE nhận từ hội đồng.** Hồ sơ hiện chưa có phiếu hoặc biên bản ghi điểm của 3AE.

## 5. Khó khăn và cách xử lý

Một yêu cầu có thể chạy nhiều lần. Nhóm cộng token và tool ở cấp lần chạy, sau đó đếm kết quả ở cấp yêu cầu. Phép kiểm 5.600 lượt gọi tool × 15 đ = 84.000 đ đối chiếu trực tiếp với bảng A2.

## 6. Tổng hợp đóng góp

Quân viết mô hình chi phí, kiểm số, thiết kế pilot và tổng hợp báo cáo. Hà và Quang gắn nhãn độc lập. Hà tổng hợp bảng lỗi, Quang phụ trách chỉ số, rủi ro và hồ sơ Gate 2a. [Chi tiết đóng góp của từng thành viên](../../TEAM.md)

## 7. Hạn chế và hướng cải thiện

Đợt chạy thử thiếu nhóm đối chứng. Pilot sẽ đo chênh lệch giữa hai nhánh cùng thời gian, theo dõi truy cập chéo và dùng phút xem lại, làm lại thực tế để cập nhật dự toán sau tuần đầu.

## 8. Tài liệu tham khảo

[Dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md) · [Hướng dẫn Lab 13](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md) · [Mã tính toán](../../src/lab13.py)
