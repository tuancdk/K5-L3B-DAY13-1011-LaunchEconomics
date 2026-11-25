# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) [simulated] |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) [simulated] |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) [simulated]; trong phạm vi noi_dia + hang_nang 3,97% (39/982) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm trợ lý mà nhân viên mở gợi ý của trợ lý | Số `agent_suggestion_shown` có staff_id thuộc nhóm trợ lý, chia số `refund_request_created` có arm = tro_ly | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | Số `audit_sample_checked` có so_tien_da_hoan ≠ so_tien_dung, chia số đơn được kiểm tra trong tuần | Không cần tính |

Số tính thử do `src/lab13.py` in ra (mục "E1 · Chỉ số trong đợt chạy thử"). Chỉ số chính trong đợt chạy thử là 82,83% [simulated]. Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien_yeu_cau, depot, staff_id, arm (tro_ly/doi_chung), trace_id | Khi khách gửi yêu cầu |
| `input_validation_failed` | Agent | request_id, truong_loi, reason (ví dụ ma_khong_hop_le), trace_id | Khi đầu vào của khách không hợp lệ |
| `agent_run_completed` | Agent | request_id, attempt, tokens_in, tokens_out, tool_calls, status (ok/loi), trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | request_id, staff_id, so_tien_de_xuat, phien_ban_bang_gia, trace_id | Khi gợi ý hiện cho nhân viên |
| `staff_review_decision` | Nhân viên | request_id, staff_id, quyet_dinh (giu/sua/bo), phut_xem_lai (đo thật), trace_id | Khi nhân viên bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | request_id, staff_id, phut_lam_lai (đo thật), ly_do, trace_id | Khi làm lại xong |
| `handoff_to_staff` | Agent | request_id, reason (thieu_du_lieu/ngoai_pham_vi/vuot_gioi_han_chay), tom_tat, trace_id | Khi chuyển ca cho nhân viên |
| `refund_ledger_write` | Dịch vụ sổ cái | request_id, idempotency_key, so_tien, ket_qua (ok/loi), trace_id | Khi ghi lệnh hoàn vào sổ cái |
| `ticket_closed` | Hệ thống ticket | request_id, created_at, closed_at, trace_id | Khi yêu cầu được đóng |
| `ticket_reopened` | Khách | request_id, reopened_at, reason (ví dụ so_tien), trace_id | Khi khách mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | request_id, so_tien_da_hoan, so_tien_dung, phien_ban_bang_gia, trace_id | Hằng tuần, mẫu 100 đơn |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính (đóng trong 24 giờ, không mở lại trong 7 ngày): `refund_request_created` (mẫu số, created_at) + `ticket_closed` (closed_at − created_at ≤ 24 giờ) + `ticket_reopened` (không có trong 7 ngày sau closed_at).
- Chỉ số dùng (tỉ lệ bỏ qua gợi ý): `staff_review_decision` với quyet_dinh = sua hoặc bo, chia số `staff_review_decision`.
- Chỉ số an toàn (lỗi lọt đến khách): `ticket_reopened` trong 7 ngày, chia số `refund_request_created`.
- Chi phí mỗi việc thành công (dùng cho luật dừng chi phí): `agent_run_completed` (token, tool, mọi lần chạy) + `staff_review_decision.phut_xem_lai` + `staff_rework_completed.phut_lam_lai`, chia số yêu cầu thành công. Thay phút simulated bằng phút đo thật.
- Hoàn trùng (luật dừng an toàn): hai `refund_ledger_write` ket_qua = ok cùng request_id.
- Chỉ số dùng tự đề xuất (% yêu cầu được mở bằng trợ lý): `agent_suggestion_shown` (tử số) + `refund_request_created` với arm = tro_ly (mẫu số).
- Chỉ số an toàn tự đề xuất (% đơn hoàn sai qua kiểm tra mẫu): `audit_sample_checked`, so sánh so_tien_da_hoan với so_tien_dung.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công lên 6.787 đ (+51,8%) [simulated], yếu tố nhạy nhất trong B1 | Tỉ lệ `staff_rework_completed` trên số yêu cầu theo tuần > 9,8%, tức gấp đôi mức 4,9% (48/982) trong phạm vi của đợt chạy thử [simulated] | Thu hẹp về noi_dia, rà 20 trace làm lại gần nhất để tìm nguyên nhân | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× mốc 12.000 đ, hoặc 12.415 đ = 1,03× nếu làm lại 15,3 phút/ca như dữ liệu (B4) [simulated] | % yêu cầu có `staff_review_decision` còn > 50% ở cuối bước rollout 0.25; thời gian xem lại trung bình > 4,8 phút/ca (mức hoà vốn B4) [simulated] | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15%; rút gọn màn hình xem lại | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu chỉ còn một nửa, CPS 5.784 đ = 0,48× (A4) [simulated] | Số việc thành công theo tuần < 50% kế hoạch trong 2 tuần liên tiếp | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
