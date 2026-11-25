# Báo cáo cá nhân — Trương Thu Hà — 2A202603780

## 1. Thông tin thành viên

- Họ tên: Trương Thu Hà
- MSSV: 2A202603780
- Email: 26ai.hattt@vinuni.edu.vn
- Vai trong nhóm: người gắn nhãn 1

## 2. Phần việc phụ trách

- Theo dõi điều kiện "Xong khi" của CP1–CP5 cho cả nhóm.
- Gắn nhãn độc lập 20 ca lỗi ở CP3, so nhãn với Nguyễn Ngọc Quang và tổng hợp `report/team/bang_loi.md`.

## 3. Đóng góp cụ thể

- Kiểm tra "Xong khi": chạy `lab13.py` thấy ba phép thử ĐẠT (1,20 · 1,25 · 1,25); kiểm `pilot_plan.yaml` đọc được và không còn dấu `?`; báo nhóm vế "KHÔNG THÌ" của luật dừng cần ghi việc bị cấm.
- Gắn nhãn độc lập 20 ca, không trao đổi trước khi so (cột "Nhãn người 1" trong `report/team/bang_loi.md`).
- So nhãn với Quang: đồng thuận ban đầu 7 / 20 = 35%, dưới mốc 80%. Viết lại định nghĩa năm loại lỗi và một câu quy tắc cho từng ca trong 13 ca lệch (1, 2, 3, 7, 8, 9, 10, 12, 13, 17, 18, 19, 20).
- Rà bảng khắc phục 5 ca do Quân soạn nháp: bỏ khối thu gọn, bổ sung tên event cho cột phát hiện, ghi rõ người soạn và người rà.

## 4. Bằng chứng

- Commit `138ef37` "CP3: bang loi - nguoi gan nhan, bang khac phuc co event" trên nhánh main.
- File `report/team/bang_loi.md` (cột "Nhãn người 1", tỉ lệ đồng thuận, bảng khắc phục).

## 5. Công cụ AI đã dùng

- Codex: hỗ trợ đếm lại số ca trùng từ hai cột nhãn gốc, đối chiếu nhãn chốt với bảng tham khảo và cập nhật số liệu CP3 trong hồ sơ nhóm. Có thể kiểm lại bằng cách đếm các dòng “Có” rồi chia cho 20.
- Claude: giải thích nội dung lab, hướng dẫn thao tác VS Code và Git, rà định dạng file markdown. Không dùng AI để gắn nhãn 20 ca.
- Cách tự kiểm tra: đối chiếu định nghĩa 5 loại lỗi với slide buổi sáng; chạy các lệnh kiểm tra trong `CHECKPOINTS.md`; xem bản hiển thị (Cmd + K, V) trước khi commit.

## 6. Tự đánh giá

Mình làm tốt ở phần đồng bộ giữa các file: thêm tên event vào bảng khắc phục cho khớp với danh sách event trong `chi_so.md`, và ghi rõ ai soạn nháp, ai rà soát để không nhận công thay người khác. Điểm chưa tốt là lần sửa đầu tiên mình dán nội dung từ chế độ xem trước vào `bang_loi.md`, làm file mất hết ký hiệu markdown (`#`, `|`); mình phát hiện kịp và khôi phục bằng `git restore` trước khi push nên bản trên GitHub không bị hỏng. Bộ nhãn độc lập của mình chỉ trùng 7/20 ca với Quang; các ca lệch chủ yếu do mình gắn theo chỗ cần sửa thay vì nguyên nhân gốc (ví dụ ca 1, 9 mình chọn Hệ thống/Giới hạn trong khi gốc lỗi là khách nhập sai). Lần sau mình sẽ luôn chạy `git pull` trước khi sửa, chỉ gõ trực tiếp vào file `.md` với bản xem trước mở song song (Cmd + K, V), và kiểm tra lại bằng `git status` trước khi commit.
