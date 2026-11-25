# Team

## Thông tin nhóm

- Tên nhóm: 3AE
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-3AE-LaunchEconomics` (xem [quy định nộp bài](SUBMISSION.md)).
- URL repo, nhánh nộp, commit chốt: [GitHub của nhóm 3AE](https://github.com/nmqdhtb/K5-L3B-DAY13-3AE-LaunchEconomics), nhánh `main`. Bản chốt là commit cuối cùng nhóm push lên `main` trước hạn nộp.

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
| 1 | Nguyễn Minh Quân | 2A202603794 | 26ai.quannm10@vinuni.edu.vn | nmqdhtb | Nhóm trưởng, người viết code và người kiểm số |
| 2 | Nguyễn Ngọc Quang | 2A202603773 | 26ai.quangnn3@vinuni.edu.vn | shoxieje | Người gắn nhãn 2, kiêm giữ hồ sơ |
| 3 | Trương Thu Hà | 2A202603780 | 26ai.hattt@vinuni.edu.vn | TruongThuHa | Người gắn nhãn 1 |

Bốn vai của lab:

- **Người viết code:** Quân viết và chạy `src/lab13.py` để lập mô hình chi phí, tính độ nhạy và cỡ mẫu pilot.
- **Người kiểm số:** Quân tính tay chi phí gọi tool từ CSV, đối chiếu với kết quả chạy và điền bảng chi phí.
- **Người gắn nhãn 1:** Hà theo dõi điều kiện hoàn thành CP1–CP5 và gắn nhãn độc lập 20 ca ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** Quang gắn nhãn độc lập cùng 20 ca, phụ trách bảng chỉ số và tổng hợp hồ sơ launch.

Mẫu lab yêu cầu đổi người viết code sau giờ giải lao để ít nhất hai thành viên tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên có báo cáo riêng theo mẫu `report/team/MSSV_HoTen.md` và tự nộp cùng link repo nhóm trên LMS.

## NguyenMinhQuan-2A202603794

### Phần việc phụ trách

- Viết mô hình chi phí A–B, kiểm số, tính cỡ mẫu D1 và lập kế hoạch pilot. Tổng hợp báo cáo nhóm và kết quả duyệt chéo.

### Đóng góp cụ thể

- Hoàn thiện các bảng A1–A4, B1–B4 và kiểm tra chi phí gọi tool bằng phép tính 5.600 lượt × 15 đ = 84.000 đ.
- Ghi kết quả 3AE chấm 5AE vào báo cáo nhóm và phiếu chấm. 3AE cho 5AE 30/30 điểm và kết luận **Go có điều kiện**.

### Bằng chứng

- Commit `ea303ab`. [Mã tính toán](src/lab13.py) · [Bảng chi phí](report/team/bang_chi_phi.md) · [Kế hoạch pilot](report/team/pilot_plan.yaml)
- Commit `c64bb1a`. [Báo cáo nhóm](report/team/group_report.md) · [Phiếu 3AE chấm 5AE](report/team/phieu_cham.md) · [Báo cáo cá nhân của Quân](report/team/2A202603794_NguyenMinhQuan.md)

## NguyenNgocQuang-2A202603773

### Phần việc phụ trách

- Gắn nhãn độc lập ở CP3, phụ trách chỉ số và rủi ro kinh tế, tổng hợp hồ sơ launch v0.

### Đóng góp cụ thể

- Gắn nhãn đủ 20 ca trước khi so kết quả với Hà.
- Đối chiếu 3 chỉ số E1 với CSV, đặc tả 8 sự kiện có `trace_id` và ghi 2 rủi ro kinh tế. Tổng hợp hồ sơ launch đủ 7 mục với đề xuất **Go có điều kiện**, kiểm tra quy tắc nộp bài và gộp PR #1.

### Bằng chứng

- Bộ nhãn độc lập ở commit `f5e5d9b`. [Bảng lỗi CP3](report/team/bang_loi.md)
- PR #1 được gộp ở commit `7073d86`. [Chỉ số và rủi ro](report/team/chi_so.md) · [Hồ sơ launch v0](report/team/ho_so_launch_v0.md) · [Báo cáo cá nhân của Quang](report/team/2A202603773_NguyenNgocQuang.md)

## TruongThuHa-2A202603780

### Phần việc phụ trách

- Gắn nhãn độc lập ở CP3, đối chiếu kết quả với Quang, rà bảng khắc phục và kiểm tra điều kiện hoàn thành CP1–CP5.

### Đóng góp cụ thể

- Gắn nhãn 20 ca và ghi nhận hai người trùng 7/20 ca (35%). Viết lại định nghĩa cho 5 loại lỗi và ghi quy tắc cho từng ca trong 13 ca bất đồng. Nhãn sau thống nhất khớp đáp án 20/20.
- Rà 5 biện pháp khắc phục, bổ sung tên sự kiện dùng để phát hiện lỗi. Kiểm tra ba phép thử A1 và khả năng đọc tệp YAML của kế hoạch pilot.

### Bằng chứng

- Bộ nhãn độc lập ở commit `55d9ecc`, kết quả đối chiếu ở `30090cf` và phần rà bảng khắc phục ở `138ef37`. [Bảng lỗi CP3](report/team/bang_loi.md) · [Báo cáo cá nhân của Hà](report/team/2A202603780_TruongThuHa.md)
