# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: 1011
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để Gate 2a duyệt kế hoạch pilot, trả lời bốn câu hỏi: có đáng chạy, nhân viên có dùng, khi hỏng thì sao, pilot có ra được quyết định không. Mọi con số do `src/lab13.py` tính từ hai CSV, hoặc tính tay có ghi cách tính. Nhóm chia bốn vai theo `TEAM.md`, mỗi checkpoint là một issue (#1–#9) có checklist, mỗi phần việc đi qua một PR. Sau giải lao đổi người viết code để hai người tự tính được chi phí.

## 3. Giải pháp

- **A · Chi phí mỗi việc thành công** ([bang_chi_phi.md](bang_chi_phi.md)): tử số cộng token, tool trên mọi 1.624 lần chạy (kể cả lần lỗi) và phút xem lại, làm lại; mẫu số chỉ đếm 978 việc thành công. Tách theo `loai`, cộng 40 triệu đ/tháng chi phí cố định cho phạm vi noi_dia + hang_nang.
- **B · Độ nhạy** ([bang_chi_phi.md](bang_chi_phi.md)): gọi lại cùng `mo_hinh` cho 9 kịch bản, một cặp, giới hạn 1–3 lần chạy và kịch bản xem lại 100%; kiểm "giảm một nửa = ½ mức gấp đôi" trước khi làm tròn.
- **C · Bảng lỗi** ([bang_loi.md](bang_loi.md)): hai người gắn nhãn độc lập 20 ca, đồng thuận 10/20 = 50% nên viết lại định nghĩa thành năm câu hỏi xét theo thứ tự, thống nhất 20 ca; bảng khắc phục 5 ca đủ năm loại, mỗi dòng có event, ngưỡng và một vai trò phụ trách.
- **D · Pilot** ([pilot_plan.yaml](pilot_plan.yaml)): tính năm câu D1 trước khi chọn cách chia; chia ngẫu nhiên theo nhân viên 20 + 20 cụm, phân tầng theo depot, MDE 6 điểm, 4 luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ.
- **E · Chỉ số và hồ sơ** ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)): ba chỉ số tính thử, hai chỉ số tự đề xuất, 11 event có `trace_id` và kiểm tra chéo chỉ số ↔ event, 3 dòng rủi ro kinh tế; hồ sơ một trang bảy mục.

## 4. Kết quả

- Chi phí mỗi việc thành công 4.472 đ, gấp 16,28× hoá đơn token và tool chia số yêu cầu (274,7 đ); làm lại chiếm 51,8% tổng chi phí [simulated].
- Theo loại: noi_dia 0,22×, hang_nang 0,69×, doi_tac 0,85×, quoc_te 1,88× mốc 12.000 đ [simulated]. Phạm vi noi_dia + hang_nang đã cộng cố định: 4.599 đ = 0,38× [simulated].
- Ba yếu tố nhạy nhất khi gấp đôi: làm lại +51,8%, xem lại +40,7%, lương +25% → +23,1% [simulated]. Giới hạn 2 lần chạy cho chi phí cả hệ thống thấp nhất (6.901.220 đ) [simulated].
- Pilot: cần 1.251 yêu cầu/nhóm cho +5 điểm nhưng 20 cụm/nhóm chỉ cho cỡ mẫu hiệu dụng < 1.000, nên chọn MDE 6 điểm (859/nhóm, ≥ 299 yêu cầu/nhân viên, DE 6,96); power 64,2% nếu tác động thật là 5 điểm.
- Chỉ số trong đợt chạy thử: chính 82,83% · bỏ qua gợi ý 27,12% · mở lại 7 ngày 4,25% (trong phạm vi 3,97%) [simulated].
- **Đề xuất cuối:** Go có điều kiện cho pilot noi_dia + hang_nang, nêu hai con số bất lợi (xem lại 100% → 0,98–1,03× [simulated]; power 64,2%) và 4 điều kiện có người phụ trách, ngày kiểm tra.
- **Duyệt chéo Gate 2a:** nhóm nhận 25/30 điểm từ hội đồng. Nhóm 1011 làm hội đồng cho nhóm HH, chấm 25/30 và chuyển đề xuất Go của HH thành Go có điều kiện ([phieu_cham.md](phieu_cham.md)).

## 5. Khó khăn và cách xử lý

- **Đồng thuận gắn nhãn thấp (50%):** người gắn nhãn 2 không dùng nhãn Ngữ cảnh, xếp các ca "trợ lý đúng thiết kế nhưng khách thấy sai" vào loại khác. Xử lý: viết lại định nghĩa theo thứ tự Ngầm → Do người dùng → Giới hạn → Hệ thống → Ngữ cảnh, ghi một câu quy tắc cho từng ca lệch, giữ nguyên hai bộ nhãn độc lập.
- **Không đủ cụm cho mức +5 điểm:** chia theo nhân viên chỉ có 20 cụm/nhóm. Xử lý: chấp nhận MDE 6 điểm, ghi rõ đánh đổi power 64,2% và đưa thành điều kiện ký chấp nhận trong hồ sơ.
- **Lỗi chạy trên Windows:** Python hệ thống thiếu `statsmodels`; trong venv, `python lab13.py` báo `UnicodeEncodeError: 'charmap' codec can't encode character` khi in tiếng Việt. Xử lý: chạy bằng venv và đặt `PYTHONIOENCODING=utf-8`, sau đó chạy hết và ba phép thử in ĐẠT.
- **Lệnh tự kiểm tra từ cấm bắt chính báo cáo cá nhân** (dòng trích lại lệnh grep). Xử lý: viết lại câu ở PR #25.
- **Trùng việc phần A:** người giữ hồ sơ điền song song với người kiểm số. Xử lý: bỏ bản trùng, chỉ giữ bảng của người kiểm số (PR #12).

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Hai khoản lớn nhất (xem lại, làm lại) vẫn là phút simulated; pilot phải thay bằng phút đo thật từ `staff_review_decision` và `staff_rework_completed` trước khi kết luận về chi phí.
- Power chỉ 64,2% ở mức 5 điểm: nếu tác động thật nhỏ hơn 6 điểm, pilot có thể không phát hiện được.
- Lịch pilot có thể chưa đủ mẫu tới ngày quyết định 2027-01-05. Tính tay: bước 50% bắt đầu khoảng 2026-12-21, cần 7 ngày theo dõi nên tuyển mẫu đến 2026-12-29 (9 ngày); mỗi nhân viên khoảng 1.500 ÷ 40 × 982/1.200 ≈ 31 yêu cầu trong phạm vi/ngày, tức ≈ 276 < 299 yêu cầu cần. Plan đã ghi: chưa đủ mẫu thì không kết luận, giữ phạm vi và chốt lại ngày; hướng cải thiện là lùi ngày quyết định khoảng một tuần.
- quoc_te (1,88×) và doi_tac (0,85×, thành công 54,4%, chỉ 68 yêu cầu) nằm ngoài pilot; cần dữ liệu riêng trước khi xét lại [simulated].

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, https://arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", https://pair.withgoogle.com
- Tài liệu statsmodels, lớp `NormalIndPower` (mục `stats.power`)
- Tài liệu lab: `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`
