# Bảng chi phí · Nhiệm vụ A và B

Số liệu tính bằng [mã của nhóm](../../src/lab13.py) từ 1.200 yêu cầu và 1.624 lần chạy. Đơn vị tiền là đồng. Nhãn `simulated` chỉ kết quả sử dụng phút xem lại hoặc làm lại giả lập. Chỉ A4 cộng chi phí cố định.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1 + 0,2 = **1,20** |
| Số lần chạy trung bình, chạy đến khi đúng | 1 / 0,8 = **1,25** |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | (1 + 0,2 + 0,04) / (1 − 0,2³) = **1,25** |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv`, 26 đ/1.000 token vào và 130 đ/1.000 token ra | đo từ trace |
| Tool | 84.000 | `logix_runs.csv`, 5.600 lượt gọi × 15 đ | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | Token và tool của các dòng có `attempt > 1`, đã tính trong hai khoản trên | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated`, 890 phút × 2.000 đ | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated`, 1.132 phút × 2.000 đ | simulated |
| Tổng chi phí | 4.373.585 | Token + tool + xem lại + làm lại | simulated |
| Số việc thành công | 978 việc | Đếm yêu cầu có `ket_qua == 'thanh_cong'` trong `logix_requests.csv` | đo từ trace |
| Chi phí mỗi việc thành công | 4.472 | Tổng chi phí của mọi lần chạy / 978 việc thành công | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,65 | (245.585 + 84.000) / 1.200 yêu cầu | đo từ trace |

- **Chi phí mỗi việc thành công gấp bao nhiêu lần “hoá đơn chia số yêu cầu”?** 4.472 / 274,65 ≈ **16,3 lần** (simulated).
- **Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm?** Làm lại chiếm **51,8%** (simulated), tính bằng 2.264.000 / 4.373.585.

Tính thêm 12.000 đ cho mỗi yêu cầu trong 222 yêu cầu cần nhân viên tiếp quản, chi phí cả hệ thống là (4.373.585 + 222 × 12.000) / 1.200 = **5.865 đ/yêu cầu**, bằng 0,49× mức tự làm (simulated).

## A3 · Tách theo loại yêu cầu

Hai cột chi phí và so sánh với mức tự làm sử dụng phút lao động `simulated`.

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

- **Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không?** Quốc tế tốn 1,88× mức tự làm (simulated). Chạy lại giúp ít vì tỉ lệ OK ở lần 1, 2, 3 lần lượt là 30,0%, 11,4% và 2,2%. Nhóm chọn nội địa và hàng nặng cho pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Với cơ cấu như mẫu, cứ 1.200 yêu cầu toàn hệ thống có 900 việc thành công trong phạm vi pilot. Nhóm chia 40 triệu đ/tháng cho số việc này ở từng quy mô. Hai cột cuối gồm cả chi phí lao động `simulated`.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| Một nửa khối lượng (22.500 yêu cầu/tháng) | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- **Chi phí cố định có đổi kết luận không? Ở khối lượng nào?** Ở cả hai quy mô, chi phí sau phân bổ vẫn dưới 12.000 đ/việc (simulated). Khi khối lượng giảm một nửa, phần cố định tăng thêm 1.185 đ/việc.

## B1 · Đổi từng yếu tố

Mốc so sánh là 4.472 đ/việc thành công. Cả mức gốc và hai cột kết quả đều dùng chi phí lao động `simulated`.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ/1.000 token vào và 260 đ/1.000 token ra, giữ nguyên giá tool | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ/1.000 token vào và 65 đ/1.000 token ra, giữ nguyên giá tool | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | Tính cả phút xem lại và làm lại ở mức 2.500 đ/phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Giữ chi phí chạy đến lần 2. Yêu cầu cần lần 3 chuyển cho nhân viên | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Giữ chi phí lần 1. Yêu cầu cần chạy lại chuyển cho nhân viên | 4.111 đ | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- **Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi.** Chi phí đạt **6.543 đ/việc**, tăng **46,3%** (simulated). Hai khoản thay đổi độc lập nên mức tăng bằng tổng hai tác động riêng.
- **Xếp hạng ba yếu tố ảnh hưởng mạnh nhất.** Theo các kịch bản B1, đứng đầu là số ca làm lại gấp đôi (+51,8%), tiếp đến là tỉ lệ xem lại gấp đôi (+40,7%) và lương tăng 25% (+23,1%) (simulated).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống bằng tổng chi phí trợ lý cộng 12.000 đ cho mỗi yêu cầu chưa thành công. Ba cột chi phí dùng phút lao động `simulated`.

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- **Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không?** Công ty chi ít nhất với **2 lần** (6.901.220 đ, simulated). Với **1 lần**, chi phí trợ lý thấp nhất (4.111 đ/việc thành công, simulated), nhưng có thêm 85 yêu cầu cần nhân viên tiếp quản.

## B4 · Nếu phải xem lại tất cả

- **Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ.** Xem 948 yêu cầu có kết quả OK trong 5 phút/yêu cầu và làm lại 48 ca ở mức 9 phút/ca cho **11.743 đ/việc** (0,98×, simulated). Ở mức 15,3 phút/ca, chi phí đạt **12.415 đ/việc** (1,03×, simulated).
- **Kết quả này nói gì về thứ pilot cần học được?** Đo phút xem lại và làm lại thực tế, đồng thời theo dõi mở lại trong 7 ngày. Thời gian xem lại tối đa để hoà vốn là **5,12 phút** nếu làm lại mất 9 phút/ca, hoặc **4,80 phút** nếu mất 15,3 phút/ca (simulated).
