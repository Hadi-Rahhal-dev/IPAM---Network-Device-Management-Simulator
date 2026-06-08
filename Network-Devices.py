import json

class NetworkDevice:
    def __init__(self, name, mac, ip, device_type):
        self.name = name
        self.mac = mac.upper().strip()
        self.ip = ip.strip()
        self.type = device_type
        
    def show(self):
        print(f"Device name : {self.name}")
        print(f"Device Type : {self.type}")
        print(f"Mac address : {self.mac}")
        print(f"IP address  : {self.ip}")
        
    def to_dic(self):
        return {
            "name": self.name,
            "mac": self.mac,
            "ip": self.ip,
            "type": self.type
        }

def save_network(device_list):
    data = {
        "devices": [d.to_dic() for d in device_list]
    }
    with open("network.json", "w") as f:
        json.dump(data, f, indent=4)
        
def load_network():
    try:
        with open("network.json", "r") as f:
            data = json.load(f)
            device_list = []
            for item in data.get("devices", []):
                loaded_device = NetworkDevice(
                    item["name"],
                    item["mac"],
                    item["ip"],
                    item["type"]
                )
                device_list.append(loaded_device)
            return device_list
        
    except FileNotFoundError:
        router = NetworkDevice("Main_Gateway", "AA:BB:CC:11:22:33", "192.168.1.1", "Router")
        return [router]
        
devices = load_network()

gateway_device = devices[0] 
gateway_subnet = gateway_device.ip.split(".")[0:3]

while True:
    print("1- Show Connected Devices")
    print("2- Add New Device (Subnet & IP/MAC Check)")
    print("3- Search Device")
    print("4- Ping Simulator (Test Connectivity)")
    print("5- Exit")
    
    choice = input("Choose from 1 to 5: ")
    print("-"*15)
    
    if choice == "1":
        for d in devices:
            d.show()
            print("^"*15)
        print("-"*15)
	
    elif choice == "2":
        a = input("Which device you want to add: ")
        name_exists = False
        
        for d in devices:
            if d.name.lower() == a.lower():
                name_exists = True
                break
                
        if name_exists:
            print("🛑 This device name is already added to the network!")
            print("-"*15)
        else:
            device_type = input("Device name is available ✓, Now what is the type of new device: ")
            
            print("\n--- Current IPs in the network ---")
            for d in devices:
                print(f"- {d.ip}")
            print("----------------------------------\n")
            
            while True:
                ip = input(f"Enter a unique IP (Must be in subnet {'.'.join(gateway_subnet)}.X): ")
                
                ip_parts = ip.split(".")[0:3]
                if ip_parts != gateway_subnet:
                    print(f"🛑 Subnet Error! Device must be in the same network as Gateway ({'.'.join(gateway_subnet)}.X)")
                    continue 
                
                ip_conflict = False
                for d in devices:
                    if d.ip == ip:
                        ip_conflict = True
                        break
                
                if ip_conflict:
                    print("~ This IP is already taken! Please enter a unique IP.")
                else:
                    break 
                    
            while True:
                mac = input("Enter a unique MAC: ")
                mac_conflict = False
                
                for d in devices:
                    if d.mac == mac.upper().strip():
                        mac_conflict = True
                        break
                
                if mac_conflict:
                    print("~ This MAC is already taken! Please enter a unique MAC address.")
                else:
                    break 
                    
            new_device = NetworkDevice(a, mac, ip, device_type)
            devices.append(new_device)
            print("New Device added to system successfully ✓")
            save_network(devices)
            print("-"*15)
            
    elif choice == "3":
        a = input("Which device you want to search (name or ip or mac): ")
        found = False
        
        for d in devices:
            if a.lower() == d.name.lower() or a == d.ip or a.upper() == d.mac:
                print(f"Name: {d.name} | Type: {d.type} | Mac: {d.mac} | IP: {d.ip}")
                found = True
        if not found:
            print("~ This device is not found")
        print("-"*15)
    
    elif choice == "4":
        src_name = input("Enter source device name (Who is pinging?): ")
        dst_ip = input("Enter destination IP to ping: ")
        
        src_exists = False
        dst_exists = False
        
        for d in devices:
            if d.name.lower() == src_name.lower():
                src_exists = True
                break
                
        for d in devices:
            if d.ip == dst_ip:
                dst_exists = True
                break
                
        print(f"\nPinging {dst_ip} from {src_name}...")
        
        if src_exists and dst_exists:
            print(f"Reply from {dst_ip}: bytes=32 time=4ms TTL=64")
            print(f"Reply from {dst_ip}: bytes=32 time=5ms TTL=64")
            print("📊 Ping statistics: Packets: Sent = 2, Received = 2, Lost = 0 (0% loss) ✅")
        else:
            print("Request timed out. ❌")
            print("📊 Ping statistics: Packets: Sent = 2, Received = 0, Lost = 2 (100% loss)")
        print("-"*15)
    	
    elif choice == "5":
        print("System exit, goodbye")
        break
