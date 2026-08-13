from typing import Any


PRODUCTS = [
	("LAPTOP-01", "Acer Aspire 5 15", "Laptops", "Acer", 54990, "16 GB RAM|512 GB SSD|15.6 inch display"),
	("LAPTOP-02", "ASUS Vivobook 15 OLED", "Laptops", "ASUS", 66990, "OLED display|16 GB RAM|512 GB SSD"),
	("LAPTOP-03", "Lenovo IdeaPad Slim 5", "Laptops", "Lenovo", 71990, "Ryzen performance|16 GB RAM|Lightweight chassis"),
	("LAPTOP-04", "Dell Inspiron 14 Plus", "Laptops", "Dell", 78990, "14 inch display|Intel Core Ultra|Backlit keyboard"),
	("LAPTOP-05", "HP Pavilion Aero 13", "Laptops", "HP", 74990, "Ultra-light design|16 GB RAM|Fast charging"),
	("LAPTOP-06", "Apple MacBook Air 13", "Laptops", "Apple", 99900, "Apple silicon|Liquid Retina display|All-day battery"),
	("LAPTOP-07", "MSI Modern 14", "Laptops", "MSI", 58990, "Business portability|Wi-Fi 6E|Backlit keyboard"),
	("LAPTOP-08", "Samsung Galaxy Book4", "Laptops", "Samsung", 82990, "AMOLED display|Galaxy integration|Premium aluminium"),
	("DESKTOP-01", "Dell OptiPlex Business Desktop", "Desktop Computers", "Dell", 62990, "Intel Core i5|16 GB RAM|512 GB SSD"),
	("DESKTOP-02", "HP Pro Tower 280", "Desktop Computers", "HP", 57990, "Expandable tower|Business security|Wired keyboard"),
	("DESKTOP-03", "Lenovo ThinkCentre Neo 50", "Desktop Computers", "Lenovo", 59990, "Compact tower|Tool-free access|Energy efficient"),
	("DESKTOP-04", "ASUS ExpertCenter D5", "Desktop Computers", "ASUS", 64990, "Enterprise reliability|Quiet cooling|Dual display"),
	("DESKTOP-05", "Acer Veriton Workstation", "Desktop Computers", "Acer", 68990, "Professional graphics ready|Expandable memory|TPM security"),
	("DESKTOP-06", "Apple Mac mini", "Desktop Computers", "Apple", 69900, "Compact design|Apple silicon|Thunderbolt connectivity"),
	("AIO-01", "HP All-in-One 24", "All-in-One Computers", "HP", 75990, "23.8 inch display|Wireless keyboard|Integrated webcam"),
	("AIO-02", "Lenovo IdeaCentre AIO 3", "All-in-One Computers", "Lenovo", 72990, "FHD display|Harman audio|Space-saving stand"),
	("AIO-03", "Dell Inspiron All-in-One 24", "All-in-One Computers", "Dell", 81990, "Touch display|Pop-up webcam|Dual speakers"),
	("AIO-04", "ASUS AiO V241", "All-in-One Computers", "ASUS", 69990, "NanoEdge display|SonicMaster audio|HDMI input"),
	("MONITOR-01", "Samsung ViewFinity 27-inch Monitor", "Monitors", "Samsung", 24990, "QHD resolution|IPS panel|Height adjustable"),
	("MONITOR-02", "Dell UltraSharp 27 USB-C Monitor", "Monitors", "Dell", 42990, "USB-C hub|Colour accurate|Ergonomic stand"),
	("MONITOR-03", "LG UltraGear 27 Gaming Monitor", "Monitors", "LG", 31990, "165 Hz refresh|1 ms response|Adaptive sync"),
	("MONITOR-04", "BenQ Eye-Care 24 Monitor", "Monitors", "BenQ", 15990, "Low blue light|Flicker free|Slim bezel"),
	("MONITOR-05", "Acer Nitro 24 Gaming Monitor", "Monitors", "Acer", 18990, "180 Hz refresh|Full HD|HDR support"),
	("MONITOR-06", "ASUS ProArt 27 Monitor", "Monitors", "ASUS", 38990, "Factory calibrated|100 percent sRGB|USB-C"),
	("KEYBOARD-01", "Logitech MX Keys S", "Keyboards and Mice", "Logitech", 10995, "Smart illumination|Multi-device|USB-C charging"),
	("KEYBOARD-02", "Dell Premier Wireless Keyboard", "Keyboards and Mice", "Dell", 7990, "Multi-device|Numeric keypad|Long battery life"),
	("KEYBOARD-03", "HP 350 Compact Keyboard", "Keyboards and Mice", "HP", 2999, "Compact layout|Bluetooth|Travel friendly"),
	("MOUSE-01", "Logitech MX Master 3S", "Keyboards and Mice", "Logitech", 9495, "Quiet clicks|8K DPI sensor|MagSpeed wheel"),
	("MOUSE-02", "Razer DeathAdder Essential", "Keyboards and Mice", "Razer", 2499, "Gaming sensor|Ergonomic grip|Mechanical switches"),
	("MOUSE-03", "Microsoft Bluetooth Mouse", "Keyboards and Mice", "Microsoft", 1899, "Compact design|Bluetooth|Precise tracking"),
	("STORAGE-01", "Samsung T7 Portable SSD 1TB", "Storage", "Samsung", 9990, "USB 3.2|1050 MBps read|Shock resistant"),
	("STORAGE-02", "WD My Passport 2TB", "Storage", "Western Digital", 7290, "Password protection|Automatic backup|Portable design"),
	("STORAGE-03", "SanDisk Extreme Portable SSD", "Storage", "SanDisk", 11990, "IP65 protection|Fast NVMe storage|Carabiner loop"),
	("STORAGE-04", "Seagate Expansion Desktop 4TB", "Storage", "Seagate", 10490, "High capacity|Plug and play|USB 3.0"),
	("NETWORK-01", "TP-Link Archer AX55 Router", "Networking", "TP-Link", 7999, "Wi-Fi 6|Gigabit ports|OneMesh support"),
	("NETWORK-02", "Netgear Nighthawk AX4 Router", "Networking", "Netgear", 12990, "Dual-band Wi-Fi 6|Security controls|Four antennas"),
	("NETWORK-03", "D-Link 8-Port Gigabit Switch", "Networking", "D-Link", 2499, "Eight gigabit ports|Fanless|Plug and play"),
	("NETWORK-04", "Ubiquiti UniFi Access Point", "Networking", "Ubiquiti", 13990, "Wi-Fi 6|PoE powered|Central management"),
	("AUDIO-01", "JBL Quantum 100 Headset", "Audio and Video", "JBL", 2999, "Detachable microphone|Memory foam|3.5 mm audio"),
	("AUDIO-02", "Logitech Z407 Speakers", "Audio and Video", "Logitech", 8995, "Bluetooth control|Subwoofer|80 watt output"),
	("WEBCAM-01", "Logitech C920 HD Pro Webcam", "Audio and Video", "Logitech", 7995, "Full HD video|Stereo microphones|Auto focus"),
	("WEBCAM-02", "Dell UltraSharp 4K Webcam", "Audio and Video", "Dell", 18990, "4K sensor|AI framing|Windows Hello"),
	("POWER-01", "APC Back-UPS 1100VA", "Power and Accessories", "APC", 8490, "Battery backup|Surge protection|Automatic voltage regulation"),
	("POWER-02", "CyberPower 1500VA UPS", "Power and Accessories", "CyberPower", 12990, "LCD status|USB management|Pure sine wave"),
	("DOCK-01", "Dell USB-C Dock WD19S", "Power and Accessories", "Dell", 21990, "Dual display|Power delivery|Gigabit Ethernet"),
	("DOCK-02", "Anker 8-in-1 USB-C Hub", "Power and Accessories", "Anker", 6999, "HDMI|Card reader|100 watt pass-through"),
	("PRINTER-01", "HP LaserJet Pro MFP", "Printers and Scanners", "HP", 28990, "Print scan copy|Wi-Fi|Automatic duplex"),
	("PRINTER-02", "Canon PIXMA MegaTank Printer", "Printers and Scanners", "Canon", 19990, "Refillable ink tanks|Borderless print|Wireless"),
	("PRINTER-03", "Epson EcoTank Office Printer", "Printers and Scanners", "Epson", 24990, "Low cost printing|ADF scanner|Ethernet"),
	("SCANNER-01", "Brother Compact Document Scanner", "Printers and Scanners", "Brother", 22990, "Duplex scan|Portable|Cloud workflows"),
]

GROUP_IMAGES = {
	"Laptops": "photo-1496181133206-80ce9b88a853",
	"Desktop Computers": "photo-1593640408182-31c70c8268f5",
	"All-in-One Computers": "photo-1527443224154-c4a3942d3acf",
	"Monitors": "photo-1527443154391-507e9dc6c5cc",
	"Keyboards and Mice": "photo-1587829741301-dc798b83add3",
	"Storage": "photo-1531492746076-161ca9bcad58",
	"Networking": "photo-1544197150-b99a580bb7a8",
	"Audio and Video": "photo-1590602847861-f357a9332bbc",
	"Power and Accessories": "photo-1601524909162-ae8725290836",
	"Printers and Scanners": "photo-1612815154858-60aa4c59eaa6",
}


def build_demo_catalog() -> dict[str, Any]:
	erpnext_items = []
	items = []
	catalog_memberships: dict[str, list[dict[str, Any]]] = {}
	for index, product in enumerate(PRODUCTS, start=1):
		code, name, group, brand, web_price, highlights = product
		item_code = f"CXSHOP-DEMO-{code}"
		image = _image_url(group, index)
		mrp = round(web_price * 1.1)
		erpnext_items.append({
			"item_code": item_code,
			"item_name": name,
			"item_group": group,
			"brand": brand,
			"stock_uom": "Nos",
			"description": f"{name} prepared for the online computer catalog.",
			"image": image,
			"is_stock_item": 1,
			"standard_rate": web_price,
		})
		items.append({
			"item_code": item_code,
			"item_name": name,
			"erpnext_item": item_code,
			"availability": "Immediately" if index % 4 else "Tomorrow",
			"item_group": group,
			"brand": brand,
			"short_description": f"{name} selected for dependable work, study, and business use.",
			"full_description": f"Explore {name} with transparent pricing, product imagery, and dependable support.",
			"web_price": web_price,
			"mrp": mrp,
			"image": image,
			"highlights": highlights,
			"published": 1,
		})
		catalog_memberships.setdefault(group, []).append({
			"ishop_item": item_code,
			"display_order": index * 10,
		})

	catalogs = []
	for group, memberships in catalog_memberships.items():
		catalogs.append({
			"catalog_code": f"CXSHOP-DEMO-{_catalog_code(group)}",
			"catalog_name": group,
			"description": f"Online product catalog for {group.lower()}.",
			"catalog_image": _image_url(group, 100 + len(catalogs)),
			"published": 1,
			"catalog_items": memberships,
		})
	return {"erpnext_items": erpnext_items, "items": items, "catalogs": catalogs}


def _image_url(group: str, signature: int) -> str:
	photo = GROUP_IMAGES[group]
	return f"https://images.unsplash.com/{photo}?auto=format&fit=crop&w=1200&q=80&sig={signature}"


def _catalog_code(group: str) -> str:
	return "-".join(part.upper() for part in group.replace("and", " ").split())
