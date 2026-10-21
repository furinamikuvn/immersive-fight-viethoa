#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
deploy_direct_viethoa.py
========================
Script triển khai Việt Hóa TRỰC TIẾP của Tawa cho Master Nukumizu.
Đồng bộ tự động vào cả 3 thư mục:
  1. Workspace nguồn: `Immersive Fight 4.2.9 Viet Hoa`
  2. Workspace modpack: `Immersive Fight 4.2.9`
  3. Minecraft instance thật: `Forge 1.20.1` của TLauncher

Quy chuẩn:
  - Tên vật phẩm/vũ khí/khối: 100% TIẾNG ANH (dễ tra JEI).
  - Mô tả/tooltip/kỹ năng/potion: 100% TIẾNG VIỆT (sắc bén, hào hùng).
  - Tạo đồng thời cả vi_vn.json, zh_cn.json, en_us.json trong resources/assets/
"""

import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

tools_dir = Path(__file__).resolve().parent

print("=" * 70)
print("  TAWA DIRECT VIỆT HÓA PIPELINE — IMMERSIVE FIGHT 4.2.9")
print("=" * 70)

# Bước 1: Chạy build & deploy hoàn hảo
print("\n[BƯỚC 1] Chạy Perfect Direct Việt Hóa (230 namespaces x 3 file lang)...")
subprocess.run([sys.executable, str(tools_dir / "perfect_direct_viethoa.py")], check=True)

# Bước 2: Tự động dịch các chuỗi mô tả còn sót
print("\n[BƯỚC 2] Tinh chỉnh và chuyển ngữ các mô tả còn sót...")
subprocess.run([sys.executable, str(tools_dir / "auto_translate_all_remaining.py")], check=True)

# Bước 3: Ghi đè các hiệu ứng đặc biệt
print("\n[BƯỚC 3] Áp dụng các từ điển đặc thù (BetterEnd, Relics, Dungeons & Combat)...")
subprocess.run([sys.executable, str(tools_dir / "apply_specific_cleanups.py")], check=True)

print("\n" + "=" * 70)
print("  🎉 HOÀN TẤT 100%! BẢN DỊCH TRỰC TIẾP ĐÃ SẴN SÀNG.")
print("  Khởi động lại game Minecraft Forge 1.20.1 để thưởng thức!")
print("=" * 70)
