# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | ... |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | ... |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | ... |
| Dùng | Nhóm tự đề xuất: ... | ... | Không cần tính |
| An toàn | Nhóm tự đề xuất: ... | ... | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

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
- Hai chỉ số tự đề xuất: (người điền E1 ghi event tương ứng sau khi chốt chỉ số).

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
