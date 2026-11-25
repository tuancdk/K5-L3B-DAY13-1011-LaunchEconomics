"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist

import pandas as pd
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH_THANG = 40_000_000
PHAM_VI_PILOT = ('noi_dia', 'hang_nang')


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if p == 0:
        return math.inf if k is None else k
    return ti_le_thanh_cong(p, k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return float(p > 0)
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    thanh_cong = ti_le_thanh_cong(p, k)
    return so_lan_chay_ky_vong(p, k) / thanh_cong if thanh_cong else math.inf


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Tính chi phí theo yêu cầu và chi phí mỗi việc thành công.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - chay_lai: phần token và tool của các lần thử sau lần đầu, đã nằm trong tổng.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        reqs = reqs.copy()
        vuot_gioi_han = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot_gioi_han, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot_gioi_han, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = (runs['tokens_in'] * gia_vao + runs['tokens_out'] * gia_ra) / 1000
    tien_tool = runs['tool_calls'] * gia_tool
    token = tien_token.sum()
    tool = tien_tool.sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = reqs['ket_qua'].eq('thanh_cong').sum()
    return {
        'token': token,
        'tool': tool,
        'chay_lai': (tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        'xem_lai': xem_lai,
        'lam_lai': lam_lai,
        'tong': tong,
        'thanh_cong': thanh_cong,
        'cps': tong / thanh_cong if thanh_cong else math.inf,
        'hoa_don_moi_yc': (token + tool) / len(reqs) if len(reqs) else math.nan,
    }


def in_ket_qua_cp1(runs, reqs):
    """In bảng A2–A4 để đối chiếu với báo cáo chi phí."""
    ket_qua = mo_hinh(runs, reqs)
    print('\nA2 · Chi phí từ trace (đồng, trừ số việc thành công)')
    for ten, gia_tri in ket_qua.items():
        nhan = ' [simulated]' if ten in ('xem_lai', 'lam_lai', 'tong', 'cps') else ''
        so_le = 1 if ten == 'hoa_don_moi_yc' else 0
        print(f'{ten:16s} {gia_tri:>14,.{so_le}f}{nhan}')
    print(f"CPS / hóa đơn mỗi yêu cầu: {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.2f}× [simulated]")
    ca_khong_thanh_cong = len(reqs) - ket_qua['thanh_cong']
    chi_phi_he_thong = (ket_qua['tong'] + ca_khong_thanh_cong * BASELINE) / len(reqs)
    print(f'Chi phí cả hệ thống: {chi_phi_he_thong:,.0f} đ/yêu cầu '
          f'({chi_phi_he_thong / BASELINE:.2f}× chi phí tự làm) [simulated]')

    print('\nA3 · Chi phí theo loại yêu cầu')
    print(f'{"Loại":12s} {"Số YC":>6s} {"Thành công":>12s} {"Lần/YC":>8s} '
          f'{"CPS [simulated]":>17s} {"CPS/12.000 [simulated]":>23s}')
    for loai, nhom in reqs.groupby('loai', sort=False):
        ket_qua_nhom = mo_hinh(runs, nhom)
        cps = ket_qua_nhom['cps']
        print(f'{loai:12s} {len(nhom):6d} {ket_qua_nhom["thanh_cong"] / len(nhom):12.1%} '
              f'{nhom["so_lan_chay"].mean():8.2f} {cps:17,.0f} {cps / BASELINE:22.2f}×')

    runs_theo_loai = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    ti_le_ok = runs_theo_loai.assign(ok=runs_theo_loai['status'].eq('ok')).pivot_table(
        index='loai', columns='attempt', values='ok'
    )
    print('\nTỉ lệ ok theo lần thử')
    print(ti_le_ok.to_string(float_format=lambda ti_le: f'{ti_le:.1%}'))

    print('\nA4 · Chi phí cố định trong phạm vi noi_dia + hang_nang')
    pham_vi = reqs[reqs['loai'].isin(PHAM_VI_PILOT)]
    ket_qua_pham_vi = mo_hinh(runs, pham_vi)
    ti_le_thanh_cong_trong_mau = ket_qua_pham_vi['thanh_cong'] / len(reqs)
    for khoi_luong in (45_000, 22_500):
        so_viec_thanh_cong = khoi_luong * ti_le_thanh_cong_trong_mau
        co_dinh_moi_viec = CHI_PHI_CO_DINH_THANG / so_viec_thanh_cong
        cps = ket_qua_pham_vi['cps'] + co_dinh_moi_viec
        print(f'{khoi_luong:,} yêu cầu/tháng → {so_viec_thanh_cong:,.0f} việc thành công/tháng, '
              f'cố định {co_dinh_moi_viec:,.0f} đ/việc, '
              f'CPS {cps:,.0f} đ ({cps / BASELINE:.2f}×) [simulated]')


# ---------- Nhiệm vụ D1 · Cỡ mẫu pilot ----------
def co_mau_hai_ty_le(p1, p2, alpha, power):
    """Cỡ mẫu mỗi nhóm cho kiểm định hai phía, hai nhóm cùng kích thước."""
    phan_phoi_chuan = NormalDist()
    z_alpha = phan_phoi_chuan.inv_cdf(1 - alpha / 2)
    z_power = phan_phoi_chuan.inv_cdf(power)
    p_trung_binh = (p1 + p2) / 2
    do_lech_chuan_gop = math.sqrt(2 * p_trung_binh * (1 - p_trung_binh))
    do_lech_chuan_rieng = math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return math.ceil(
        ((z_alpha * do_lech_chuan_gop + z_power * do_lech_chuan_rieng) / (p2 - p1)) ** 2
    )


def in_ket_qua_cp4(reqs):
    """In cỡ mẫu D1 và tỷ lệ mở lại dùng để lập kế hoạch pilot."""
    baseline, alpha, power = 0.70, 0.05, 0.80
    icc = 0.02
    so_nhan_vien_moi_nhom = 20
    so_depot_moi_nhom = 6
    so_yeu_cau_moi_nhan_vien = 75

    co_mau_5_diem = co_mau_hai_ty_le(baseline, 0.75, alpha, power)
    he_so_thiet_ke = 1 + (so_yeu_cau_moi_nhan_vien - 1) * icc
    co_mau_theo_cum = math.ceil(co_mau_5_diem * he_so_thiet_ke)
    so_nhan_vien_can = math.ceil(co_mau_theo_cum / so_yeu_cau_moi_nhan_vien)
    tran_theo_nhan_vien = so_nhan_vien_moi_nhom / icc
    tran_theo_depot = so_depot_moi_nhom / icc

    co_mau_6_diem = co_mau_hai_ty_le(baseline, 0.76, alpha, power)
    # Giải c*m / (1 + (m - 1)*ICC) >= n để tính số yêu cầu tối thiểu mỗi người.
    so_yeu_cau_toi_thieu = math.ceil(
        co_mau_6_diem * (1 - icc) / (so_nhan_vien_moi_nhom - co_mau_6_diem * icc)
    )
    he_so_thiet_ke_6_diem = 1 + (so_yeu_cau_toi_thieu - 1) * icc
    co_mau_hieu_dung = so_nhan_vien_moi_nhom * so_yeu_cau_toi_thieu / he_so_thiet_ke_6_diem
    power_5_diem = NormalIndPower().power(
        proportion_effectsize(0.75, baseline), nobs1=co_mau_6_diem, alpha=alpha
    )

    print('\nD1 · Cỡ mẫu pilot [simulated]')
    print(f'a. Theo yêu cầu (+5 điểm): {co_mau_5_diem:,} yêu cầu/nhóm')
    print(f'b. Theo nhân viên (m={so_yeu_cau_moi_nhan_vien}): DE={he_so_thiet_ke:.2f}, '
          f'{co_mau_theo_cum:,} yêu cầu/nhóm, {so_nhan_vien_can} nhân viên/nhóm '
          f'({2 * so_nhan_vien_can} cần so với {2 * so_nhan_vien_moi_nhom} hiện có)')
    print(f'c. {so_nhan_vien_moi_nhom} nhân viên/nhóm: cỡ mẫu hiệu dụng < {tran_theo_nhan_vien:,.0f}')
    print(f'd. {so_depot_moi_nhom} depot/nhóm: cỡ mẫu hiệu dụng < {tran_theo_depot:,.0f}')
    print(f'e. +6 điểm: cần {co_mau_6_diem:,} mẫu hiệu dụng/nhóm, '
          f'tối thiểu {so_yeu_cau_toi_thieu} yêu cầu/nhân viên; '
          f'DE={he_so_thiet_ke_6_diem:.2f}, cỡ mẫu hiệu dụng={co_mau_hieu_dung:.2f}/nhóm')
    print(f'   Ở mức {co_mau_6_diem:,} mẫu hiệu dụng/nhóm, power cho chênh lệch +5 điểm: {power_5_diem:.1%}')

    pham_vi = reqs[reqs['loai'].isin(PHAM_VI_PILOT)]
    print('\nD3 · Tỷ lệ mở lại trong 7 ngày [simulated]')
    for ten, nhom in (('Toàn mẫu', reqs), ('noi_dia + hang_nang', pham_vi)):
        mo_lai = nhom['mo_lai_trong_7_ngay']
        print(f'{ten}: {mo_lai.sum():,}/{mo_lai.count():,} yêu cầu ({mo_lai.mean():.2%})')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    in_ket_qua_cp1(runs, reqs)
    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    in_ket_qua_cp4(reqs)
