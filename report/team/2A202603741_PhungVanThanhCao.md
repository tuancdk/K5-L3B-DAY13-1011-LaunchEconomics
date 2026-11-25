# Báo cáo cá nhân — PhungVanThanhCao-2A202603741

## 1. Thông tin thành viên

- Họ tên: Phùng Văn Thanh Cao
- MSSV: 2A202603741
- Email: 26ai.caopvt@vinuni.edu.vn
- Vai trong nhóm: Người gắn nhãn 1

## 2. Phần việc phụ trách

- Theo dõi điều kiện "Xong khi" của từng checkpoint CP1–CP5, báo cho nhóm phần còn thiếu trước khi chuyển checkpoint.
- Nhiệm vụ C: gắn nhãn độc lập 20 ca lỗi theo năm loại của Google PAIR, so nhãn với người gắn nhãn 2, viết quy tắc phân biệt và bảng khắc phục.
- File phụ trách: `report/team/bang_loi.md` (cột "Nhãn người 1", quy tắc phân biệt, bảng khắc phục).

## 3. Đóng góp cụ thể

- CP1 · A: chạy `python lab13.py` để kiểm checklist. Xác nhận ba phép thử A1 ĐẠT (1,20 · 1,25 · 1,25) và A2 khớp đáp án (chi phí mỗi việc thành công 4.472 đ, gấp 16,28× hoá đơn token [simulated]). Báo nhóm `bang_chi_phi.md` phần A còn trống. Góp ý thêm `doi_tac` (0,85× [simulated]) vào câu trả lời A3.
- CP2 · B: kiểm B1 đủ 9 kịch bản, khớp đáp án; kiểm quy tắc "giảm một nửa bằng ½ mức gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9 [simulated]); xác nhận B4 ghi cả 0,98× và 1,03× [simulated]. Báo nhóm phần B trong `bang_chi_phi.md` còn 17 chỗ trống và branch CP4 chưa merge.
- CP3 · C: tự gắn nhãn độc lập cả 20 ca, không trao đổi với người gắn nhãn 2, ra kết quả: Do người dùng 4 · Hệ thống 5 · Ngữ cảnh 4 · Giới hạn hệ thống 3 · Ngầm 4. Tỉ lệ đồng thuận với người gắn nhãn 2 là 10/20 = 50%, dưới 80%, nên hai người viết lại định nghĩa theo thứ tự xét (Ngầm → Do người dùng → Giới hạn → Hệ thống → Ngữ cảnh) và viết quy tắc cho 10 ca không trùng. Bộ nhãn thống nhất khớp bảng đáp án ở 20/20 ca.
- CP4 · D: kiểm "Xong khi" của `pilot_plan.yaml`: `yaml.safe_load` chạy không lỗi, không còn `?` ngoài dòng chú thích, có 4 luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ, chia theo nhân viên 20 cụm mỗi nhóm, ghi rõ đánh đổi MDE 6 điểm (power 64,2% ở mức 5 điểm, simulated).
- CP5 · E: viết danh sách 11 event có `trace_id` trong `chi_so.md` và phần kiểm tra chéo chỉ số → event; tên event khớp với bảng khắc phục CP3. Điền E1: ba chỉ số tính thử do `lab13.py` in ra (82,83% · 27,12% · 4,25% [simulated]) và hai chỉ số tự đề xuất. Điền E2: 3 dòng rủi ro kinh tế lấy số từ bảng độ nhạy (+51,8%; 0,98–1,03×; +2.370 đ/việc [simulated]). Cập nhật mục 4 của hồ sơ launch sang "Xong, có bằng chứng".
- Duyệt chéo Gate 2a: (điền sau)

## 4. Bằng chứng

| Loại | Nội dung |
|---|---|
| Commit | `8cf75a7`: thêm báo cáo cá nhân và thông tin TEAM.md (PR #14) · (thêm mã commit CP3 sau khi push) |
| File | `report/team/bang_loi.md`, cột "Nhãn người 1"; `TEAM.md`, dòng 3 |
| Bảng / mục | `bang_loi.md`: hai bộ nhãn độc lập; checklist "Xong khi" CP1, CP2 |
| Con số | 20/20 ca đã gắn nhãn; B1 9/9 kịch bản khớp đáp án; A2 4.472 đ [simulated] |

## 5. Công cụ AI đã dùng

| Công cụ | Dùng vào việc gì | Cách tự kiểm tra |
|---|---|---|


- Mọi con số trong hồ sơ đều do `src/lab13.py` tính, hoặc tính tay có ghi cách tính, không lấy số do AI tự đưa ra.

## 6. Tự đánh giá

- Làm tốt:
- Chưa tốt / cần cải thiện:
- Bài học rút ra:
- Mức đóng góp tự chấm (/10):
