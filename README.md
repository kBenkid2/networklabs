# 🌐 Network Labs

> **Họ tên:** Vũ Văn Kiệt  
> **Mục tiêu:** Network Engineer | CCNA  
> **Platform:** EVE-NG, Cisco IOS, Python  

---

## 📂 Danh sách dự án

### 1. 🏢 [Thiết kế & Triển khai Hạ tầng Mạng Doanh nghiệp (SME)](./TK_TrienKhaiHaTangMangDoanhNgiepSME/)

> Xây dựng mô hình mạng hoàn chỉnh theo chuẩn 3 lớp cho doanh nghiệp vừa và nhỏ

| | |
|---|---|
| **Quy mô** | 1 trụ sở chính, 2 chi nhánh, 100+ users |
| **Tech Stack** | Cisco IOS, VLAN, RSTP, Static Route, DHCP, NAT, ACL |
| **Platform** | EVE-NG |

**Highlights:**
- Thiết kế 3-tier (Core - Distribution - Access)
- Inter-VLAN Routing bằng Layer 3 Switch SVI
- Floating Static Route failover tự động
- DHCP tập trung trên Core Switch
- NAT PAT ra Internet + ACL bảo mật giữa các VLAN

---

### 2. 🔐 [VPN IPSec Site-to-Site](./Site_to_Site_IPsecVPN/)

> Kết nối bảo mật giữa 2 chi nhánh qua Internet

| | |
|---|---|
| **Quy mô** | 2 Site, 1 ISP giả lập |
| **Tech Stack** | Cisco IOS, IPSec, ISAKMP, Crypto Map, VTI |
| **Platform** | EVE-NG |

**Highlights:**
- Triển khai cả 2 phương pháp: **ACL-based** và **Route-based (VTI)**
- IKE Phase 1 + Phase 2 với 3DES, MD5, Pre-shared key
- NAT Exemption tránh NAT traffic VPN
- Xử lý lỗi Policy Mismatch thực tế

---

### 3. 🐍 [Network Automation - Python + Netmiko](./Python_Auto/)

> Tự động hóa quản lý thiết bị Cisco bằng Python qua SSH

| | |
|---|---|
| **Language** | Python 3 |
| **Library** | Netmiko |
| **Platform** | EVE-NG + VMware |

**Highlights:**
- Kết nối SSH vào Router Cisco tự động
- Menu tương tác: show interface, version, backup config
- Ping từ Router và từ máy tính local
- Auto backup running-config ra file

---

## 🛠️ Tech Stack tổng quan

![Cisco](https://img.shields.io/badge/Cisco_IOS-1BA0D7?style=flat&logo=cisco&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![EVE-NG](https://img.shields.io/badge/EVE--NG-Lab-orange?style=flat)

| Công nghệ | Mức độ |
|-----------|--------|
| VLAN / Trunking / STP | ✅ Thành thạo |
| Routing (Static, OSPF) | ✅ Thành thạo |
| NAT / ACL | ✅ Thành thạo |
| IPSec VPN Site-to-Site | ✅ Thực hành |
| Python Netmiko Automation | ✅ Thực hành |
| EVE-NG Lab Design | ✅ Thành thạo |
