# Chi phí trợ lý hoàn phí LogiX-VN

Số liệu tính bằng `src/lab13.py`, đơn vị tiền là đồng. Chi phí biến đổi gồm token, tool, xem lại và làm lại. Chỉ bảng A4 cộng chi phí cố định.

## A1 · Kiểm tra công thức chạy lại

| Phép thử với p = 0,8 | Tính tay | Python |
| --- | --- | ---: |
| Số lần chạy trung bình, tối đa 2 lần | 1 + 0,2 | 1,20 |
| Số lần chạy trung bình đến khi đúng | 1 / 0,8 | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | (1 + 0,2 + 0,04) / (1 − 0,2³) | 1,25 |

## A2 · Chi phí trên toàn mẫu

| Khoản | Kết quả | Cách tính |
| --- | ---: | --- |
| Token | 245.585 đ | 26 đ/1.000 token vào, 130 đ/1.000 token ra |
| Tool | 84.000 đ | Kiểm độc lập từ CSV, 5.600 lượt gọi × 15 đ |
| Trong đó, token và tool của lần chạy 2–3 | 93.804 đ | Đã nằm trong hai khoản trên |
| Xem lại (simulated) | 1.780.000 đ | 890 phút × 2.000 đ |
| Làm lại (simulated) | 2.264.000 đ | 1.132 phút × 2.000 đ |
| Tổng chi phí (simulated) | 4.373.585 đ | Cộng token, tool, xem lại và làm lại |
| Số việc thành công | 978 | Đếm yêu cầu có kết quả thành công |
| Chi phí mỗi việc thành công (simulated) | 4.472 đ | 4.373.585 / 978 |
| Hóa đơn token và tool mỗi yêu cầu | 274,65 đ | (245.585 + 84.000) / 1.200 |

Chi phí mỗi việc thành công gấp **16,3 lần** hóa đơn mỗi yêu cầu. Làm lại chiếm tỷ trọng cao nhất, **51,8%** tổng chi phí (simulated).

Tính cả nhân viên tiếp quản 222 yêu cầu, chi phí hệ thống là (4.373.585 + 222 × 12.000) / 1.200 = **5.865 đ/yêu cầu**, bằng 0,49 lần mức tự làm (simulated).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Thành công | Lần chạy/yêu cầu | Đ/việc thành công (simulated) | So với 12.000 đ (simulated) |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 | 0,85× |

Chọn nội địa và hàng nặng cho pilot. Quốc tế chỉ đạt 27,3% thành công, tỷ lệ run OK trong các lần thử 1–3 lần lượt là 30,0%, 11,4% và 2,2%. Đối tác có tỷ lệ thành công 54,4%.

## A4 · Phân bổ 40 triệu đồng cố định mỗi tháng

Giữ cơ cấu yêu cầu như mẫu, cứ 1.200 yêu cầu toàn hệ thống có 900 việc thành công thuộc phạm vi pilot.

| Yêu cầu toàn hệ thống/tháng | Việc thành công trong phạm vi | Cố định/việc | Tổng đ/việc (simulated) | So với 12.000 đ (simulated) |
| ---: | ---: | ---: | ---: | ---: |
| 45.000 | 33.750 | 1.185 | 4.599 | 0,38× |
| 22.500 | 16.875 | 2.370 | 5.784 | 0,48× |

Cả hai quy mô vẫn dưới 12.000 đ/việc. Khi lượng việc giảm một nửa, phần cố định tăng thêm 1.185 đ trên mỗi việc thành công.

## B1 · Độ nhạy so với mức gốc 4.472 đ/việc (simulated)

| Kịch bản | Đ/việc thành công (simulated) | Thay đổi (simulated) |
| --- | ---: | ---: |
| Giá token ×2 | 4.723 | +5,6% |
| Giá token ×0,5 | 4.346 | −2,8% |
| Tiền xem lại ×2 | 6.292 | +40,7% |
| Tiền xem lại ×0,5 | 3.562 | −20,3% |
| Tiền làm lại ×2 | 6.787 | +51,8% |
| Tiền làm lại ×0,5 | 3.315 | −25,9% |
| Lương tăng 25% | 5.506 | +23,1% |
| Tối đa 2 lần chạy | 4.237 | −5,2% |
| Tối đa 1 lần chạy | 4.111 | −8,1% |

## B2 · Đổi một cặp và xếp hạng

Giá token và tiền xem lại cùng gấp đôi đưa chi phí lên **6.543 đ/việc**, tăng **46,3%** (simulated). Mô hình cộng chi phí nên hai tác động cộng lại.

Ba yếu tố ảnh hưởng mạnh nhất theo các mức thay đổi của B1 là làm lại (+51,8%), xem lại (+40,7%) và lương (+23,1%) (simulated).

## B3 · Giới hạn chạy lại

| Giới hạn | Tổng chi phí trợ lý (simulated) | Yêu cầu chưa thành công | Tổng chi phí hệ thống (simulated) | Đ/việc thành công (simulated) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 3.621.781 | 319 | 7.449.781 | 4.111 |
| 2 | 4.093.220 | 234 | 6.901.220 | 4.237 |
| 3 | 4.373.585 | 222 | 7.037.585 | 4.472 |

Chọn tối đa **2 lần** để chi phí hệ thống thấp nhất, **6.901.220 đ** (simulated). Giới hạn 1 lần cho chi phí trợ lý mỗi việc thành công thấp nhất nhưng đẩy thêm 85 yêu cầu sang nhân viên.

## B4 · Xem lại 100% trong phạm vi pilot

Với 948 yêu cầu có kết quả OK cần xem 5 phút và 48 ca làm lại mất 9 phút/ca, chi phí đạt **11.743 đ/việc**, bằng 0,98× mức tự làm (simulated). Nếu làm lại mất 15,3 phút/ca, chi phí đạt **12.415 đ**, bằng 1,03× (simulated).

Pilot cần đo phút xem lại và theo dõi mở lại sau 7 ngày. Để hòa vốn, thời gian xem lại trung bình tối đa lần lượt là **5,12 phút** và **4,80 phút** theo hai giả định trên (simulated).
