# Team

## Thông tin nhóm

- Tên nhóm: 1011
- Lớp: L3B
- Trưởng nhóm: Lê Anh Tuấn (tuancdk)
- Repo nhóm: `K5-L3B-DAY13-1011-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/tuancdk/K5-L3B-DAY13-1011-LaunchEconomics · `main` · (điền khi chốt)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Vũ Quang Huy | 2A202603782 | 26ai.huyvq6@vinuni.edu.vn | huyvu-03 | Người viết code (đến 15:20) → người kiểm số (sau 15:35) |
|   2 | Nguyễn Minh Đức | 2A202603751 | nmduc7904@gmail.com | Minhduc7904 | Người kiểm số (đến 15:20) → người viết code (sau 15:35) |
|   3 | Phùng Văn Thanh Cao | 2A202603741 | 26ai.caopvt@vinuni.edu.vn | ththanh8888 | Người gắn nhãn 1 |
|   4 | Lê Anh Tuấn | 2A202603792 | 26ai.tuanla3@vinuni.edu.vn | tuancdk | Trưởng nhóm; người gắn nhãn 2, kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## PhungVanThanhCao-2A202603741

### Phần việc phụ trách

- Người gắn nhãn 1: theo dõi điều kiện "Xong khi" của CP1–CP5; nhiệm vụ C (`bang_loi.md`); danh sách event, E1, E2 trong `chi_so.md`; mục 4 của `ho_so_launch_v0.md`.

### Đóng góp cụ thể

- Kiểm checklist CP1, CP2, CP4: xác nhận số khớp đáp án, báo nhóm các bảng còn trống, kiểm `pilot_plan.yaml` đọc được bằng `yaml.safe_load`.
- Gắn nhãn độc lập 20 ca lỗi (cột "Nhãn người 1"), cùng người gắn nhãn 2 thống nhất nhãn.
- Viết 11 event có `trace_id` và phần kiểm tra chéo; điền E1 (3 chỉ số tính thử, 2 chỉ số tự đề xuất) và 3 dòng rủi ro kinh tế E2.

### Bằng chứng

- Commit `8cf75a7` (PR #14), `556eb64` (nhãn độc lập CP3, PR #17), `2b3c824` (danh sách event, PR #21), cùng commit E1/E2 này.
- File: `report/team/bang_loi.md`, `report/team/chi_so.md`, `report/team/2A202603741_PhungVanThanhCao.md`.

## LeAnhTuan-2A202603792

Báo cáo chi tiết: [report/team/2A202603792_LeAnhTuan.md](report/team/2A202603792_LeAnhTuan.md)

### Phần việc phụ trách

- Trưởng nhóm: tạo repo, chia vai, mở issue theo checkpoint và theo dõi tiến độ.
- CP3: người gắn nhãn 2, hoàn thiện `report/team/bang_loi.md`.
- CP5 · E3: giữ hồ sơ `report/team/ho_so_launch_v0.md`.

### Đóng góp cụ thể

- Mở 9 issue (#1–#9) có checklist và người phụ trách; điền `TEAM.md` và khung hồ sơ lúc đầu buổi.
- CP3: gắn 20 ca độc lập; đồng thuận 10/20 = 50% → viết lại định nghĩa, thống nhất 20 ca, bảng khắc phục 5 ca đủ năm loại.
- CP5 · E3: điền đủ bảy mục hồ sơ và đề xuất Go có điều kiện cho noi_dia + hang_nang, kèm 4 điều kiện có người phụ trách và ngày kiểm tra.

### Bằng chứng

- [PR #10](https://github.com/tuancdk/K5-L3B-DAY13-1011-LaunchEconomics/pull/10) · [PR #19](https://github.com/tuancdk/K5-L3B-DAY13-1011-LaunchEconomics/pull/19) (commit `77100e7`) · [PR #20](https://github.com/tuancdk/K5-L3B-DAY13-1011-LaunchEconomics/pull/20)
- [Issue #4](https://github.com/tuancdk/K5-L3B-DAY13-1011-LaunchEconomics/issues/4) (CP3) và [issue #5](https://github.com/tuancdk/K5-L3B-DAY13-1011-LaunchEconomics/issues/5) (CP4) đóng kèm kết quả kiểm tra.

## VuQuangHuy-2A202603782

Báo cáo chi tiết trong [báo cáo cá nhân](report/team/2A202603782_VuQuangHuy.md).

### Phần việc phụ trách

- Viết code cho CP1 (A1–A4) và CP2 (B1–B4), kiểm số và hoàn thiện kế hoạch pilot ở CP4, tính ba chỉ số E1 ở CP5.

### Đóng góp cụ thể

- **CP1–CP2** — Cài đặt mô hình chi phí mỗi việc thành công, phân tích theo loại yêu cầu và khối lượng, rồi kiểm tra độ nhạy với giá token, thời gian nhân viên và giới hạn chạy lại.
- **CP4** — Tính tay D1(e), đối chiếu kết quả 299 yêu cầu/nhân viên với script của Minh Đức, hoàn thiện kế hoạch pilot và kiểm tra bốn luật dừng.
- **CP5** — Tính và đối chiếu với CSV ba chỉ số E1 để Thanh Cao đưa vào bảng chỉ số của nhóm.

### Bằng chứng

- [src/lab13.py](src/lab13.py) trong các commit `4c884a3` (CP1), `f8aa454` (CP2) và `39dde70` (CP5).
- [pilot_plan.yaml](report/team/pilot_plan.yaml) trong commit `f9d8207` (CP4).

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-
