# 🏢 Thiết kế & Triển khai Hạ tầng Mạng Doanh nghiệp (SME)

> **Platform:** EVE-NG | **Vendor:** Cisco IOS  
> **Scale:** 1 trụ sở chính, 2 chi nhánh, mô phỏng 100+ users

---

## 📐 Topology

```
                    [R1] - Loopback: 203.0.113.1 (giả lập Internet)
                   /    \
         10.1.2.0/30    10.2.3.0/30
                /            \
          [Coresw1]--L3--[Coresw2]
           /    \        /    \
       [swAcc1]          [swAcc2]
       /     \           /     \
     PC1    PC3        PC2    PC4
   vlan100 vlan200   vlan100 vlan200
```

---

## 🔧 Công nghệ triển khai

| Công nghệ | Mô tả |
|-----------|-------|
| **VLAN** | VLAN 100 (192.168.100.0/24), VLAN 200 (192.168.200.0/24) |
| **Inter-VLAN Routing** | SVI trên Layer 3 Switch (Coresw) |
| **RSTP** | Rapid Spanning Tree, Coresw1 làm Root Primary 100,200
| **Static Route** | Static và Floating static route với AD=5 cho đường backup Trên R1
| **DHCP** | DHCP Server trên Coresw1 cho cả 2 VLAN, default trỏ về Coresw1
| **NAT** | PAT trên R1 để các VLAN ra Internet |
| **ACL** | Kiểm soát truy cập giữa các VLAN |

---

## 🌐 Quy hoạch địa chỉ IP

### Uplink (Point-to-Point)
| Link | Subnet | R1 | Coresw |
|------|--------|----|--------|
| R1 → Coresw1 | 10.1.2.0/30 | 10.1.2.1 | 10.1.2.2 |
| R1 → Coresw2 | 10.2.3.0/30 | 10.2.3.1 | 10.2.3.2 |
| Coresw1 ↔ Coresw2 | 10.12.0.0/30 | 10.12.0.1 | 10.12.0.2 |

### SVI (Gateway các VLAN)
| Switch | VLAN 100 | VLAN 200 |
|--------|----------|----------|
| Coresw1 | 192.168.100.3 | 192.168.200.3 |
| Coresw2 | 192.168.100.2 | 192.168.200.2 |

### DHCP Pool
| VLAN | Dải cấp phát | Gateway |
|------|-------------|---------|
| VLAN 100 | 192.168.100.10 - .254 | 192.168.100.3 |
| VLAN 200 | 192.168.200.10 - .254 | 192.168.200.3 |

---

## 🔁 Định tuyến

```bash
# R1 - Primary route qua Coresw1
ip route 192.168.100.0 255.255.255.0 10.1.2.2
ip route 192.168.200.0 255.255.255.0 10.1.2.2

# R1 - Backup route qua Coresw2 (Floating Static AD=5)
ip route 192.168.100.0 255.255.255.0 10.2.3.2 5
ip route 192.168.200.0 255.255.255.0 10.2.3.2 5
```

---

## 🛡️ Bảo mật

- **BPDU Guard** trên tất cả port access (chống cắm switch trái phép)
- **PortFast** trên port xuống end-device
- **ACL** kiểm soát traffic giữa VLAN 100 và VLAN 200
- **NAT PAT** kiểm soát truy cập Internet

---

## 📁 File trong repo

| File | Mô tả |
|------|-------|
| `SME.unl` | File topology EVE-NG (import để chạy lab) |
| `SME.png` | Sơ đồ mạng tổng quan |

---

## 💡 Điểm nổi bật

- Link giữa 2 Coresw thiết kế **Layer 3** thay vì Layer 2 → tránh loop, không cần STP block, cả 2 đường active đồng thời
- **Floating Static Route** đảm bảo failover tự động khi Coresw1 down
- Mô hình **3-tier** (Core - Distribution - Access) chuẩn enterprise
