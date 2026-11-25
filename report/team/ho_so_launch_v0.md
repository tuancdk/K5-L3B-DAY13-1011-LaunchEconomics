# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: 1011 · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated], gấp 16,3× hoá đơn token + tool chia số yêu cầu (274,7 đ); làm lại chiếm 51,8% tổng chi phí [simulated] | Giả lập | Người viết code |
| 2 · Ba yếu tố nhạy nhất | Khi gấp đôi: 1. số ca làm lại +51,8% (6.787 đ) · 2. tỉ lệ xem lại +40,7% (6.292 đ) · 3. lương nhân viên +25% → +23,1% (5.506 đ); giá token gấp đôi chỉ +5,6% [simulated] (`bang_chi_phi.md` B1, B2) | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | Cả hệ thống 5.865 đ/yêu cầu = 0,49× của 12.000 đ [simulated]; phạm vi noi_dia + hang_nang đã cộng cố định 4.599 đ = 0,38× [simulated]; quoc_te 1,88× → loại khỏi phạm vi | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử (chưa có đối chứng): chính 82,83% (994/1.200) · dùng: bỏ qua gợi ý 27,12% (48/177) · an toàn: mở lại 7 ngày 4,25% (51/1.200), trong phạm vi 3,97% (39/982). Chờ `chi_so.md` đối chiếu và bổ sung event | Chưa | Người gắn nhãn 1 |
| 5 · Bảng lỗi và cách khắc phục | 20 ca: đồng thuận độc lập 10/20 = 50% (< 80%) → đã viết lại định nghĩa và thống nhất 20/20 (4 Do người dùng · 5 Hệ thống · 4 Ngữ cảnh · 4 Giới hạn · 3 Ngầm); bảng khắc phục 5 ca đủ năm loại, mỗi ca có event + ngưỡng + một vai trò (`bang_loi.md`) | Xong, có bằng chứng | Người gắn nhãn 2 |
| 6 · Pilot plan | Chia ngẫu nhiên theo nhân viên 20 + 20 cụm, phân tầng theo depot; phạm vi noi_dia + hang_nang; MDE 6 điểm (859/nhóm, ≥ 299 yêu cầu/người, DE 6,96); **bất lợi:** power chỉ 64,2% nếu tác động thật là 5 điểm; 4 luật dừng có ngưỡng, người dừng là Giám đốc vận hành; quyết định 2027-01-05 (`pilot_plan.yaml`) | Xong, có bằng chứng | Người viết code |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi → 6.787 đ (+51,8%); xem lại 100% trong phạm vi → 11.743 đ = 0,98× (12.415 đ = 1,03× nếu làm lại 15,3 phút), hoà vốn khi xem lại ≤ 4,8–5,1 phút/ca; khối lượng còn một nửa → cố định 2.370 đ/việc [simulated] | Giả lập | Người gắn nhãn 2, kiêm giữ hồ sơ |

**Đề xuất: Go có điều kiện** cho pilot chỉ gồm noi_dia + hang_nang: cộng cố định vẫn 4.599 đ = 0,38× của 12.000 đ [simulated]; loại quoc_te (1,88×) và doi_tac (0,85×) [simulated]. Con số bất lợi: xem lại 100% đẩy chi phí lên 0,98–1,03× [simulated], và power chỉ 64,2% nếu tác động thật là 5 điểm. Pilot bắt đầu 2026-12-07, ngày quyết định 2027-01-05.

| # | Điều kiện | Người phụ trách | Ngày kiểm tra |
| --: | --- | --- | --- |
| 1 | Khoá chống trùng và đối soát sổ cái mỗi giờ (ca 7, 20); kiểm thử 0 ca hoàn trùng | Kỹ sư trưởng agent | 2026-12-04 |
| 2 | Ký chấp nhận MDE 6 điểm, biết power 64,2% ở mức 5 điểm | Giám đốc vận hành | 2026-12-04 |
| 3 | Bật đủ event có trace_id; thay phút xem lại, làm lại simulated bằng phút đo thật | PM trợ lý hoàn phí | 2026-12-14 |
| 4 | Giảm xem lại theo bậc: 100% ở bước 10%, chỉ giảm khi tỉ lệ sửa + bỏ < 15%; mỗi lần xem ≤ 4,8 phút [simulated] | Trưởng nhóm CSKH | 2026-12-21 |
