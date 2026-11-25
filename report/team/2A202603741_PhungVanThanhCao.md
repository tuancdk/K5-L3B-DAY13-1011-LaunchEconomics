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
| Commit | `8cf75a7`: báo cáo cá nhân và TEAM.md (PR #14) · `556eb64`: nhãn độc lập người gắn nhãn 1, CP3 (PR #17) · `2b3c824`: danh sách 11 event và kiểm tra chéo (PR #21) · `3dad4b2`: E1, E2 trong `chi_so.md`, hồ sơ mục 4, đóng góp TEAM.md (PR #24) |
| File | `report/team/bang_loi.md` (cột "Nhãn người 1"); `report/team/chi_so.md` (event, E1, E2); `report/team/ho_so_launch_v0.md` (mục 4); `TEAM.md` (dòng 3 và mục cá nhân) |
| Bảng / mục | `bang_loi.md`: hai bộ nhãn độc lập; `chi_so.md`: bảng E1, danh sách event, bảng E2; checklist "Xong khi" CP1, CP2, CP4 |
| Con số | 20/20 ca đã gắn nhãn; B1 9/9 kịch bản khớp đáp án; A2 4.472 đ [simulated]; E1 82,83% · 27,12% · 4,25% [simulated]; 11 event có `trace_id` |

## 5. Công cụ AI đã dùng

| Công cụ | Dùng vào việc gì | Cách tự kiểm tra |
|---|---|---|
| Claude | Hỗ trợ giải đáp những phần còn đang chưa phân vân, kết quả gán nhãn 20 ca lỗi do cá nhân chủ động thực hiện theo Google PAIR, giải đáp các trường hợp chưa rõ ràng, phân tích những điểm chưa thống nhất và hỗ trợ hoàn thiện quy tắc phân biệt giữa các nhóm nhãn | Đối chiếu với tiêu chí Google PAIR, yêu cầu dự án (`CHECKPOINTS.md`, `RUBRIC.md`), kết quả trao đổi với người gắn nhãn 2 và tài liệu minh chứng; tự đánh giá, xác nhận kết quả trước khi cập nhật |

- Mọi con số trong hồ sơ đều do `src/lab13.py` tính, hoặc tính tay có ghi cách tính, không lấy số do AI tự đưa ra.

## 6. Tự đánh giá

- **Làm tốt:** Có ý thức chủ động theo dõi tiến độ và các điều kiện hoàn thành của từng checkpoint CP1–CP5, kịp thời rà soát và phản hồi những nội dung còn thiếu để nhóm bổ sung. Hoàn thành phần gắn nhãn độc lập 20 ca lỗi, phối hợp đối chiếu kết quả với người gắn nhãn 2 và tham gia xây dựng quy tắc phân biệt nhằm thống nhất cách đánh giá. Đồng thời, chú trọng kiểm tra số liệu và bằng chứng trước khi cập nhật vào báo cáo chung.

- **Chưa tốt / cần cải thiện:** Trong quá trình gắn nhãn, một số trường hợp có nguyên nhân gốc tương đối phức tạp nên việc phân biệt giữa các nhóm nhãn ban đầu chưa thực sự nhất quán. Tỷ lệ đồng thuận độc lập đạt 50%, cho thấy bản thân cần cải thiện thêm khả năng phân tích tình huống, xác định nguyên nhân gốc và vận dụng tiêu chí phân loại một cách chặt chẽ hơn. Bên cạnh đó, cần chủ động hơn trong việc rà soát và hoàn thiện tài liệu từ sớm.

- **Bài học rút ra:** Qua quá trình thực hiện, bản thân nhận thấy việc thống nhất định nghĩa và tiêu chí đánh giá ngay từ đầu rất quan trọng, đặc biệt đối với những công việc mang tính phân tích và gắn nhãn. Việc đối chiếu kết quả giúp nhận diện những điểm chưa thống nhất, đồng thời nâng cao tính nhất quán và độ tin cậy của dữ liệu. Ngoài ra, mỗi kết quả cần được kiểm chứng bằng số liệu và bằng chứng cụ thể trước khi đưa vào báo cáo.

- **Mức đóng góp tự chấm: 8/10.**
