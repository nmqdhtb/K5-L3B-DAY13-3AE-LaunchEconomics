# Phiếu chấm hội đồng Gate 2a

**Nhóm chấm** · 3AE, lớp L3B

**Nhóm được chấm** · 5AE

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | 5AE đề xuất Go có điều kiện vì chi phí khi xem lại 100% có thể lên tới 12.414 đ/việc (simulated) và tỷ lệ mở lại của `hang_nang` là 8,23%, vượt trần 6%. |
| Số giả lập và phạm vi | Thiếu nhãn và dùng phạm vi “mọi yêu cầu” | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập, phạm vi thu hẹp có lý do bằng số | 10 | Các chi phí có nhãn `simulated`. Pilot giới hạn ở `noi_dia` và `hang_nang`, chiếm 982/1.200 yêu cầu. Chi phí sau khi cộng cố định là 4.599 đ/việc thành công (simulated). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Chia ngẫu nhiên 20 nhân viên mỗi nhánh, cần ít nhất 299 yêu cầu/người để phát hiện chênh lệch 6 điểm phần trăm. Có 4 luật dừng đủ 4 vế và cờ tắt có hiệu lực trong 30 phút. |
| **Tổng** | | | | **30 / 30** | |

## Quyết định của hội đồng

**Go có điều kiện.**

Trong phạm vi `noi_dia` và `hang_nang` (982/1.200 yêu cầu), chi phí mỗi việc thành công sau khi cộng chi phí cố định là 4.599 đ, bằng 0,38× mức tự làm 12.000 đ. Khi khối lượng giảm một nửa, chi phí là 5.784 đ, bằng 0,48×. Nhóm đã loại `quoc_te` (1,88×) và `doi_tac` (0,85×). Các số so sánh chi phí đều là `simulated`.

Thiết kế ngẫu nhiên 20 + 20 nhân viên nhắm tới chênh lệch tối thiểu 6 điểm phần trăm, với 859 yêu cầu hiệu dụng mỗi nhánh và ít nhất 299 yêu cầu mỗi nhân viên. Bốn luật dừng đều đủ bốn vế, kèm cờ tắt trong 30 phút. Hội đồng gắn các điều kiện sau với quyết định mở pilot.

- Trước 2026-12-04, hoàn tất vá lỗi ở ca 7 và ca 20, bật đủ 15 sự kiện có `trace_id` và xác nhận chấp nhận power 0,64 nếu chênh lệch thực tế chỉ là 5 điểm phần trăm.
- Sau tuần 1, thay phút xem lại và làm lại giả lập bằng phút đo thật. Khi xem lại 100%, chi phí đạt 11.743 đ/việc (0,98× mức tự làm) và lên tới 12.414 đ (1,03×) nếu làm lại mất 15,3 phút/ca (`simulated`).
- Theo dõi riêng `hang_nang` vì 13/158 yêu cầu mở lại trong 7 ngày (8,23%), vượt trần 6%. Cuối bước 0.25, thu hẹp về `noi_dia` nếu `hang_nang` vẫn vượt trần.

## Câu hỏi của 3AE

Trong đợt chạy thử, `hang_nang` có tỉ lệ mở lại 7 ngày là 8,23% (13/158, vượt trần 6%) và làm lại 11,39%, nhưng luật dừng an toàn trong `pilot_plan.yaml` lại đo gộp cả phạm vi (3,97%). Vì sao nhóm vẫn đưa `hang_nang` vào pilot thay vì tách luật dừng riêng hoặc chỉ chạy `noi_dia` từ đầu, và nếu phải cắt `hang_nang` cuối bước 0.25 (2026-12-21) thì bước 0.50 trong 2 tuần có còn đủ m ≥ 299 yêu cầu/nhân viên không?

## Câu trả lời của 5AE

Nhóm giữ `hang_nang` vì CPS biến đổi 8.221 đ = 0,69× [simulated] vẫn rẻ hơn 12.000 đ và khi gộp với `noi_dia` (chiếm 83,9%, mở lại 3,16%) thì tỉ lệ mở lại chung là 3,97% nên không làm pilot dừng ngay tuần đầu. Đồng thời, đã có điều kiện theo dõi riêng để thu hẹp về `noi_dia` vào 2026-12-21 nếu `hang_nang` vẫn trên 6%.

Nếu cắt `hang_nang` trước bước 0.50, lượng `noi_dia` còn khoảng 25,8 yêu cầu/nhân viên/ngày (1.500 / 40 × 824 / 1.200), cần khoảng 12 ngày để đạt m ≥ 299 nên vẫn kịp trong 2 tuần (14 ngày) của bước 0.50. Nhóm ghi nhận sẽ bổ sung luật dừng tách riêng cho `hang_nang` vào `pilot_plan.yaml`.
