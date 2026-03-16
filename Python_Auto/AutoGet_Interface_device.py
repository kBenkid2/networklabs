from netmiko import ConnectHandler
from netmiko.exceptions import (
    NetmikoAuthenticationException,
    NetmikoTimeoutException,
)
import subprocess

device = {
    "device_type": "cisco_ios",
    "host": "192.168.28.100",  # IP router của bạn
    "username": "python",
    "password": "cisco",
    "secret": "cisco",  # enable secret
    "port": 22,
}

try:
    connection = ConnectHandler(**device)  # kết nối SSH
    connection.enable()  # vào enable

    while True:
        print("\n========== NETWORK TOOL ==========")
        print(f"Router: {device['host']}")
        print("----------------------------------")
        print("1.  Show ip interface brief")
        print("2.  Show version")
        print("3.  Show running-config (interfaces)")
        print("4.  Backup running-config ra file")
        print("5.  Ping tu ROUTER toi 1 dia chi")
        print("6.  Ping tu MAY TINH toi 1 dia chi")
        print("7.  Thoat")

        choice = input("Chon chuc nang (1-7): ").strip()

        if choice == "1":
            output = connection.send_command("show ip int brief")
            print("\n=== KET QUA LENH SHOW IP INT BRIEF ===")
            print(output)

        elif choice == "2":
            output = connection.send_command("show version")
            print("\n=== THONG TIN PHAN MEM (SHOW VERSION) ===")
            print(output)

        elif choice == "3":
            output = connection.send_command("show running-config | section interface")
            print("\n=== CAU HINH CAC INTERFACE ===")
            print(output)

        elif choice == "4":
            output = connection.send_command("show running-config")
            filename = f"backup_running_config_{device['host']}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(output)
            print(f"\nDa backup running-config vao file: {filename}")

        elif choice == "5":
            target = input("Nhap dia chi IP muon ping tu ROUTER: ").strip()
            if target:
                cmd = f"ping {target} repeat 5"
                output = connection.send_command(cmd)
                print(f"\n=== KET QUA PING TU ROUTER TOI {target} ===")
                print(output)
            else:
                print("Khong co dia chi IP.")

        elif choice == "6":
            target = input("Nhap dia chi IP muon ping tu MAY TINH: ").strip()
            if target:
                print(f"\n=== KET QUA PING TU MAY TINH TOI {target} ===")
                # -n 4: Windows ping 4 goi
                completed = subprocess.run(
                    ["ping", "-n", "4", target],
                    text=True,
                    capture_output=True,
                    encoding="utf-8",
                )
                print(completed.stdout)
            else:
                print("Khong co dia chi IP.")

        elif choice == "7":
            print("Thoat chuong trinh.")
            break

        else:
            print("Lua chon khong hop le, vui long nhap 1-7.")

    connection.disconnect()

except NetmikoAuthenticationException:
    print("Sai username/password hoặc secret.")
except NetmikoTimeoutException:
    print("Khong ket noi duoc toi thiet bi.")
except Exception as e:
    print(f"Loi: {e}")