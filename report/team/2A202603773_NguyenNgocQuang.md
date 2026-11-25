# Báo cáo cá nhân — NguyenNgocQuang-2A202603773

## 1. Thông tin thành viên

- Họ tên: Nguyễn Ngọc Quang
- MSSV: 2A202603773
- Email: 26ai.quangnn3@vinuni.edu.vn
- Vai trong nhóm: Người gắn nhãn 2, kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- Giữ và tổng hợp hồ sơ `report/team/ho_so_launch_v0.md` đủ 7 mục theo chuẩn Gate 2a.
- Hoàn thiện `report/team/chi_so.md` gồm bảng chỉ số (E1), danh sách sự kiện có `trace_id`, kiểm tra chéo khả năng tính chỉ số từ sự kiện và bảng rủi ro kinh tế (E2).
- Gắn nhãn độc lập 20 ca lỗi (CP3) để đối chiếu đồng thuận cùng Người gắn nhãn 1 (Trương Thu Hà) trong `report/team/bang_loi.md`, và tham gia ghi `report/team/phieu_cham.md` khi duyệt chéo.
- Rà soát tính nhất quán số liệu, nhãn `simulated`, vai trò phụ trách và tuân thủ quy tắc nộp bài trước khi gộp vào `main`.

## 3. Đóng góp cụ thể

- **Chỉ số và sự kiện (`report/team/chi_so.md`):**
  - Tính và kiểm tra lại 3 chỉ số trên 1.200 yêu cầu từ `src/logix_requests.csv`: chỉ số chính `994 / 1.200 = 82,83%`, chỉ số sử dụng `(41 + 7) / 177 = 27,12%`, chỉ số an toàn `51 / 1.200 = 4,25%`, diễn đạt đúng phạm vi mô tả đợt chạy thử (không suy diễn nhân quả).
  - Đề xuất bổ sung 2 chỉ số đo trong pilot: tỷ lệ nhân viên mở gợi ý (sử dụng) và tỷ lệ hoàn sai số tiền trong mẫu kiểm toán hằng tuần (an toàn).
  - Đặc tả 8 sự kiện đều có `event_id`, `occurred_at`, `request_id` và `trace_id`, kèm bảng kiểm tra chéo chứng minh đủ dữ liệu tính cả 5 chỉ số và ghi nhận `review_minutes`, `rework_minutes` thực tế thay cho dữ liệu `simulated`.
  - Lập bảng rủi ro kinh tế (E2) gắn với bảng độ nhạy trong `bang_chi_phi.md`: số ca làm lại gấp đôi (`6.787 đ/việc`, tăng `51,8%`, `simulated`) và xem lại 100% ở mức 15,3 phút làm lại (`12.415 đ/việc`, ngưỡng hòa vốn `4,80 phút` xem lại, `simulated`).
- **Hồ sơ launch v0 (`report/team/ho_so_launch_v0.md`):**
  - Tổng hợp đầy đủ 7 mục trong một trang với trạng thái chuẩn (`Xong, có bằng chứng`, `Giả lập`, `Chưa`), gắn nhãn `simulated` cho mọi con số từ cột giả lập và gán một vai trò cụ thể cho từng mục.
  - Chốt đề xuất **Go có điều kiện** kèm 3 điều kiện có ngày kiểm tra (`30/11/2026`, `08/12/2026`, `05/01/2027`) và người phụ trách khớp với `report/team/pilot_plan.yaml`.
- **Kiểm tra và gộp nhánh:**
  - Rà soát toàn bộ bộ hồ sơ theo `RUBRIC.md` và `SUBMISSION.md`, tạo nhánh `feat/finish-task`, mở PR #1, squash-merge vào `main` và dọn dẹp nhánh làm việc.

## 4. Bằng chứng

- File đã hoàn thiện: `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`.
- Pull Request & commit trên repo nhóm: PR #1 (`https://github.com/nmqdhtb/K5-L3B-DAY13-3AE-LaunchEconomics/pull/1`), commit `7073d86` (`feat: finish task`).
- Kết quả tự kiểm tra: đối chiếu trực tiếp 3 chỉ số E1 từ `src/logix_requests.csv` khớp 100% (`82,83%`, `27,12%`, `4,25%`); kiểm tra không vi phạm quy tắc 5 trong `report/team/` và không còn dấu `?` ngoài chú thích trong `pilot_plan.yaml`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity (trợ lý lập trình AI).
- **Mục đích sử dụng:** Rà soát cấu trúc bài lab, đối chiếu yêu cầu trong `RUBRIC.md` và `SUBMISSION.md`, chạy script Python kiểm tra chéo số liệu từ `src/logix_requests.csv`, kiểm tra quy tắc định dạng/nhãn `simulated`, hỗ trợ thao tác Git/GitHub PR và soạn báo cáo cá nhân.
- **Cách tự kiểm tra:** Đối chiếu trực tiếp từng con số giữa `chi_so.md`, `ho_so_launch_v0.md`, `bang_chi_phi.md` và `pilot_plan.yaml`; chạy lệnh kiểm tra trên CSV gốc và kiểm tra `git diff` trước khi mở PR và squash-merge.

## 6. Tự đánh giá

- **Điểm làm tốt:** Chủ động theo sát cấu trúc hồ sơ Gate 2a, đảm bảo mọi số liệu nhất quán giữa các file, phân biệt rõ số đo thực và số `simulated`, và chỉ rõ các điều kiện chặn trước khi triển khai pilot.
- **Kết quả CP3.** Mục 5 của hồ sơ đã ghi nhận mức đồng thuận ban đầu 7/20 (35%). Sau khi nhóm viết lại định nghĩa và xử lý 13 ca bất đồng, nhãn chốt khớp đáp án 20/20. [Bảng lỗi](bang_loi.md)
- **Duyệt chéo.** Nhóm 3AE đã chấm 5AE 30/30, kết luận **Go có điều kiện** và ghi lại câu hỏi cùng câu trả lời của 5AE. [Phiếu chấm](phieu_cham.md)
